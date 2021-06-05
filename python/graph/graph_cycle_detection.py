from enum import Enum

class TraversalState(Enum):
    UNSEEN = 0
    SEEN = 1
    CLEARED = 2

class Graph():
    def __init__(self):
        self.adjlst = {}

    def addEdge(self, node_1, node_2):
        if self.adjlst.get(node_1) == None:
            self.adjlst[node_1] = []
        if self.adjlst.get(node_2) == None:
            self.adjlst[node_2] = []
        if self.adjlst[node_1].count(node_2) == 0:
            self.adjlst[node_1].append(node_2)
        
    def isCycle(self, node, traversalStates):
        if traversalStates[node] == TraversalState.SEEN:
            return True
        traversalStates[node] = TraversalState.SEEN
        for neighbour in self.adjlst[node]:
            if self.isCycle(neighbour, traversalStates):
                return True
        traversalStates[node] = TraversalState.CLEARED
        return False

    def cycleDetection(self):
        traversalStates = {}
        for node in self.adjlst.keys():
            traversalStates[node] = TraversalState.UNSEEN
        for node, state in traversalStates.items():
            if state == TraversalState.UNSEEN and self.isCycle(node, traversalStates):
                return True
        return False


class UndirectedGraph():
    def __init__(self):
        pass
    # should i pass in undirectedGraph here to borrow from its methods?
    # or pass directed into undirected since theres more info in an undirexcted? 
        # but that implies preserving info and not starting from scratch





if __name__ == "__main__":
    graph = Graph()
    graph.addEdge('A', 'B')
    graph.addEdge('B', 'C')
    graph.addEdge('A', 'E')
    for key, item in graph.adjlst.items():
        print(key, item)

    print(graph.cycleDetection())

    #cycle added
    graph.addEdge('C', 'A')
    print(graph.cycleDetection())
