from City import Graph


my_graph = Graph()
my_graph.create_city_graph()

print("Is Kuala Lumpur in the graph? ",my_graph.contain_city("Kuala Lumpur"))
print("Is London in the graph? ", my_graph.contain_city("London"))

print("Where can I travel from Kuala Lumpur? ")
my_graph.print_edges(my_graph.get_city_vertex("Kuala Lumpur"))

# my_graph.traverse_BFS("London")





# ©Zairul Mazwan©
