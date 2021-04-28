#time - O(n)
#space - O(n)
''' need to confirm those values are right
'''

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder(root):
    res = []
    if not root:
        return res
    stack = []
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        res.append(root.val)
        root = root.right
    return res

def inorder_rec(root, arr=None):
    if root == None:
        return "whatever i want, doesnt matter"
    if arr == None:
        arr = []
    inorder_rec(root.left, arr)
    arr.append(root.val)
    inorder_rec(root.right, arr)
    return arr

def binary_tree_paths(root):
    res = []
    if root is None:
        return res
    dfs(res, root, str(root.val))
    return res


def dfs(res, root, cur):
    if root.left is None and root.right is None:
        res.append(cur)
    if root.left:
        dfs(res, root.left, cur+'->'+str(root.left.val))
    if root.right:
        dfs(res, root.right, cur+'->'+str(root.right.val))

if __name__ == '__main__':
    n1 = Node(100)
    n2 = Node(50)
    n3 = Node(150)
    n4 = Node(25)
    n5 = Node(75)
    n6 = Node(125)
    n7 = Node(175)
    n1.left, n1.right = n2, n3
    n2.left, n2.right = n4, n5
    n3.left, n3.right = n6, n7
    

    # print(inorder_rec(n1))
    # inorder_rec(n1)
    # n1
    # assert inorder(n1)     == [25, 50, 75, 100, 125, 150, 175]
    # assert inorder_rec(n1) == [25, 50, 75, 100, 125, 150, 175]
    
    # print(inorder(n1))
    print(binary_tree_paths(n1))