import requests
from datetime import datetime, timedelta
from fpdf import FPDF
from itertools import combinations
import os


def get_user_inputs():
    while True:
        country = input("Country: ").strip().title()
        city = input("City: ").strip().title()
        prayer_times = fetch_prayer_times(city, country)
        if not prayer_times:
            continue
        break

    # Available time window: 24hr format
    while True:
        try:
            start = datetime.strptime(input("Available from\nStart (HH:MM): "), "%H:%M")
            break
        except ValueError:
            print("Invalid format. Use HH:MM like 07:05")
    while True:
        try:
            end = datetime.strptime(input("End (HH:MM): "), "%H:%M")
            if end > start:
                break
            else:
                print("End time must be after start time.")
        except ValueError:
            print("Invalid format. Use HH:MM like 13:55")

    while True:
        try:
            total_hours = float(input("Total study hours: "))
            window_hours = (end - start).seconds / 3600
            if 0 < total_hours <= window_hours:
                break
            else:
                print(f"Enter a number between 0 and {window_hours} hours.")
        except ValueError:
            print("Enter a number(hours). Example: 3.5")

    block = get_block(total_hours)
    block_break = get_block_break()

    while True:
        try:
            buffer = float(input("Prayer break time(minutes): "))
            if 0 <= buffer <= 60:
                break
            else:
                print("Enter between 0 to 60 minutes")
        except ValueError:
            print("Enter a number(minutes). Example: 15")

    return city, country, prayer_times, start, end, total_hours, block, block_break, buffer


def get_block(total_hours):
    while True:
        try:
            block = float(input("How many hours per study block?: "))
            if 0 < block <= total_hours:
                if total_hours % block != 0:
                    print(f"Total hours must be divisible by block size. {total_hours} hours is not divisible by {block}")
                    continue
                return block
            print(f"Enter a number between 0 and {total_hours} hours.")
        except ValueError:
            print("Enter a number(hours). Example: 1.5")


def get_block_break():
    while True:
        try:
            block_break = float(input("Break between blocks (minutes): "))
            if 0 <= block_break <= 120:
                return block_break
            print("Enter between 0 to 120 minutes.")
        except ValueError:
            print("Enter a number(minutes). Example: 10")


def fetch_prayer_times(city, country):
    # Calls Aladhan API, returns 5 prayer times as datetime.time objects
    try:
        url = f"http://api.aladhan.com/v1/timingsByCity?city={city}&country={country}&method=2"
        response = requests.get(url)
        if response.status_code != 200:
            print("Location not found. Try again.")
            return False
        try:
            data = response.json()
        except requests.exceptions.JSONDecodeError:
            print("Location not found. Try again.")
            return None
        timings = data["data"]["timings"]
        result = {}
        for prayer in ["Fajr", "Dhuhr", "Asr", "Maghrib", "Isha"]:
            result[prayer] = datetime.strptime(timings[prayer], "%H:%M").time()
        return result
    except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
        print("Network error. Check your internet connection.")
        return None


def check_existing_schedule(date):
    filename = f"schedule_{date}.pdf"
    return os.path.exists(filename)


def get_gaps(start, end, prayer_times, buffer):
    # Finds free time slots between prayer times within the available window
    # 10 mins before prayer = preparation time, buffer after = prayer duration
    gaps = []
    prayers_in_window = sorted([t for t in prayer_times.values() if start.time() < t < end.time()])
    current = start.time()
    for prayer in prayers_in_window:
        time = datetime.combine(datetime.today(), prayer)
        gap_end = (time - timedelta(minutes=10)).time()
        next_start = (time + timedelta(minutes=buffer)).time()
        gaps.append((current, gap_end))
        current = next_start
    gaps.append((current, end.time()))
    return gaps


def generate_arrangements(gaps, block, block_break, total_hours):
    possible_blocks = []
    for gap_start, gap_end in gaps:
        today = datetime.today()
        _block = timedelta(hours=block)
        _position = datetime.combine(today, gap_start)
        while (_position + _block).time() <= gap_end:
            block_start = _position.time()
            block_end = (_position + _block).time()
            possible_blocks.append((block_start, block_end))
            _position = _position + timedelta(minutes=30)

    # Yields valid combinations: no overlaps, user-defined break enforced between blocks
    num_blocks = int(total_hours / block)
    for combo in combinations(possible_blocks, num_blocks):
        sorted_combo = sorted(combo, key=lambda x: x[0])
        valid = True
        for i in range(len(sorted_combo) - 1):
            gap_after_block = (datetime.combine(datetime.today(), sorted_combo[i][1]) + timedelta(minutes=block_break)).time()
            if gap_after_block > sorted_combo[i + 1][0]:
                valid = False
                break
        if valid:
            yield sorted_combo


