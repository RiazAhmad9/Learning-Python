'''
inflect is a library that handles English language formatting.
inflect.engine() gives you access to its methods.
p.join() automatically handles all comma/and logic:
  ["Liesl"] → "Liesl"
  ["Liesl", "Friedrich"] → "Liesl and Friedrich"
  ["Liesl", "Friedrich", "Louisa"] → "Liesl, Friedrich, and Louisa"
Key rule: build your list FIRST, call p.join() AFTER the loop.
Control-D raises EOFError — we catch it to exit cleanly instead of crashing.
'''

import inflect

p = inflect.engine()
names = []

while True:
    try:
        text = input("Name: ")
        names.append(text)
    except EOFError:
        break

print("Adieu, adieu, to " + p.join(names))
