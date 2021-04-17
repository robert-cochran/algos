from icecream import ic

def dfs(start, end):
    # root must contain a way to access children
    return 0

def bfs():
    return 0

def dijk():
    return 0

class Graph():
    def __init__(self, g):
        self.graph = g
        self.edges = []

    def verticies(self, g):
        return self.graph.keys


    def print_path(self, start, end, path, queue, checked): 
        graph = self.graph
        # print(path, queue, checked)
        while len(queue)>0:
            ic(path, queue, checked)
            current_node = queue.pop(0)
            if end in graph[current_node]:
                path.append(current_node)
                path.append(end)
                return path
            checked.append(current_node)
            for neighbour in graph[current_node]:
                ic(graph[current_node])
                ic(neighbour)
                if checked.count(neighbour)==0: #check if node hasnt been checked already
                    npath = path.copy()
                    npath.append(neighbour)
                    ic(npath)
                    nqueue = queue.copy()
                    nqueue.append(neighbour)
                    nchecked = checked.copy()
                    nchecked.append(neighbour)
                    # print(npath)
                    self.print_path(neighbour, end, npath, nqueue, nchecked) 
        return []




    def bfs(self, start, end): 
        queue = [start]
        checked = []
        while len(queue)>0:
            current_node = queue.pop(0)
            if end in self.graph[current_node]:
                return True
            checked.append(current_node)
            for node in self.graph[current_node]:
                if checked.count(node)==0:
                    queue.append(node) 
        return False




if __name__ == "__main__":
    g_ex = { "a" : ["d"],
        "b" : ["c"],
        "c" : ["b", "c", "d", "e"],
        "d" : ["a", "c"],
        "e" : ["c"],
        "f" : []
    }

    graph = Graph(g_ex)
    
    #print(dir(graph))
    
    
    start_node = 'a'
    end_node = 'e'
    path = [start_node]
    queue = [start_node]
    
    print(graph.bfs(start_node, end_node))

    print("PRINT PATH NOT WORKING")

    print(graph.print_path(start_node, end_node, [start_node], [start_node], []))
