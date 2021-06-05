# rec and non rec?
# quick_sort splits array into two halves of less than and greater than some pivot point
# 
"""
Time Complexity: O()
"""

from icecream import ic

def quick_sort(arr):

    if len(arr)<2:
        return arr

    pivot = len(arr) - 1
    index = pivot - 1

    while pivot > 0 and index > -1:
        if arr[index] > arr[pivot]:
            arr.append(arr.pop(index))
            pivot -= 1
            index -= 1
        else:
            index -= 1

    low = arr[:pivot]
    hi = arr[pivot:]

    ordlow = quick_sort(low)
    ordhi = quick_sort(hi)

    arr.clear()
    arr.extend(ordlow)
    arr.extend(ordhi)
    # ordarr = arr

    return arr

if __name__ == '__main__':
    arr = [1,3,2,6,3,10,1,1,0,90,-1,0]
    arr2 = [10,50,80,0,100,25,75,60]
    arr3 = [10,10,10,0]
    arr4 = [0,10,10,10]
    arr5 = [0]
    arr6 = [0, 0]
    arr7 = [0,7,0]
    arr8 = [0,10]

    
    assert quick_sort(arr) == [-1, 0, 0, 1, 1, 1, 2, 3, 3, 6, 10, 90]
    assert quick_sort(arr2) == [0, 10, 25, 50, 60, 75, 80, 100]
    assert quick_sort(arr3) == [0, 10, 10, 10]
    assert quick_sort(arr4) == [0, 10, 10, 10]
    assert quick_sort(arr5) == [0] 
    assert quick_sort(arr6) == [0,0] 
    assert quick_sort(arr7) == [0,0,7] 

    ic(quick_sort(arr2))
    print(quick_sort(arr))
    print(quick_sort(arr2))
    print(quick_sort(arr3))
    print(quick_sort(arr4))
    print(quick_sort(arr5))
    print(quick_sort(arr6))
    print(quick_sort(arr7))