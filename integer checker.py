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


# main routine goes here
target_score = int_check()
print(target_score)