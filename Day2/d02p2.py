# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 07:48:04 2022

Last 2 lines in input must be \n

@author: romslo

 Some rules
 
 ABC = opponent
 XYZ = me

# A Rock     - 1 point 
# B Paper    - 2 points
# C Scissors - 3 points

# X need to lose
# Y need to draw
# Z need to win

# lose              - 0 points
# draw              - 3 points
# win               - 6 points

"""

import numpy as np

#Load as a string matrix
input = np.loadtxt("input.txt", dtype='str', delimiter=' ')

# Convert from letters to values

input[input == 'A'] = 1
input[input == 'B'] = 2
input[input == 'C'] = 3
input[input == 'X'] = 0
input[input == 'Y'] = 3
input[input == 'Z'] = 6

input = input.astype(int)

print(input.sum)

# do the comparrison in each row
# Got to remember that Scossors 3 will be beat by Rock 1
points = 0
for row in input:

    #Opponent win
    if row[1] == 0:
        my_move = row[0] - 1 
        if my_move < 1:
            my_move = 3
        
    # if I win
    elif row[1] == 6:
        my_move = row[0] + 1 
        if my_move > 3:
            my_move = 1

    # if draw
    else:
        my_move = row[0]
    
    points = points + my_move + row[1]
        

    