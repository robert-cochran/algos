#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    up_lim = n+1
    down_lim = 0
    right_lim = n+1
    left_lim = 0
    for obs in obstacles:
        #up_lim
        if obs[1] == c_q:
            if obs[0] > r_q and obs[0] < up_lim:
                up_lim = obs[0]
            #down limit
            if obs[0] < r_q and obs[0] > up_lim:
                down_lim = obs[0]
        if obs[0] == r_q:
            if obs[1] > c_q and obs[1] < right_lim:
                right_lim = obs[1]
            #down limit
            if obs[1] < c_q and obs[1] > left_lim:
                left_lim = obs[1]
    # for i in range(0,n):
    #     if obs[r_q + i][c_q + i]
    
    if up_lim > n:
        up_lim = n
    if right_lim > n:
        right_lim = n
    if down_lim < 1:
        down_lim = 1
    if left_lim < 1:
        left_lim = 1
    
    print(left_lim)

    left, right, up, down = c_q-left_lim, right_lim-c_q, up_lim-r_q, r_q-down_lim
    # print(up_lim, down_lim, right_lim, left_lim)
    diag_ur, diag_ul, diag_br, diag_bl = min(up, right), min(up, left), min(down, right), min(down, left)
    moves = [left, right, up, down, diag_ur, diag_ul, diag_br, diag_bl]
    print(moves)
    return sum(moves)
    

# function obstacleFilter(obstacles, n):


    
    
if __name__ == '__main__':
    f = open('in1.txt', 'r')

    nk = f.readline().split()
    n = int(nk[0])
    k = int(nk[1])
    r_qC_q = f.readline().split()
    r_q = int(r_qC_q[0])
    c_q = int(r_qC_q[1])
    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, f.readline().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)
    print(result)
    f.close()