import random
def start():
    mat=[]
    for i in range(4):
        mat.append([0]*4)

    print('For moving left press : A or a')
    print('For moving right press : D or d')
    print('For moving up press : W or w')
    print('For moving down press : S or s')

    mat=add_new_2(mat)
    return mat

def add_new_2(mat):
    r=random.randint(0,3)
    c=random.randint(0,3)
    while mat[r][c]!=0:
        r=random.randint(0,3)
        c=random.randint(0,3)
    mat[r][c]=2
    return mat

def compress(mat):
    changed=False 
    new_mat=[]
    for i in range(4):
        new_mat.append([0]*4)

    for i in range(4):
        pos=0
        for j in range(4):
            if mat[i][j]!=0:
                new_mat[i][pos]=mat[i][j]

                if j!=pos:
                    changed=True
                pos+=1
    return new_mat,changed

def merged(mat):
    changed=False
    for i in range(4):
        for j in range(3):
            if mat[i][j]==mat[i][j+1]:
                mat[i][j]=mat[i][j]*2
                mat[i][j+1]=0
                changed=True 
    return mat,changed

def reverse(mat):
    new_mat=[]
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[i][3-j])
    return new_mat

def transpose(mat):
    new_mat=[]
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[j][i])
    return new_mat


def check_current_status(mat):

    for i in range(4):
        for j in range(4):
            if mat[i][j]==2048:
                return 'WON'
    
    for i in range(4):
        for j in range(4):
            if mat[i][j]==0:
                return 'GAME NOT OVER'
            
    for i in range(3):
        for j in range(3):
            if mat[i][j]==mat[i][j+1] or mat[i][j]==mat[i+1][j]:
                return 'GAME NOT OVER'
            
    for i in range(3):
        if mat[3][i]==mat[3][i+1]:
            return 'GAME NOT OVER'
    
    for j in range(3):
        if mat[j][3]==mat[j+1][3]:
            return 'GAME NOT OVER'
        
    return 'LOST'

def move_left(mat):
    new_mat,flag1=compress(mat)
    new_mat,flag2=merged(new_mat)
    new_mat,flag=compress(new_mat)
    flag=flag1 or flag2
    return new_mat,flag

def move_right(mat):
    new_mat=reverse(mat)
    new_mat,flag=move_left(new_mat)
    new_mat=reverse(new_mat)
    return new_mat,flag 

def move_up(mat):
    new_mat=transpose(mat)
    new_mat,flag=move_left(new_mat)
    new_mat=transpose(new_mat)
    return new_mat,flag

def move_down(mat):
    new_mat=transpose(mat)
    new_mat,flag=move_right(new_mat)
    new_mat=transpose(new_mat)
    return new_mat,flag
    

