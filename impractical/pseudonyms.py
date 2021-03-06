"""generates random names and that"""

import random

print("Welcome to the Psych 'Sidekick Name Picker.'\n")
print("A name just like Sean would pick for Gus:\n\n")

first = ('Hamish', 'Blake', 'Matt', 'Reece', 'Ethan', 'Lachlan')

last = ('Lochran', 'Perry', 'Stephens', 'Leitz', 'Celis', 'Crouch')

while True:
    firstName = random.choice(first)

    lastName = random.choice(last)

    print("\n\n")
    print(f"{firstName} {lastName}")
    print("\n\n")

    try_again = input("\n\nTry again? (Press Enter else n to quit)\n ")
    if try_again.lower() == "n":
        break

    input("\nPress Enter to exit.")
