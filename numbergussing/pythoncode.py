import random
import math

print('welcome to pyhton project \nNumber guessing game')

#lower bound
lower = int(input('Enter the lower bound : '))

#upper bound
upper = int(input('Enter the upper bound : '))

#system number
randomnumber= random.randint(lower,upper)

#number of attempts
total_chances = math.ceil(math.log(upper - lower +1,2))

print('Start the game')

count=0
flag=False

while count < total_chances:
    count +=1

    guess = int(input("enter your desired number : "))

    if guess == randomnumber:
        print("Congrats you did it")

        flag = True
        break 
    elif randomnumber > guess :
        print("your guess is a bit smaller")
    else:
        print("your guess is a bit big")

if not flag:
    print("The number is %d" % randomnumber)
    print("Better luck next time")
