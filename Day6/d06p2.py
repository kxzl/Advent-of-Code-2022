# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 20:11:23 2022

@author: romslo
"""

with open('input.txt') as f:
    input = f.readlines()
    
num_of_char = 14

for code in input:
    for i in range(len(code)):
        marker = code[i:num_of_char+i]
        if len(set(marker)) == len(marker):
            print(str(i+num_of_char) + " " + marker)
            break