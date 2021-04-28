"""
b-tree

rules:
1. Every node has at most m children.
2. Every non-leaf node (except root) has at least ⌈m/2⌉ child nodes.
3. The root has at least two children if it is not a leaf node.
4. A non-leaf node with k children contains k − 1 keys.
5. All leaves appear in the same level and carry no information.
"""

class Node():
    def __init__(self, values, parent=None. children=[]):
        self.values = values
        self.parent = parent
        self.children = children


class BTree():
    def __init__(self, value, order=5):
        self.root = Node(value)
        self.order = order

    def add(self, value):
        pass

    def remove(self, value):
        pass

    def find(self, key):
        return find_node(self.root, key)
    
    def find_node(self, root_node, key):
        # key, value = list(d.items())[0]
        root_keys, root_values = list(self.root.values.items())
        for i in range(len(root_keys)):
            if key < root_keys[i]:
                return find_node(root_node.children[i], key)              
                    #need to check the child at first position
            # need case for key == root_key
            # need case for key not being in a node and no children left to check
            return self.root.values[key]
        #if not there we must find the child sitting between the two nodes we want
        # for i in values while i < limit
        # if value < root.values[i], try next
        # if value > root.values[i] then look at the child node

        # algo
            # if value < key1, look at child 1
            # if value < key2, look at child 2
            # ...
            # else look at child 3



def balance(node):
    pass

if __name__ == "__main__":
    b = BTree({0:"zer0"})
    b.add({1:"on1"})
    assert b.find(1) == "on1"
    b.add({2:"2wo"})
    assert b.find(2) == "2wo"
