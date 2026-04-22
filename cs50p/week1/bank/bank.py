#Printing specific outputs considering the condition.

#Asking for input and converting the string in lowercase and striping whitespaces from both end,
text = input("Greeting: ").lower().strip()

#Checking the condition and printing result.
if text.startswith("hello"):
    print("$0")
elif text.startswith("h"):
    print("$20")
else:
    print("$100")