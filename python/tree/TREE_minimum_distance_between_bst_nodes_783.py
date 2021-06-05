from icecream import ic
'''
Notes

start on root val
no negatives
have at least two nodes
we also know we can traverse bakc and forth to find values with bst



--------------------------------------------------------------------
Quesitons
should we find the total node count?
width?
height?

can we think about this like it was an array?
    assuming we had an array, how would we solve this
        since its soerted, we know that the end and start will be good starting points as parent of right most will definitely be not chaning, 
        same with leftmmost
        see strategy 1
        
will recording any edges count towards a wrong answer?
can i store the edges as differences? 
and then sort the edges?
'''

'''
Strategy 1
inorder traversal down until stop
take difference between leftmost leaf and parent
set as current min
if none
go right
'''

'''
ENSURE
Move down left

def minDiffInBST(self, root: TreeNode) -> int:
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def insert(self, val):
        if val < self.val:
            if self.left:
                self.left.insert(val)
            else:
                self.left = TreeNode(val)
        elif self.val < val:
            if self.right:
                self.right.insert(val)
            else:
                self.right = TreeNode(val)
        





'''
solution 2 uses inorder traversal and recursion to save values to array
array is then used to find minimal difference between elements
recurrance relation ?
guarantee or aim of fn?
    array of sorted values of left subtree
    array of sorted values of right subtree
'''
def solution2(root: TreeNode) -> [int]:

    #input: take in a node with children in bst
    #output: array of tree in asc. order
    def inorder(root: TreeNode) -> [int]:
        arr = []
        if root:
            arr = inorder(root.left) # collect left
            arr.append(root.val) # join left  
            arr.extend(inorder(root.right)) #collect right, join right
        return arr
    
    # take in an asc. sorted array and return min diff between elements
    def findMin(arr: [int]) -> int:
        minDiff = arr[1] - arr[0]
        for i in range(1,len(arr)):
            diff = arr[i] - arr[i-1]
            if diff < minDiff:
                minDiff = diff
        return minDiff
    
    arr = inorder(root)
    minDiff = findMin(arr)
    return minDiff


'''
solution 1 uses postOrder without recursion
didnt finish
'''
# def solution1(root: TreeNode) -> int:
#     stack, minDiff = [], 0
#     prevVal = 0
#     #use post order instead to ensure the leaf nodes are visited first, then the parents of those, etc...
#     while root or stack:
#         # traverse to bottom left of tree and record parents value
#         while root:
#             stack.append(root)
#             if root.left: # we only want to save prevVal for nodes that have a children
#                 parentVal = root.val
#             root = root.left
#         # if no more elements to explore upwards, then return
#         if not stack:
#             return minDiff
#         root = stack.pop()
#         while root:
#             stack.append(root)
#             root = root.right

#         leftDiff = parentVal - root.val
#         if left < minDiff:
#             minDiff = leftDiff

#         if root.right:
#             rightDiff = root.right
#     return None





if __name__ == "__main__":
    root = TreeNode(27)
    root.insert(14)
    root.insert(35)
    root.insert(10)
    root.insert(19)
    root.insert(31)
    root.insert(42)

    '''
          27
        /    \
      14      35
      /\      /\
    10  19  31  42
    '''

    print(solution2(root))