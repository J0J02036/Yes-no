print("🎲🎲 Roll it 13 🎲🎲")

# loop for testing purposes

while True:
    want_instructions = input("do you want to read the instructions ").lower()
    print(want_instructions)
    print(f"you answered {want_instructions} to the question")

    # checks for yes or no
    if want_instructions == "yes" or want_instructions == "y":
        print("you chose yes")

    elif want_instructions == "no" or want_instructions == "n":
        print("you chose no")

    else:
        print("you did not insert a valid response")
