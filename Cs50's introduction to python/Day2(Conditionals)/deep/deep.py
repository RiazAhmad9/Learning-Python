# Printing 'Yes' if the user inputs 42 or forty-two or forty two.

# Asking for input.
text = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

# Converting the string to lower case.
text = text.casefold()

#Printing 'Yes' if conditions meet, else printing 'No'.
if (text == "42" or text == "forty-two" or text == "forty two"):
    print("Yes")
else:
    print("No")

