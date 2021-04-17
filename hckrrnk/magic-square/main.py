#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import *

# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    pass

def magicCheck(s):

    if (sum(s[0:3]) == sum(s[3:6]) == sum(s[6:9]) == sum(s[0::3]) == sum(s[1::3]) == sum(s[2::3]) == (s[0]+s[4]+s[8]) == (s[2]+s[4]+s[6])):
        return True
    return False


if __name__ == '__main__':

    s_m =  ['8 3 4','1 5 9','6 7 2']
    s_nm1 = ['4 9 2','3 5 7','8 1 5']
    s_nm2 = ['4 8 2','4 5 7','6 1 6']

    s_c2 = ['2 9 8','4 2 7','5 6 7']

    x = s_c2

    X = []
    X.extend(list(map(int,(x[0].split()))))
    X.extend(list(map(int,(x[1].split()))))
    X.extend(list(map(int,(x[2].split()))))


    Ans = 81
    for P in permutations(range(1,10)):
        if magicCheck(P):
            Ans = min(Ans, sum(abs(P[i] - X[i]) for i in range(0,9)))
    print(Ans)


    # result = formingMagicSquare(s_nm2)
    # print(result)




    
