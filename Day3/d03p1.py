# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 10:54:19 2022

@author: romslo
"""



#Read input
with open('input.txt') as f:
    rucksack_items = f.readlines()
    
missplaced_items = []
for items in rucksack_items:
    comp_1 = items[0:len(items)//2]
    comp_2 = items[len(items)//2:len(items)]
    
    missplaced_items.append((set(comp_1) & set(comp_2)).pop())
    
priority = ['dummy','a','b','c','d','e','f','g','h','i','j','k','l', 'm','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L', 'M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

prio_sum = 0
for item in missplaced_items:
    prio_sum += priority.index(item)