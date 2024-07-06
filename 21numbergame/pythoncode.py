import random
def start():
    box=[]
    print('which turn will you take?(F/S)')
    choose=input('> ')
    turn=0
    if choose=='F':
        flag=True 
        while flag:
            while True:
                if turn%2==0:
                    print('''Enter the number of digits you want to choose? 
                          (number should be integer and should be less than or equal to 4
                          and the numbers should no excede 21)''')
                    x1=int(input("> "))
                    if len(box)==0:
                        for i in range(x1):
                            box.append(i)
                    else:
                        for i in range(box[-1]+1,box[-1]+1+x1):
                            box.append(i)
                    print('List of elements present in Box')
                    print(box)
                    if box[-1]==21:
                        print()
                        print('You loose.... \nbetter luck nexttime')
                        exit(0)
                else:
                    print('system is selecting the number')
                    y=4
                    if 21-box[-1]<4:
                        y=21-box[-1]  
                    x2=random.randint(1,y)
                    print(x2)
                    for i in range(box[-1]+1,box[-1]+1+x2):
                        box.append(i)
                    print('List of elements present in Box')
                    print(box)
                    if box[-1]==21:
                        print()
                        print('Congrats you won')
                        exit(0)
                turn+=1 
    elif choose=='S':
        while True:
            if turn%2==0:
                print('System selected number')
                if len(box)==0:
                    x1=random.randint(1,4)
                    for i in range(x1):
                        box.append(i)
                else:
                    y=4
                    if 21-box[-1]<4:
                        y=21-box[-1]
                    x1=random.randint(1,y)
                    for i in range(box[-1]+1,box[-1]+1+x1):
                        box.append(i)
                print()
                print(f'> {x1}')
                print()
                print('List of eleents present in box\n')
                print(box)
                if box[-1]==21:
                    print('\nYou Won! ')
                    exit(0)
            else:
                print('''Enter the number of digits you want to choose? 
                          (number should be integer and should be less than or equal to 4
                          and the numbers should no excede 21)''')
                x1=int(input('> '))
                for i in range(box[-1]+1,box[-1]+1+x1):
                    box.append(i)
                print(f'the elementspresent in box\n{box}\n')
                if box[-1]==21:
                    print('You Loose!\nBetter luck next time')
                    exit(0)
                
            turn +=1     



print('starting the game......')
print('if you want to play?(yes / no)')
ans=input('> ')
if ans=='yes':
    start()
elif ans=='no':
    print('exiting the game ')
    exit(0)
