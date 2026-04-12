#Printing specific outputs considering the condition.

#Asking for input.
text = input("Greeting: ")

#Converting the string in lowercase and striping whitespaces from both end.
text = text.casefold().strip()

#Checking the condition and printing result.
if "hello" in text:
    print(100)
elif "h" in text:
    print(20)
else:
    print(0)    


