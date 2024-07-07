import logic

if __name__=='__mian__':

    pass

mat = logic.start()

print(mat)

while True:

    command=input('Please Enter the command : ')

    if command== 'A' or command == 'a':

        mat,flag=logic.move_left(mat)

        status=logic.check_current_status(mat)
        print(status)

        if status=='GAME NOT OVER':
            logic.add_new_2(mat)
        else:
            break

    elif command == 'D' or command == 'd':
        mat,flag=logic.move_right(mat)
        status=logic.check_current_status(mat)
        print(status)
        if status == 'GAME NOT OVER':
            logic.add_new_2(mat)
        else:
            break 

    elif command == 'S' or command == 's':
        mat,flag=logic.move_down(mat)
        status=logic.check_current_status(mat)
        print(status)
        if status=='GAME NOT OVER':
            logic.add_new_2(mat)
        else:
            break 

    elif command=='W' or command=='w':
        mat,flag=logic.move_up(mat)
        status=logic.check_current_status(mat)
        print(status)
        if status=='GAME NOT OVER':
            logic.add_new_2(mat)
        else:
            break 
    else:
        print('Invalid command')
    print(mat)