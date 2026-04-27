"""
text_logger
--------------
Appends user input to a text file until 'done' is typed.

- open("name.txt", "a"): opens in append mode — creates file if it doesn't exist,
  adds to it if it does, never overwrites
- with statement: closes the file automatically after each write
- f"{text}\n": writes each entry on a new line
- 'done' as exit: gives user control over when to stop
"""

while True:
    text = input("Input: ")
    if text == "done":
        break
    try:
        with open("name.txt", "a") as file:
            file.write(f"{text}\n")
    except PermissionError:
        print("Permission denied — cannot write to file")