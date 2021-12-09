import numpy as np 
import math

#initialize the matrix with a simple puzzle
board = np.zeros((9,9))
board[0,:] = [0,7,1,9,2,0,0,4,3]
board[1,:] = [0,4,0,8,0,1,6,0,0]
board[2,:] = [2,0,0,0,0,3,1,0,8]
board[3,:] = [5,0,0,7,3,4,0,6,0]
board[4,:] = [0,0,0,0,1,0,8,3,0]
board[5,:] = [1,0,0,0,8,5,0,7,4]
board[6,:] = [9,1,0,3,0,2,0,8,0]
board[7,:] = [0,0,7,5,0,0,0,1,0]
board[8,:] = [6,8,3,0,0,0,0,0,0]
board = board.astype('int8')
possible_numbers = [1,2,3,4,5,6,7,8,9]

def box(y,x): #which 3x3 box is it in as coordinates
    sub_box = (int(y/3)+1, int(x/3)+1)
    #print(sub_box)
    return sub_box
    
def check_box(y,x): #returns array of numbers in box
    sub_box_y, sub_box_x = box(y,x)
    box_contents = board[(3*sub_box_y-3):(3*sub_box_y),(3*sub_box_x-3):(3*sub_box_x)]
    #print(box_contents)
    return box_contents

def check_row(y,x): #returns array of numbers in row
    row = board[y,:]
    #print(row)
    return row

def check_column(y,x): #returns array of numbers in column
    column = board[:,x]
    #print(column)
    return column 

def check_coords(y,x): #returns possible numbers for a given set of coordinates
    box_contents = check_box(y,x).flatten()
    row = check_row(y,x)
    column = check_column(y,x)
    found = np.unique(np.concatenate((box_contents, row, column), axis = 0))
    answers = np.setdiff1d(possible_numbers, found, assume_unique=True)
    return answers

def find_zeros(): #finds all coordinate pairs for all zeros
    y,x = np.where(board == 0)
    zeros = list(zip(y,x))
    return zeros
    
def update(*array): #updates a zero to a value when a single solution is found 
    for zeros in array:
        for y,x in zeros:
            print(y,x)
            if (len(check_coords(y,x)) == 1):
                board[y,x] = check_coords(y,x)
                print(board)
                print(np.count_nonzero(board == 0))

for i in range(30):
    update(find_zeros())