def display_and_select(arrangements, prayer_times):
    # Prints all options in a box layout and returns the user's chosen arrangement
    date = datetime.today().strftime("%d %B %Y")
    print("╔══════════════════════════════════════╗")
    header = f"║  DAILY SCHEDULE - {date}"
    print(header.ljust(39) + "║")
    print("╠══════════════════════════════════════╣")
    print("║  PRAYER TIMES".ljust(39) + "║")
    for name, time in prayer_times.items():
        line = f"║  {name:<10}{time.strftime('%H:%M')}"
        print(line.ljust(39) + "║")
    for i, arrangement in enumerate(arrangements, 1):
        print("╠══════════════════════════════════════╣")
        print(f"║  OPTION {i}".ljust(39) + "║")
        for j, (block_start, block_end) in enumerate(arrangement, 1):
            line = f"║  {block_start.strftime('%H:%M')} - {block_end.strftime('%H:%M')}  Study Block {j}"
            print(line.ljust(39) + "║")
    print("╚══════════════════════════════════════╝")

    while True:
        try:
            choice = int(input("Choice: "))
            if 1 <= choice <= len(arrangements):
                return arrangements[choice - 1]
            print(f"Choose between 1-{len(arrangements)}")
        except ValueError:
            print(f"Enter a number between 1-{len(arrangements)}")


def get_best_arrangements(gaps, block, block_break, total_hours):
    # Collects up to 100 valid arrangements from the generator
    arrangements = []
    for arrangement in generate_arrangements(gaps, block, block_break, total_hours):
        arrangements.append(arrangement)
        if len(arrangements) >= 100:
            break

    # Ranks by spread score (max gap between blocks) and keeps top 5
    def spread_score(combo):
        sorted_combo = sorted(combo, key=lambda x: x[0])
        total_gap = 0
        for i in range(len(sorted_combo) - 1):
            end = datetime.combine(datetime.today(), sorted_combo[i][1])
            start = datetime.combine(datetime.today(), sorted_combo[i + 1][0])
            total_gap += (start - end).seconds
        return total_gap

    arrangements = sorted(arrangements, key=spread_score, reverse=True)[:5]
    if not arrangements:
        return None
    return arrangements


def save_pdf(arrangements, prayer_times):
    BASE = os.path.dirname(os.path.abspath(__file__))
    date = datetime.today().strftime("%Y-%m-%d")

    # Page setup
    pdf = FPDF(orientation="portrait", format="A4")
    pdf.add_page()
    pdf.set_auto_page_break(auto=False)
    pdf.set_left_margin(25)
    pdf.set_right_margin(25)

    # Islamic geometric background image
    bg_path = os.path.join(BASE, "schedule.png")
    pdf.image(bg_path, x=0, y=0, w=210, h=297)

    # Gold border boxes for header and footer
    pdf.set_draw_color(180, 140, 60)
    pdf.set_line_width(0.5)
    pdf.rect(0, 0, 209.5, 39)
    pdf.rect(0, 276, 209.5, 20.5)

    # Title in header
    pdf.set_text_color(212, 170, 45)
    pdf.set_font("helvetica", style="B", size=30)
    pdf.set_y(13)
    pdf.cell(0, 10, "DAILY SCHEDULE", align="C")

    # Prayer times section
    pdf.set_y(45)
    pdf.set_text_color(212, 170, 45)
    pdf.set_font("helvetica", style="B", size=20)
    pdf.cell(0, 8, "PRAYER TIMES", align="L")
    pdf.ln(10)
    pdf.line(7, pdf.get_y(), 203, pdf.get_y())
    pdf.ln(7)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("helvetica", size=17)
    for name, time in prayer_times.items():
        pdf.cell(60, 7, name, align="L")
        pdf.cell(0, 7, time.strftime('%H:%M'), align="L")
        pdf.ln(10)

    # Study schedule section
    pdf.ln(15)
    pdf.set_text_color(212, 170, 45)
    pdf.set_font("helvetica", style="B", size=20)
    pdf.cell(0, 8, "STUDY SCHEDULE", align="L")
    pdf.ln(10)
    pdf.line(7, pdf.get_y(), 203, pdf.get_y())
    pdf.ln(7)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("helvetica", size=17)
    for j, (block_start, block_end) in enumerate(arrangements, 1):
        pdf.cell(60, 7, f"Block {j}", align="L")
        pdf.cell(0, 7, f"{block_start.strftime('%H:%M')} - {block_end.strftime('%H:%M')}", align="L")
        pdf.ln(10)

    # Date in footer
    pdf.set_y(-15)
    pdf.set_text_color(212, 170, 45)
    pdf.set_font("helvetica", size=20)
    pdf.cell(0, 8, date, align="C")

    pdf.output(os.path.join(BASE, f"schedule_{date}.pdf"))


def main():
    date = datetime.today().strftime("%Y-%m-%d")
    value = False
    if check_existing_schedule(date):
        print("Schedule for today already exists")
        while True:
            option = input("Change?(Y/N) ").lower()
            if option in ["change", "y", "yes"]:
                value = True
                break
            elif option in ["exit", "no", "n"]:
                print("Exited")
                exit()
            else:
                print("Please enter yes or no")
    else:
        value = True

    if value:
        city, country, prayer_times, start, end, total_hours, block, block_break, buffer = get_user_inputs()
        gaps = get_gaps(start, end, prayer_times, buffer)
        while True:
            arrangements = get_best_arrangements(gaps, block, block_break, total_hours)
            if arrangements is not None:
                break
            # Reprompt only block and break time, everything else stays locked
            print("No valid schedule could be generated. Please adjust your block duration or break time and try again.")
            block = get_block(total_hours)
            block_break = get_block_break()
        schedule = display_and_select(arrangements, prayer_times)
        save_pdf(schedule, prayer_times)
        print("Schedule saved")


if __name__ == "__main__":
    main()