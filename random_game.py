import sys
import random
sys.argv
while True:
    num = input("Please choose a number between 1 and 10:")
    try:
        random_num = random.randint(1, 11)
        if (int(num) == random_num):
            print(f"You guess right!\n The num was {random_num}")
            break
        elif (int(num) == 255):
            break
        elif (int(num) > 10):
            print('Type a number between 1 and 10\n Try again!5')
        else:
            print(f"Guess again!\n The num was {random_num}")
    except ValueError as Ve:
        raise Ve
        print('Type a number between 1 and 10\n Try again!')
    
