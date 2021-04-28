"""
Time Complexity: O(n log n)
Space Complexity: O(n) or O(n log n) reasoning being we are passing halved copies down the tree
    these only exist for one leg of the tree at a time though
"""

from icecream import ic

def queue():
    def __init__(arr):
        self.arr = arr

    def next(self):
        return self.arr.pop(0)

    def add(self, val):
        self.arr.append(val)

def merge_sort(arr):
    
    if len(arr) < 2:
        return arr

    split = len(arr)//2
    arr1 = arr[:split]
    arr2 = arr[split:]
    
    arr1 = merge_sort(arr1)
    arr2 = merge_sort(arr2)

    ordarr = []

    while len(arr1) != 0 and len(arr2) != 0:
        if arr1[0] < arr2[0]:
            ordarr.append(arr1.pop(0))
        else:
            ordarr.append(arr2.pop(0))

    if len(arr1) == 0:
        ordarr.extend(arr2)

    else:
        ordarr.extend(arr1)

    return ordarr 


if __name__ == '__main__':
    arr = [1,3,2,6,3,10,1,1,0,90,-1,0]
    arr2 = [10,50,80,0,100,25,75,60]
    arr3 = [10,10,10,0]
    arr4 = [0,10,10,10]
    arr5 = [0]
    arr6 = [0, 0]
    arr7 = [0,7,0]

    assert merge_sort(arr) == [-1, 0, 0, 1, 1, 1, 2, 3, 3, 6, 10, 90]
    assert merge_sort(arr2) == [0, 10, 25, 50, 60, 75, 80, 100]
    assert merge_sort(arr3) == [0, 10, 10, 10]
    assert merge_sort(arr4) == [0, 10, 10, 10]
    assert merge_sort(arr5) == [0] 
    assert merge_sort(arr6) == [0,0] 
    assert merge_sort(arr7) == [0,0,7] 

    # print(merge_sort(arr))
    # print(merge_sort(arr2))
    # print(merge_sort(arr3))
    # print(merge_sort(arr4))
    # print(merge_sort(arr5))
    # print(merge_sort(arr6))
    # print(merge_sort(arr7))
