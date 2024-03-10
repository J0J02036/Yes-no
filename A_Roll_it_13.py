def yes_no(question):
    # loop for testing
    # checks for yous or no
    # repets if user doesn't enter a valid response
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("you did not insert a valid response")


def instructions():
    print('''
           ** instructions **
    
              do something
            do something else
                  ect
    
                 done :)
    ''')



# main routine
print()
print("🎲🎲 Roll it 13 🎲🎲")
print()

# loop for testing purposes

want_instructions = yes_no("do you want to read the instructions ")

if want_instructions == "yes":
    instructions()

print("program con tunes")