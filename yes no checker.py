def yes_no(question):

    while True:
        want_instructions = input(question).lower()

        if want_instructions == "yes" or want_instructions == "y":
            return "yes"

        elif want_instructions == "no" or want_instructions == "n":
            return "no"

        else:
            print("you did not insert a valid response")


want_instructions = yes_no("Do you want to read the instructions? ")
print(f"You chose {want_instructions}")

# main routine

roll_again = yes_no("do you want to roll again")
print(f"you said {roll_again} to rolling again")
