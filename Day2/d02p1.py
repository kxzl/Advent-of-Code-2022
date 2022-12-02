# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 07:48:04 2022

Last 2 lines in input must be \n

@author: romslo

 Some rules
 
 ABC = opponent
 XYZ = me

# A and X Rock     - 1 point 
# B and Y Paper    - 2 points
# C and Z Scissors - 3 points

# lose              - 0 points
# draw              - 3 points
# win               - 6 points

"""

import numpy as np

#Load as a string matrix
input = np.loadtxt("input.txt", dtype='str', delimiter=' ')

# Convert from letters to values

input[(input == 'A') | (input == 'X')] = 1
input[(input == 'B') | (input == 'Y')] = 2
input[(input == 'C') | (input == 'Z')] = 3
input = input.astype(int)

# do the comparrison in each row
# Got to remember that Scossors 3 will be beat by Rock 1
points = 0
for row in input:
    # see how the game goes
    outcome = row[0] - row[1]
    # if -1 I win
    # if 1 opponent win
    # if -2 I win
    # if 2 Opponent win
    
    #Opponent win
    if (outcome == 1) | (outcome == -2):
        points = points + row[1] + 0
    # if I win
    elif (outcome == -1) | (outcome == 2):
        points = points + row[1] + 6
    # if draw
    else:
        points = points + row[1] + 3
        
print(points)
    