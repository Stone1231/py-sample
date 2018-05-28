import collections

class graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict = []
        self.gdict = gdict

    # Get the keys of the dictionary
    def getVertices(self):
        return list(self.gdict.keys())

    # Add the vertex as a key
    def addVertex(self, vrtx):
       if vrtx not in self.gdict:
            self.gdict[vrtx] = []

    def edges(self):
        return self.findedges()
    # Find the distinct list of edges
    def findedges(self):
        edgename = []
        for vrtx in self.gdict:
            for nxtvrtx in self.gdict[vrtx]:
                if {nxtvrtx, vrtx} not in edgename:
                    edgename.append({vrtx, nxtvrtx})
        return edgename        

    # Add the new edge
    def addEdge(self, edge):
        edge = set(edge)
        (vrtx1, vrtx2) = tuple(edge)
        if vrtx1 in self.gdict:
            self.gdict[vrtx1].append(vrtx2)
        else:
            self.gdict[vrtx1] = [vrtx2]

# Create the dictionary with graph elements
graph_elements = { "a" : ["b","c"],
                "b" : ["a", "d"],
                "c" : ["a", "d"],
                "d" : ["e"],
                "e" : ["d"]
                }

g = graph(graph_elements)

print(g.getVertices())
print(g.edges())

g.addVertex("f")
print(g.getVertices())

g.addEdge({'a','e'})
g.addEdge({'a','c'})
print(g.edges())

# Depth First Traversal
def dfs(graph, start, visited = None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited

# Breadth First Traversal
def bfs(graph, startnode):
    # Track the visited and unvisited nodes using queue
    seen, queue = set([startnode]), collections.deque([startnode])
    while queue:
        vertex = queue.popleft()
        print(vertex)
        for node in graph[vertex]:
            if node not in seen:
                seen.add(node)
                queue.append(node)

gdict = {
    "a" : set(["b","c"]),
    "b" : set(["a", "d"]),
    "c" : set(["a", "d"]),
    "d" : set(["e"]),
    "e" : set(["a"])
    }    
dfs(gdict, 'a')
print()
bfs(gdict, "a")
