from Task1.Graph import Graph
from Task1 import Graph as g

my_graph = Graph()
my_graph.create_graph()
print("Dataset: ")
my_graph.print_vertices()
print()

print("Edges for 30: ")
my_graph.print_edges(my_graph.get_vertex(30))
print()

print("Breath First Search Algo Result: ")
my_graph.traverse_BFS(60)
print()

visited = []
dfs = my_graph.traverse_DFS_1(60, visited)
print("Depth First Search Algo 1 Result: ")
g.print_vertices(dfs)


# ©Zairul Mazwan©