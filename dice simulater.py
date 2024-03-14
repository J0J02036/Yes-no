# import random
import random


# generates a random number between
# to simulate a roll of a die

def roll_die():
    result = random.randint(a=1, b=6)
    return result



# main routine starts here

for item in range(0, 10):
        user_score = 0
        double_score = "no"

        # roll two dice
        roll_1 = roll_die()
        roll_2 = roll_die()

        # checks for double score opportunity
        if roll_1 == roll_2:
            double_score = "yes"

        # find total points (so far)
        user_points = roll_1 + roll_2

        # show the results
        print()
        print()
        print(f"die 1: {roll_1}      die 2: {roll_2}     points: {user_points}")
        print(f"double score opportunity: {double_score}")