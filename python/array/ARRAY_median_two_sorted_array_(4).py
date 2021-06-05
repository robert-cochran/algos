'''
Edge cases:
nothing in one
nothing in both
type check
all same values
negative values

'''


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = merge(nums1, nums2)
        med = median(merged)
        
        return med

def merge():
    max_len = (len(nums1) + len(nums2)) //2


    
def merge_naive(nums1: List[int], nums2: List[int]):
    nums3 = []
    while nums1 and nums2:
        if nums1[0] < nums2[0]:
            nums3.append(nums1.pop(0))
        else:
            nums3.append(nums2.pop(0))

    if nums1:
        nums3.extend(nums1)
    if nums2:
        nums3.extend(nums2)

    return(nums3)

# median is the middle value of an array, for even array its the average of the
# two central values
def median(arr: List[int]) -> float:
    
    if (len(arr) % 2) == 1:
        median = arr[int(len(arr)/2)]
    else:
        bottom = arr[int(len(arr)/2)-1]
        top = arr[int(len(arr)/2)]
        median = ((top+bottom)/2)
        
    return median
    # return merged
