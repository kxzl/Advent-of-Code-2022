# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 08:11:01 2022

@author: romslo
"""

#Read txt file
with open('input.txt') as f:
    input = f.read()
    
crate_stack, moves = input.split('\n\n')
crates = crate_stack.split('\n')

#remove bottom row in list with 1 2 3
crates.pop()
crate_stack = [list("".join(stack_column).strip()[::-1]) for stack_column in zip(*crates)]

c_stack = []
for element in crate_stack:
    # Check that list is not empty
    if element: 
        #check if characters, if yes, keep
        if (element[0]).isalpha():
            c_stack.append(element)

#%%
# do the moves
moves = moves.split('\n')
for move in moves:
    m_amount = int(move.split(' ')[1])
    m_from = int(move.split(' ')[3])-1 #-1 since my first stacks name i s 0 not 1
    m_to = int(move.split(' ')[5])-1 #-1 since my first stacks name i s 0 not 1
    
    for a in range(m_amount):
        c_stack[m_to].append(c_stack[m_from][-1])
        c_stack[m_from].pop()
    
answer = ""
for stack in c_stack:
    answer += stack[-1]
    
print(answer)

        