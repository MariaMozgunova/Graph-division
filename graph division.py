"""
Divide the graph`s vertexes into two non-empty
sets so that the minimum weight edge connecting the
vertexes from the same set has the maximum weight.

input:
first line - number of vertexes, number of edges(n)
following n lines: two vertexes, and the weight of edge between them

Output:
max edge weight, which is the least in the set 
"""

def the_biggest():
    maybe_the_biggest = graph
    max_vertex = 0
    vert = 0
    for maybe in maybe_the_biggest:
        if maybe[0] > max_vertex:
            max_vertex = maybe[0]
            vert = maybe
    for gr in graph:
        if [vert[2], vert[1]] != gr[1:] and vert[1:] != gr[1:]:
            return max_vertex
    del maybe_the_biggest[maybe_the_biggest.index(vert)]

graph = []
vertexes, edges = map(int, input().split())

for _ in range(edges):
    ver1, ver2, edge = map(int, input().split())
    graph.append((edge, ver1, ver2))

print(the_biggest())   

    
    
