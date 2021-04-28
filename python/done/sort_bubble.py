def bubble(arr, simulation=False):
    def swap(i, j):
        i, j = j, i
        return i, j    
    
    iteration = 0
    if simulation:
        print("iteration",iteration,":",*arr)
    for already_bubbled in range(1, len(arr)):
        for i in range(0, len(arr)-already_bubbled):
            if (arr[i] < arr[i+1]):
                pass
            else:
                arr[i], arr[i+1] = arr[i+1], arr[i]
            if simulation:
                iteration = iteration + 1
                print("iteration",iteration,":",*arr)
    return arr

def bubble_sort(arr, simulation=False):
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    n = len(arr)
    swapped = True
    
    iteration = 0
    if simulation:
        print("iteration",iteration,":",*arr)
    x = -1
    while swapped:
        swapped = False
        x = x + 1
        for i in range(1, n-x):
            if arr[i - 1] > arr[i]:
                swap(i - 1, i)
                swapped = True
                if simulation:
                    iteration = iteration + 1
                    print("iteration",iteration,":",*arr)
                    
    return arr

if __name__ == '__main__':
    arr = [1,3,2,6,3,10,1,1,0,90,-1,0]
    arr2 = [1,3,2,6,3,10,1,1,0,90,-1,0]
    a = bubble(arr)
    print(a)
    # a2 = bubble_sort(arr2, True)
    # print(a2)