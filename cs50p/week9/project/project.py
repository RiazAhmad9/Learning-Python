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
        if prayer_times:
            break
    while True:
        try:
            start = datetime.strptime(input("Available from\nStart (HH:MM): "), "%H:%M")
        except ValueError:
            print("Invalid format. Use HH:MM like 07:05")
            continue
        try:
            end = datetime.strptime(input("End (HH:MM): "), "%H:%M")
            if end > start:
                break
            else:
                print("End time must be after start time.")
        except ValueError:
            print("Invalid format. Use HH:MM like 13:55")
            continue
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
    while True:
        try:
            block = float(input("How many hours per study block?: "))
            if 0 < block <= total_hours:
                if total_hours % block != 0:
                    print(f"Total hours must be divisible by block size. {total_hours} hours is not divisible by {block}")
                    continue
                break
            else:
                print(f"Enter a number between 0 and {total_hours} hours.")
        except ValueError:
            print("Enter a number(hours). Example: 1.5")
    while True:
        try:
            buffer = float(input("Prayer break time(minutes): "))
            if 0 < buffer <= 60:
                break
            else:
                print("Enter between 0 to 60 minutes")
        except ValueError:
            print("Enter a number(minutes). Example: 15")
    return city, country, prayer_times, start, end, total_hours, block, buffer


def fetch_prayer_times(city, country):
    try:
        url = f"http://api.aladhan.com/v1/timingsByCity?city={city}&country={country}&method=2"
        response = requests.get(url)
        if response.status_code != 200:
            print("Location not found")
            return False
        data = response.json()
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
    gaps = []
    prayers_in_window = sorted([t for t in prayer_times.values() if start.time() < t < end.time()])
    current = start.time()
    for prayer in prayers_in_window:
        dt = datetime.combine(datetime.today(), prayer)
        gap_end = (dt - timedelta(minutes=buffer)).time()
        next_start = (dt + timedelta(minutes=10)).time()
        gaps.append((current, gap_end))
        current = next_start
    gaps.append((current, end.time()))
    return gaps


def generate_arrangements(gaps, block, total_hours):
    possible_blocks = []
    for gap_start, gap_end in gaps:
        today = datetime.today()
        position = gap_start
        _block = timedelta(hours=block)
        _position = datetime.combine(today, position)
        while (_position + _block).time() <= gap_end:
            _position = datetime.combine(today, position)
            block_end = (_position + _block).time()
            possible_blocks.append((position, block_end))
            position = (block_end + timedelta(minutes=30)).time()
            _position = datetime.combine(today, position)
    num_blocks = int(total_hours / block)
    arrangements = []
    for combo in combinations(possible_blocks, num_blocks):
        sorted_combo = sorted(combo, key=lambda x: x[0])
        valid = True
        for i in range(len(sorted_combo) - 1):
            if sorted_combo[i][1] > sorted_combo[i+1][0]:
                valid = False
                break
        if valid:
            arrangements.append(combo)
    if not arrangements:
        print("No valid arrangements found. Try reducing study hours or block size.")
        return None
    return arrangements


def display_and_select(arrangements, prayer_times):
    today = datetime.today().strftime("%d %B %Y")
    print("╔══════════════════════════════════════╗")
    header = f"║  DAILY SCHEDULE · {today}"
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
            if  1 <= choice <= len(arrangements):
                return arrangements[choice - 1]
            print(f"Choose between 1-{len(arrangements)}")
        except ValueError:
            print(f"Enter a number between 1-{len(arrangements)}")


def save_pdf(schedule, date):
    ...


def main():
    ...


if __name__ == "__main__":
    main()