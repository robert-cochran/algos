#returns the matrix provided as an array that starts at the top left corner and spirals inwards
#m can be any m*n size
#row and column size must be consistent

from icecream import ic
import numpy as np

def spiral(m):
    rows = len(m)
    col = len(m[0])

    # algo1
    # could pop off the top row and add that, then take the matrix and rotate it around


if __name__ == '__main__':
    a = [1,2,3]
    b = [4,5,6]
    c = [7,8,9]
    m = [a, b, c]
    rot = [[0,1],[-1,0]]

    '''desired
    7 4 1
    8 5 2
    9 6 3
    '''

    '''
    zip of m gives spin around diagoonal
    1 4 7
    2 5 8
    3 6 9
    need to rotate it around the y axis
    '''

    '''
    [::-1] rotates around the horizontal
    7 8 9
    4 5 6
    1 2 3
    '''

    # ic(list(zip(zip(m))))

    # spiral(m)
    ic(m)
    # ic(list(zip(m[::-1])))
    hrz = m[::-1]
    diag = list(zip(hrz))
    ic(list(zip(diag)))


    # npm = np.array(m)
    # ic(npm)