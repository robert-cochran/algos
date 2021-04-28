

class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if data < self.data:
            if self.left == None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right == None:
                self.right = Node(data)
            else: 
                self.right.insert(data) 


    def inorder_traversal_value(self, node, value, res):
        if node:
            node.inorder_traversal_value(node.left, value, res)
            if node.data > value:
                return [value, node.data]#  res.append(node.data)
            node.inorder_traversal_value(node.right, value, res)
        return res

    def inorder_traversal(self, node):
        if node:
            node.inorder_traversal(node.left)
            print(node.data)
            node.inorder_traversal(node.right)


root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
res = root.inorder_traversal_value(root, 19, [])
print(res)

# tree = Tree(Node(20))
# tree.insert(10, tree.root)
# tree.insert(30, tree.root)
# tree.insert(40, tree.root)
# tree.inorder_traversal(tree.root)



    # def traversal()
    

# class Node:

#     def __init__(self, data):

#         self.left = None
#         self.right = None
#         self.data = data
# # Insert Node
#     def insert(self, data):

#         if self.data:
#             if data < self.data:
#                 if self.left is None:
#                     self.left = Node(data)
#                 else:
#                     self.left.insert(data)
#             elif data > self.data:
#                 if self.right is None:
#                     self.right = Node(data)
#                 else:
#                     self.right.insert(data)
#         else:
#             self.data = data

# # Print the Tree
#     def PrintTree(self, value):
#         if self.left:
#             self.left.PrintTree()
#         print( self.data),
#         if self.right:
#             self.right.PrintTree()

# # Preorder traversal
# # Root -> Left ->Right
#     def PreorderTraversal(self, root):
#         res = []
#         if root:
#             res.append(root.data)
#             res = res + self.PreorderTraversal(root.left)
#             res = res + self.PreorderTraversal(root.right)
#         return res

# root = Node(27)
# root.insert(14)
# root.insert(35)
# root.insert(10)
# root.insert(19)
# root.insert(31)
# root.insert(42)
# root.inorder_traversal(root, 19, False)
# root.PrintTree()