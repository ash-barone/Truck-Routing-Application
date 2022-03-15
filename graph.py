import json
import pprint


class Graph:
    def __init__(self):
        self.adjacency_list = {}
        self.edge_weights = {}

    def add_point(self, new_point):
        """ Adds an address as a vertex
        :param new_point: address
        :return: if address is already in the list, return
        """
        if new_point in self.adjacency_list:
            return
        else:
            self.adjacency_list[new_point] = []

    def add_directed_edge(self, from_vertex, to_vertex, weight=1.0):
        self.edge_weights[(from_vertex, to_vertex)] = weight
        self.adjacency_list[from_vertex].append(to_vertex)

    def add_undirected_edge(self, vertex_a, vertex_b, weight=1.0):
        self.add_directed_edge(vertex_a, vertex_b, weight)
        # self.add_directed_edge(vertex_b, vertex_a, weight)

    def search(self, curr_vertex, next_vertex):
        dict = self.edge_weights.items()
        # print(dict)
        # pprint.pprint(dict)
        # print("vertexes " + str(curr_vertex) + " , " + str(next_vertex))
        temp_v = 0
        for k, v in dict:
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
    # return [v for k, v in self.edge_weights.items() if k[0] == curr_vertex and k[1] == next_vertex]


class Vertex:
    def __init__(self, label):
        self.label = label
        self.distance = float('inf')
        self.last_vertex = None
