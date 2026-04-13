# Converts time into a meal time message.

# User inputs time and  convert function calls for converted input by which conditions are checked.
def main():
    text = input("What time is it? ")
    text = convert(text)
    if 7.0 <= text <= 8.0:
        print("breakfast time")
    elif 12.0 <= text <=13.0:
        print("lunch time")
    elif 18.0 <= text <= 19.0:
        print("dinner time")

# Convert function converts the user input into a decimal float.
def convert(time):
   time = time.split(":")
   return(int(time[0]) + (int(time[1]) / 60))

# Calls main again.
if __name__ == "__main__":
    main()



