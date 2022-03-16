import json
import pprint


class Graph:
    def __init__(self):
        self.adjacency_list = {}
        self.edge_weights = {}

    def add_point(self, new_point):
        """
        Adds each address from distances.csv as a vertex in the graph
        :param new_point: The address being added
        :return If the address has already been added:
        """
        if new_point in self.adjacency_list:
            return
        else:
            self.adjacency_list[new_point] = []

    def add_directed_edge(self, from_vertex, to_vertex, weight=1.0):
        """
        Adds a directed edge from one vertex(address) to another
        :param from_vertex: The starting address
        :param to_vertex: The ending address
        :param weight: The distance from the start to the end address
        """
        self.edge_weights[(from_vertex, to_vertex)] = weight
        self.adjacency_list[from_vertex].append(to_vertex)

    def add_undirected_edge(self, vertex_a, vertex_b, weight=1.0):
        """
        Adds an undirected edge between two vertices(address)
        :param vertex_a: Address a
        :param vertex_b: Address b
        :param weight: The distance between the addresses
        """
        self.add_directed_edge(vertex_a, vertex_b, weight)
        # self.add_directed_edge(vertex_b, vertex_a, weight)

    def search(self, curr_vertex, next_vertex):
        """
        Searches the graph using the two vertices(addresses) as the key in order to access the distance value
        :param curr_vertex: Starting address
        :param next_vertex: Ending address
        :return: The distance from start to end address
        """
        graph = self.edge_weights.items()
        # print(dict)
        # pprint.pprint(dict)
        # print("vertexes " + str(curr_vertex) + " , " + str(next_vertex))
        temp_v = 0
        # search through the keys and values in the graph
        for k, v in graph:
            # print("k[0]"+ str(k[0])+ " curr vertex "+ str(curr_vertex))
            if k[0] == curr_vertex:
                # print("something happened "+ str(k[0]))
                if k[1] == next_vertex:
                    temp_v = v
                    # print("something really good happened "+ str(v))
            elif k[0] == next_vertex:
                # print("something happened reverse "+ str(k[0]))
                if k[1] == curr_vertex:
                    temp_v = v
                    # print("something really good reverse " + str(v))
        return temp_v