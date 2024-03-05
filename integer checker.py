# checks users integer
# more than 13
while True:

    error = "please enter a integer that is 13 or above"

    try:
                my_num = int(input("enter an integer:  "))


                if my_num <13:
                    print(error)

                #checks if number is >13
                else:

                    print("Your number is ", my_num)

    except ValueError:
                print(error)