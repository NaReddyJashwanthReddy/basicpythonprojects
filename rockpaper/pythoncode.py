import random

choices=['Rock','Paper','Scissors']
print('Winning rules of the game ROCK PAPER SCISSORS are :\n'
      + "Rock vs Paper -> Paper wins \n"
      + "Rock vs Scissors -> Rock wins \n"
      + "Paper vs Scissors -> Scissor wins \n")

while True:

    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")

    usechoice=input('please enter the choice : ')
    usechoice=usechoice.lower()

    print('system is choosing.......')
    syschoice=random.choice(choices)
    syschoice=syschoice.lower()


    print(f'system choice : {syschoice}')

    if usechoice=='rock' and syschoice=='paper':
        print('YOU LOOSE')
        exit(0)
    elif usechoice=='paper' and syschoice=='rock':
        print('YOU WON')
        exit(0)
    if usechoice=='rock' and syschoice=='scissors':
        print('YOU WIN')
        exit(0)
    elif usechoice=='scissors' and syschoice=='rock':
        print('YOU LOOSE')
        exit(0)
    if usechoice=='paper' and syschoice=='scissors':
        print('YOU LOOSE')
        exit(0)
    elif usechoice=='scissors' and syschoice=='paper':
        print('YOU WON')
        exit(0)
    else:
        print('invalid choice')
