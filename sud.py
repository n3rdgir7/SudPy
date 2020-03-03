import numpy as  np
from collections import Counter 


puzzle =[
    [0, 0, 0, 0, 0, 0, 0, 7, 0],
    [0, 0, 0, 0, 5, 0, 8, 0, 1],
    [0, 0, 6, 4, 1, 0, 0, 3, 5],
    [6, 0, 7, 0, 0, 0, 5, 2, 0],
    [0, 0, 0, 2, 0, 9, 0, 0, 0],
    [0, 4, 1, 0, 0, 0, 6, 0, 9],
    [9, 7, 0, 0, 2, 1, 4, 0, 0],
    [1, 0, 5, 0, 3, 0, 0, 0, 0],
    [0, 8, 0, 0, 0, 0, 0, 0, 0]
]
puzzle = np.array(puzzle, dtype='int8')
#print(puzzle)

def check_box(y, x, i):
    box = puzzle[(y*3):(y*3+3), (x*3):(x*3+3)]
    possible = ((np.argwhere(puzzle[(y*3):(y*3+3), :] == i))).astype(int)
    #print(possible)
    


for i in range(1, 6):     #check all 9 possible digits i    CHANGE ME BACK TO 1,10 AFTER TESTING!!
    print("i: ", i)
    boxes = ((np.argwhere(puzzle == i))/3).astype(int)     #array of boxes with number i (0-2)
    rows = boxes[:, 0]     #row of boxes 3x3 with i
    cols = boxes[:, 1]     #columns of boxes 3x3 with i
    #print(boxes)
    #print("rows: : ", rows)
    #print(cols)
   

    print()



    for key,value in Counter(boxes[:, 0]).items():     #check rows for count of i, k is box, value is count
        if (value == 2):     #if count of i is 2, we need to find 3rd i in that row
            col = int(3 - sum(cols[np.argwhere(rows == key)]))
            #print(col)
            for y in range((key*3),(key*3+3)):     #loop checks each of the 3 y rows in the box
                if not np.array([i]) in puzzle[y, :]:     #if i is not in that row 
                    possible = 0
                    for x in range((col*3),(col*3+3)):     #checks each of the 3 colums in the box
                    
                        if not np.array([i]) in puzzle[:, x] and puzzle[y, x] == 0:     #no i in column and empty spot
                            possible += 1
                            print(i, "is in: ", y,x)
                        print (y, x, possible)
                '''if possible == 1:
                    print("do it")
                        #puzzle[y][x] = i'''
                    


    print()     #puts a return after each i


print(puzzle)

print(("unsolved", np.count_nonzero(puzzle == 0)))     #shows the number of i in puzzle



