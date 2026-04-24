'''
1.Stores every input from the user in a ".txt" file until they type done.
2.If ".txt" file isn't available then the code creates a ".txt" file.
3.Used "a" argument instead of "w" to append values every time rather than overwriting.
'''

while True:
    text = input("Input: ")
    if text == "done":
        break
    with open("1st.txt", "a") as file:
        file.write(f"{text}\n")
