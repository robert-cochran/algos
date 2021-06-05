'''
recursviely swap any adjacent elemets in a given array
e.g. [1,2,3,4,5,6] -> [2,1,4,3,6,5]
'''

def swap(arr):
    if len(arr) < 2:
        return arr
    
    print(arr)
    arr[0], arr[1] = arr[1], arr[0]    

    if len(arr) == 2:
        return arr

    else:
        end = (swap(arr[2:]))
        beg = arr[:2]
        beg.extend(end)
        return beg

arr = [1,2,3,4,5]
print(arr[:2])
print(swap(arr))