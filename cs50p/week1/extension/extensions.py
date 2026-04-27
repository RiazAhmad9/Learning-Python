"""
extension.py
-------------
Outputs the MIME type of a file based on its extension.

- .strip().lower(): normalises input — handles case and whitespace
- .endswith(tuple): checks multiple extensions in one call
- application/octet-stream: default MIME type for unknown file types
"""

text = input("File name: ").strip().lower()

if text.endswith((".jpg", ".jpeg")):
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