from itertools import *

x = [0,2,5,6]

i = 0
for P in combinations(range(0,10)):
    print(P)
    if i>10:
        break
    i+=1