import Files as f

class City:

    def __init__(self, name):
        self.name = name
        self.edges = []



class Graph:

    def __init__(self):
        self.cities = []

    def add_city(self, v):
        self.cities.append(v)

    def set_edge(self, c1, c2):

        if c1 not in c2.edges:
            c2.edges.append(c1)

        if c2 not in c1.edges:
            c1.edges.append(c2)

    def get_city_vertex(self, city_name):

        res = None
        for i in self.cities:
            if i.name == city_name:
                res = i
        return res

    def get_edges(self, city):

        index = self.cities.index(city)
        res = self.cities[index].edges
        return res

    def print_cities(self):

        for i in self.cities:
            print(i.value, end=" ")

    def contain_city(self, city_name):

        res = False
        for i in self.cities:
            if i.name == city_name:
                res = True
        return res

    def print_edges(self, city):

        edges = self.get_edges(city)
        for i in edges:
            print(i.name,end=" ")

    def traverse_DFS_1(self, city_name, visited):

        if self.contain_city(city_name):
            v = self.get_city_vertex(city_name)
            if v not in visited:
                visited.append(v)

            for i in v.edges:
                if i not in visited:
                    visited.append(i)
                    self.traverse_DFS_1(i.value, visited)
        else:
            print("There is not vertex in the graph")
        return visited

    def traverse_BFS(self, city_name):

        if self.contain_city(city_name):

            start_vertex = self.get_city_vertex(city_name)
            queue = []
            queue.append(start_vertex)
            visited = []

            while queue:
                vertex = queue.pop(0)
                if vertex not in visited:
                    print(vertex.name, end=" ")
                    visited.append(vertex)
                    edges = self.get_edges(vertex)
                    for e in edges:
                        queue.append(e)
        else:
            print("There is no vertex in the graph")


    def create_city_graph(self):

        cities = f.read_header()
        # print(cities)

        dataset = f.read_data_csv()
        # print(dataset)

        # Creating all city objects
        for city in cities:
            c = City(city)
            self.add_city(c)

        for i in range(1,len(cities)):
            city1 = cities[i]

            for j in range(1,len(cities)):

                if (i != j):
                    city2 = cities[j]
                    connect = int(dataset[i][j])
                    # print(city1,city2,connect)

                    if (connect == 1):
                        c1 = self.get_city_vertex(city1) # must get the object that has been created in the graph
                        c2 = self.get_city_vertex(city2)
                        self.set_edge(c1,c2)




