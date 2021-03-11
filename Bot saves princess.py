# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 22:04:40 2021

@author: akshay
"""

def displayPathtoPrincess(n,grid):
    # Finding position of p and m
    for x,row in enumerate(grid):
        if 'p' in row:
            p = (x, row.index('p'))

        if 'm' in row:
            m = (x, row.index('m'))

    mov_rows =p[0]-m[0]
    mov_col= p[1]-m[1]

    if mov_rows < 0:
        direction1 = 'UP\n'* abs(mov_rows)
    else:  
        direction1 = 'DOWN\n'* abs(mov_rows)
    if mov_col <0:
        direction2 = 'LEFT\n'*abs(mov_col)
    else:
        direction2 = 'RIGHT\n'*abs(mov_col)
    
    direction= print(direction1 + direction2)
    return direction

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)
