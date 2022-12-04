# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 10:54:19 2022

@author: romslo
"""



#Read input
with open('input.txt') as f:
    rucksack_items = f.readlines()
    
common_badge = []
for x in range(0, len(rucksack_items)-2,3):
    elf_1 = (rucksack_items[x]).strip()
    elf_2 = (rucksack_items[x+1]).strip()
    elf_3 = (rucksack_items[x+2]).strip()
    
    common_badge.append((set(elf_1) & set(elf_2) & set(elf_3)).pop())
    
priority = ['dummy','a','b','c','d','e','f','g','h','i','j','k','l', 'm','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L', 'M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

prio_sum = 0
for item in common_badge:
    prio_sum += priority.index(item)