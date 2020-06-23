def check_row(grid,row,num):
    for i in range(9):
        if grid[row][i]==num:
            return False
    return True
def check_col(grid,col,num):
    for i in range(9):
        if grid[i][col]==num:
            return False
    return True
def check_block(grid,row,col,num):
    b1=row-row%3
    b2=col-col%3
    for i in range(3):
        for j in range(3):
            if grid[b1+i][b2+j]==num:
                return False
    return True
def num_fit(grid,num,row,col):
    if check_row(grid,row,num) and check_col(grid,col,num) and check_block(grid,row,col,num):
        return True
    return False
def no_filled(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                r=i
                c=j
                l=[True,r,c]
                return l
    l=[False]
    return l 
def possible(grid):
    ll=no_filled(grid)
    if not ll[0]:
        return True
    rr=ll[1]
    cc=ll[2]
    for i in range(1,10):
        if num_fit(grid,i,rr,cc):
            grid[rr][cc]=i
            if possible(grid):
                return True
            grid[rr][cc]=0
    return False
def display(grid):
    for i in range(9):
        for j in range(9):
            print(grid[i][j],end=" ")
        print()
grid=[[0, 0, 9, 0, 4, 7, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 1, 0, 6],
     [0, 8, 0, 0, 2, 0, 0, 0, 0],
     [8, 0, 1, 0, 0, 3, 0, 0, 0],
     [0, 7, 3, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 5, 4],
     [0, 0, 0, 2, 0, 0, 0, 0, 1],
     [3, 0, 0, 0, 0, 9, 0, 7, 0],
     [0, 9, 0, 8, 0, 6, 0, 4, 0]]
if possible(grid):
    display(grid)
else:
    print("No solution")
