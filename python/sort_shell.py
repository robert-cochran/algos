"""
Shell sort
Time Complexity: O()
Space Complexity: O()
"""

"""
why is bubble sort slower than quick and merge
i.e. quick sort uses a pivot but so does bubble sort, so why does quick sort perform better than bubble?
"""

def shell_sort():
    
    pass

if __name__ == "__main__":
    arr = [1,3,2,6,3,10,1,1,0,90,-1,0]
    arr2 = [10,50,80,0,100,25,75,60]
    arr3 = [10,10,10,0]
    arr4 = [0,10,10,10]
    arr5 = [0]
    arr6 = [0, 0]
    arr7 = [0,7,0]
    arr8 = [0,10]

    
    assert shell_sort(arr) == [-1, 0, 0, 1, 1, 1, 2, 3, 3, 6, 10, 90]
    assert shell_sort(arr2) == [0, 10, 25, 50, 60, 75, 80, 100]
    assert shell_sort(arr3) == [0, 10, 10, 10]
    assert shell_sort(arr4) == [0, 10, 10, 10]
    assert shell_sort(arr5) == [0] 
    assert shell_sort(arr6) == [0,0] 
    assert shell_sort(arr7) == [0,0,7] 


    ic(shell_sort(arr2))
    print(shell_sort(arr))
    print(shell_sort(arr2))
    print(shell_sort(arr3))
    print(shell_sort(arr4))
    print(shell_sort(arr5))
    print(shell_sort(arr6))
    print(shell_sort(arr7))