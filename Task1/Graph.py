
class Vertex:

    def __init__(self, value):
        self.value = value
        self.edges = []


class Graph:

    def __init__(self):
        self.vertices = []

    def add_vertex(self, v):
        self.vertices.append(v)

    def set_edge(self, v1, v2):

        if v1 not in v2.edges:
            v2.edges.append(v1)

        if v2 not in v1.edges:
            v1.edges.append(v2)

    def get_vertex(self, value):

        res = None
        for i in self.vertices:
            if i.value == value:
                res = i
        return res


    def get_edges(self, vertex):

        index = self.vertices.index(vertex)
        res = self.vertices[index].edges
        return res

    def print_edges(self, vertex):

        edges = self.get_edges(vertex)
        for i in edges:
            print(i.value,end=" ")


    def print_vertices(self):

        for i in self.vertices:
            print(i.value, end=" ")


    def contain_vertex(self, value):

        res = False
        for i in self.vertices:
            if i.value == value:
                res = True
        return res


    def traverse_DFS_1(self, value, visited):
        # Write your code here
        pass


    def traverse_DFS_2(self):
        # Write your code here
        pass

    def traverse_BFS(self, value):
        # Write your code here
        pass



    def create_graph(self):

        # Creating vertices using a for loop: 10,20,...60
        for i in range(1,7):
            value = 10*i
            v = Vertex(value)
            self.add_vertex(v)

        # [10,20,30,40,50,60]

        # Edges for 10: 20 and 50
        self.set_edge(self.vertices[0],self.vertices[1])
        self.set_edge(self.vertices[0], self.vertices[4])

        # Edges for 20: 10, 30 and 60
        self.set_edge(self.vertices[1], self.vertices[0])
        self.set_edge(self.vertices[1], self.vertices[2])
        self.set_edge(self.vertices[1], self.vertices[5])

        # Edges for 30: 20, 40 and 50
        self.set_edge(self.vertices[2], self.vertices[1])
        self.set_edge(self.vertices[2], self.vertices[3])
        self.set_edge(self.vertices[2], self.vertices[4])

        # Edges for 40: 30
        self.set_edge(self.vertices[3], self.vertices[2])

        # Edges for 50: 10 and 30
        self.set_edge(self.vertices[4], self.vertices[0])
        self.set_edge(self.vertices[4], self.vertices[2])

        # Edges for 60: 20
        self.set_edge(self.vertices[5], self.vertices[1])


def print_vertices(graph):
    for i in graph:
        print(i.value, end=" ")




# ©Zairul Mazwan©