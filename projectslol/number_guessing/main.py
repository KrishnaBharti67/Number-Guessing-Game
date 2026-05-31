import time
import random as rand

#variables
lower_range=1
higher_range=0
computer_number=0
attempts=0

difficulty=str(input('''
a)Easy (1-50) (e)
b)Medium (1-100) (m)
c)Hard (1-500) (h)
Choose a difficulty:'''))

def set_range():
    if difficulty.lower()=='e':
        return 50

    elif difficulty.lower()=='m':
        return 100

    elif difficulty.lower()=='h':
        return 500

    else:
        raise KeyError("Invalid Difficulty") 

def generate_computer(higher_range):
    computer_number=rand.randint(1,higher_range)
    return computer_number

def start_timer():
    time1=time.time()
    return time1

def end_time():
    final_time=time.time()
    return final_time

def working():
    found=False
    higher_range=set_range()
    computer_number=generate_computer(higher_range)
    start_Time=start_timer()
    attempts=0
    global difficulty

    name=str(input("Enter name to store in leaderboard:"))
    print(computer_number)
    while not found:
        try:
            n=int(input("Enter number:"))
            attempts+=1
        except:
            print("Enter valid number")
            continue
        
        if n>computer_number:
            print("Lower")
        elif n<computer_number:
            print("Higher")
        elif n==computer_number:
            break
        elif n < 1 or n > higher_range:
            print(f"Enter a number between 1 and {higher_range}")
            continue

    end_Time=end_time()

    time_elapsed=round(end_Time-start_Time)
    print(f"You win! It took you {time_elapsed}s and {attempts} attempts")

    return (name,difficulty,time_elapsed,attempts,)


def game():
    data=working()
    with open ("scores.txt","a") as ofile:
        ofile.write(str([data[0],data[1],data[2],data[3]])+'\n')

game()