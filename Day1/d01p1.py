# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 07:48:04 2022

@author: romslo
"""

with open('input.txt') as f:
    lines = f.readlines()

max_cal = 0
count_cal = 0
for line in lines: 
    
    if line == "\n":
        if max_cal < count_cal:
            max_cal = count_cal
        count_cal = 0
    else:
        count_cal = count_cal + int(line)
    
print(max_cal)
        
    
    