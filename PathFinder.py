import random
def r_search(maze, row, col):
   
    x = col + 1

    if maze[row][x] == 'p':
        #maze[row][x] = '*'
        return True , maze, row, x

    else:
        return False, maze, row, col

def l_search(maze, row, col):
   
    x = col - 1

    if maze[row][x] == 'p':
        #maze[row][x] = '*'
        return True , maze, row, x

    else:
        return False, maze, row, col

def search(maze, n,  row, col):

    for i in range(0, n):
        if (maze[i][col]) == 'p':
            maze[i][col] = '*'
            return maze, i, col

    print('There is no path through the Labyrinth')
    quit()

def u_search(maze, row, col):
    x = row - 1
    if maze[x][col] == 'p':
        #maze[x][col] = '*'
        return True, maze, x, col

    else:
        return False, maze, row, col

def d_search(maze, row, col):
    x = row + 1
    if maze[x][col] == 'p':
        #maze[x][col] = '*'
        return True, maze, x, col

    else:
        return False, maze, row, col
         
n = int(input('Enter the amount of rows in the maze: '))

maze = []

for i in range(0, n):
    print('Enter row', i+1, 'of the Labyrinth:')
    r = input()

    r = list(r)
    
    maze.append(r)
   
count = 1
hold = []
maze,new_r,new_c = search(maze, n, 0 , 0)
new_r1 = new_r
new_c1 = new_c

while new_c != len(maze[0])-1:
    
    
    def check_all(maze,new_r,new_c):
            
        answR, maze,new_rr, new_cr = r_search(maze, new_r, new_c)
        answU, maze,new_ru, new_cu = u_search(maze, new_r, new_c)
        answD, maze,new_rd, new_cd = d_search(maze, new_r, new_c)
        answL, maze,new_rl, new_cl = l_search(maze, new_r, new_c)
        x = random.randint(0,1)
        
        
        if (answR == True) and (answU == False) and (answD == False):
            maze[new_rr][new_cr] = '*'
            return maze, new_rr, new_cr

        elif (answL == True) and (answU == False) and (answD == False) and (answR == False):
            maze[new_rl][new_cl] = '*'
            return maze, new_rl, new_cl

        elif (answR == True) and (answU == False) and (answD == True):
            #x = 0
            if x == 0:
                maze[new_rr][new_cr] = '*'
                return maze, new_rr, new_cr
            if x == 1:
                maze[new_rd][new_cd] = '*'
                return maze, new_rd, new_cd

        elif (answR == True) and (answU == True) and (answD == False):
            #x = 0
            if x == 0:
                maze[new_rr][new_cr] = '*'
                return maze, new_rr, new_cr
            if x == 1:
                maze[new_ru][new_cu] = '*'
                return maze, new_ru, new_cu
        
        
        elif (answU == True) and (answD == False) and (answR == False):
            maze[new_ru][new_cu] = '*'
            return maze, new_ru, new_cu
        
            
        elif (answD == True) and (answU == False) and (answR == False):
            maze[new_rd][new_cd] = '*'
            return maze, new_rd, new_cd
        
        elif (answD == True) and (answU == True) and (answR == False):
            if x == 0:
                maze[new_rd][new_cd] = '*'
                return maze, new_rd, new_cd

            if x == 1:
                maze[new_ru][new_cu] = '*'
                return maze, new_ru, new_cu

        elif (answD == True) and (answU == True) and (answR == True):
            y = random.randint(0,2)
            if y == 0:
                maze[new_ru][new_cu] = '*'
                return maze, new_ru, new_cu

            if y == 1:
                maze[new_rd][new_cd] = '*'
                return maze, new_rd, new_cd
            
            if y == 2:
                maze[new_rr][new_cr] = '*'
                return maze, new_rr, new_cr
                

        elif(answD == False) and (answU == False) and (answR == False):
            c = len(maze)
            d = len(maze[0])
            for p in range(0, c):
                for o in range(0 ,d):
                    if maze[p][o] == '*':
                        maze[p][o] = 'p'
                        
                
            maze[new_r1][new_c1] = '*'
            return maze, new_r1, new_c1

    
    maze, new_r, new_c = check_all(maze,new_r,new_c)
    count = count + 1
    #print('This turns coords are', new_r, new_c)
  


col = len(maze[0])

for i in range(0, n):
    for j in range(0, col):
        print(maze[i][j], end = '')

    print(' ')
print('Congrats, You finished the maze. Your path was', count, 'cells long')

    










