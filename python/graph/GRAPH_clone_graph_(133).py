"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

'''
Edge cases
1. no nodes
2. one node
3. one node connect to self
4. two nodes no connectiono
5. two nodes connected simply
6. two nodes connected more than once
7. duplicate links?
8. empty nodes?
9. same value? not possible?
'''

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # visited = []
        # ognodes = []
        # newgraph = []
        # ognodes.append(node)
        # while og_visited:
        #     new_node = ognodes.pop(0)
        #     # check if new_node has already been visited
        #     # create node object for value
        #     # create node object for each neighbour?
        #     # or do we check if neighbours have already been added?
        #     # do we add in all the ndes first and then add in all the edges?
        print(findAllNodes(node))

        
        
def findAllNodes(node: 'Node') -> '[]':
    to_visit = []
    nodes = {}
    to_visit.append(node)
    
    while to_visit:
        new_node = to_visit.pop(0)
        if node.value not in to_visit:
        for neighbor in new_node.neighbors:
            if (neighbor.val not in visited):
                to_visit.append(neighbor.val)
    
    return visited
    
        
def equals(node1: 'Node', node2: 'Node') -> bool:
    for neigh1,neigh2 in zip(node1.neighbors,node2.neighbors):
        if neigh1.val != neigh2.val:
            return false
    return node1.val == node2.val
