"""
dijkstras
"""
from icecream import ic

class Node():
    def __init__(self, name, dist=None, prev=None, neighbours=[]):
        self.name = name
        self.dist = dist
        self.prev = prev
        self.neighbours = neighbours

class Graph():
    def __init__(self):
        self.nodes = []
        self.edges = []
        self.adjList = {}
        # implement adjacency matrix? adjacency list?
        # what about other matrix types, e.g. laplacian matrix, self-similarity matrix

    def addNode(self, name):
        node_exists = False
        for node in self.nodes:
            if node.name == name:
                node_exists = True
        if node_exists:
            return False
        else:
            self.adjList[name] = []
            return self.nodes.append(Node(name))

    def addEdge(self, node1_name, node2_name, cost):
        newEdge = (node1_name, node2_name, cost)
        if self.edges.count(newEdge) == 0:
            self.addNode(node1_name)
            self.addNode(node2_name)
            self.adjList[node1_name].append((node2_name, cost))
            self.adjList[node2_name].append((node1_name, cost))
            return self.edges.append(newEdge)
        return False

    def getNode(self, name):
        for node in self.nodes:
            if node.name == name:
                return node
        return None

    def getNeighbours(self, node):
        for edge in graph.edges:
            if edge[0] == name:
                neighbours.append(edge[1])
            if edge.v == name:
                neighbours.append(edge.u)
        neighbours = list(set(neighbours))

def dijk(graph, root):
    
    unchecked_nodes = []

    for node in graph.nodes:
        node.dist = float('inf')
        node.prev = None
        neighbours = []
        if node.name == root:
            node.dist = 0
            node.prev = root
        unchecked_nodes.append(node)

    while any(unchecked_nodes):
        unchecked_nodes = sorted(unchecked_nodes, key =lambda node: node.dist)
        u = unchecked_nodes.pop(0)
        for edge in graph.adjList[u.name]:    
            v = graph.getNode(edge[0])
            cost = edge[1]
            if (u.dist > (v.dist + cost)):
                if unchecked_nodes.count(v) == 0:
                    u.dist = v.dist + cost
                    u.prev = v
    
    return graph

def print_path(node, root):
    # prev_node = node
    # # ic("end",node.name)
    # while prev_node.name != root:
    #     ic(prev_node.name)
    #     prev_node = g.getNode(prev_node.prev)
    #     ic(node.name, node.prev.name)
    # ic("start",root)
    pass

if __name__ == "__main__":

    g = Graph()

    # a0, b1, c2, d3, e4, f5, g6, h7, i8
    # https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/ for dijkstras graph used
    
    g.addEdge('A', 'B', 4)
    g.addEdge('A', 'H', 8)
    g.addEdge('B', 'H', 11)
    g.addEdge('H', 'I', 7)
    g.addEdge('H', 'G', 1)
    g.addEdge('B', 'C', 8)
    g.addEdge('C', 'D', 7)
    g.addEdge('C', 'F', 4)
    g.addEdge('D', 'F', 14)
    g.addEdge('D', 'E', 9)
    g.addEdge('E', 'F', 10)
    g.addEdge('F', 'G', 2)
    g.addEdge('C', 'I', 2)
    g.addEdge('G', 'I', 6)

    root = 'A'
    g = dijk(g, root)
    shortest_paths_from_root_0 = [0,4,12,19,21,11,9,8,15]
    shortest_generated = []

    for node in sorted(g.nodes, key = lambda node: node.name):
        shortest_generated.append(node.dist)

    assert shortest_paths_from_root_0 == shortest_generated
