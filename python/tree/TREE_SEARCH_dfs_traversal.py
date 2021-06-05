#time - O(n)
#space - O(n)
# Alternatives - BFS, mixed bfs/dfs, monte carlo search
    # consider application moreso than runtime for these searches

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if data < self.data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = Node(data)
        elif self.data < data:
            if self.right:
                self.right.insert(data)
            else:
                self.right = Node(data)

### ---------------------------------------------Notes------------------------------------------------------------   
'''
node can only have 4 states
    son and daughter, son, daughter, single (bachelor)
by defining how the four states are handled in the rec relation below provides 
better understanding of how to make sure no unintended behaviour occurs

another is to look at the operations performed by the rec fn's
'''
## ---------------------------------------------break------------------------------------------------------------


'''All fn's below are recurive, take in a node and return an array'''
def preord_trav(node):
    arr = []
    if node:
        arr.append(node.data)
        arr.extend(preord_trav(node.left))
        arr.extend(preord_trav(node.right))
    return arr

def inord_trav(node):
    arr = []
    if node:
        arr.extend(inord_trav(node.left))
        arr.append(node.data)
        arr.extend(inord_trav(node.right))
    return arr

def postord_trav(node):
    arr = []
    if node:
        arr = postord_trav(node.left)
        arr.extend(postord_trav(node.right))
        arr.append(node.data)
    return arr

def revinord_trav(node):
    arr = []
    if node:
        arr = revinord_trav(node.right)
        arr.append(node.data)
        arr.extend(revinord_trav(node.left))
    return arr


'''All fn's below are iterative
Input: root: Node
Output: array: [int] - of all values in tree starting at root'''
def inorderTraversalIterative(root): # def inorderTraversal(root: Node) -> List[int]:
    stack, res = [], []
    # premise, 
        # 1. if stack is empty nothing to process upwards
        # 2. if node is empty nothing to process downwards   
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        if not stack:
            return res
        root = stack.pop()
        res.append(root.data)
        root = root.right
    return res


'''All fn's below are functional based
functional dfs
https://stackoverflow.com/questions/30464163/functional-breadth-first-search
https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.49.9852&rep=rep1&type=pdf
'''
# to do

'''All fn's below are used for printing'''
def binary_tree_paths(root):
    res = []
    if root is None:
        return res
    dfs(res, root, str(root.data))
    return res


#this prints the path from root to each leaf node 
def dfs(res, root, cur):
    if root.left is None and root.right is None: #if leaf node
        res.append(cur)
    if root.left:
        dfs(res, root.left, cur+'->'+str(root.left.data))
    if root.right:
        dfs(res, root.right, cur+'->'+str(root.right.data))


if __name__ == "__main__":
    # Setup
    root = Node(27)
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


    print(preord_trav(root))
    print(inord_trav(root))
    print(postord_trav(root))
    print(revinord_trav(root))
    print(binary_tree_paths(root))

    assert inord_trav(root) == [10, 14, 19, 27, 31, 35, 42]
    assert inorderTraversalIterative(root) == [10, 14, 19, 27, 31, 35, 42]