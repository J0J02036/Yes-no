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

# checks that user inputs an integer
# that is more than 13
def int_check():
    while True:

        error = "please enter a integer that is 13 or above"

        try:
            response = int(input("enter an integer:  "))

            if response < 13:
                print(error)

            # checks if number is >13
            else:
                return response

                print("Your number is ", response)

        except ValueError:
            print(error)



# main routine
print()
print("🎲🎲 Roll it 13 🎲🎲")
print()

# loop for testing purposes

want_instructions = yes_no("do you want to read the instructions ")

if want_instructions == "yes":
    instructions()

print("program con tunes")
target_score = int_check()