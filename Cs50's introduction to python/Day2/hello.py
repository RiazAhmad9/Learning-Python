# Print a greeting message

# Prompt the user for their name
name  = input("What is your name? ")

# Remove any leading or trailing whitespace and capitalize the first letter of each word
name  = name.strip().title()

# Split the name into parts and store the first part in a variable
first, last = name.split(" ")




# Print a greeting message using an f-string
print(f"Hello, {first}")