# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 07:48:04 2022

Last 2 lines in input must be \n

@author: romslo
"""

# Read files
with open('input.txt') as f:
    lines = f.readlines()

# Initialize variables
max_cal = 0
count_cal = 0
top_tot = 0
cal_list = []

# Loop thorough file
for line in lines: 
    
    if line == "\n":
        
        if max_cal < count_cal:
            max_cal = count_cal
            
        cal_list.append(count_cal)
        count_cal = 0
        
    else:
        count_cal = count_cal + int(line)
    
cal_list.sort(reverse=True)
top_tot = cal_list[0] + cal_list[1] + cal_list[2]
        