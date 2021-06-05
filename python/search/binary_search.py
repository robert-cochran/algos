class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left, right = 0, len(nums)-1
        # pivot = right//2
        while left <= right:
            pivot = left + ((right - left) //2)
            if nums[pivot] == target:
                return pivot
            if target < nums[pivot]:
                right = pivot-1
                # move right down
            else:
                left = pivot+1
                # move left up
        return -1

# given an array of intts and a target, this uses binary search to find target in log n time
# if target not present, -1 is returned