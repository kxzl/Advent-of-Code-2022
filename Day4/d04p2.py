# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 12:58:20 2022

@author: romslo
"""
import re

with open('input.txt') as f:
    areas = f.readlines()
    
overlapping = 0
non_overlap = []
for cleaning_pair in areas:
    # split into list
    section = re.split(',|-|\n',cleaning_pair)
    
    elf1_start = int(section[0])
    elf1_end = int(section[1])
    elf2_start = int(section[2])
    elf2_end = int(section[3])
    
    # check if one of the elves has a section inside his partners by comparing their min max
    if elf1_start >= elf2_start and elf1_start <= elf2_end:
        overlapping += 1
    elif elf2_start >= elf1_start and elf2_start <= elf1_end:
        overlapping += 1
    else:
        non_overlap.append(cleaning_pair)