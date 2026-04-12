# Outputs the file media type if found.

# Asks input.
text = input("File name: ")

#Converts string to lowercase.
text = text.casefold().strip()

#Checks conditions and prints result.
if text.endswith(".jpg" or ".jpeg"):
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
