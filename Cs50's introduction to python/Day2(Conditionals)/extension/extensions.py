# Outputs the file media type if found.

# Asks inpu, converts string to lowercase and removes shitespaces from both end.
text = input("File name: ").strip().lower()

#Checks conditions and prints result.
if text.endswith(".jpg"):
    print("image/jpeg")
elif text.endswith(".jpeg"):
    print("image/jpeg")
elif text.endswith(".png"):
    print("image/png")
elif text.endswith(".gif"):
    print("image/gif")
elif text.endswith(".zip"):
    print("application/zip")
elif text.endswith(".txt"):
    print("text/plain")
elif text.endswith(".pdf"):
    print("application/pdf")
else:
    print("application/octet-stream")