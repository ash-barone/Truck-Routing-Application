import csv
import sys

import util
from graph import Graph

distance_graph = Graph()


def load_address_data(file_name, graph):
    with open(file_name) as distances:
        distance_data = csv.reader(distances, delimiter=',')
        address_line = next(distance_data)
        # print("address line: " + str(address_line))
        other_graph = graph

        for row in distance_data:
            start_address = row[0]
            # print("start address: " + start_address)
            distance_graph.add_point(start_address)

            for col in range(len(row))[1:]:
                end_address = address_line[col]
                # print("End address: " + end_address)
                distance_graph.add_point(end_address)
                if row[col] != "":
                    #  print(float(row[col]))
                    distance_graph.add_directed_edge(start_address, end_address, float(row[col]))
                # elif row[col] == "":
                #  print("distance blank")


def create_address_graph():
    # my_graph = Graph()
    util.load_address_data("distances.csv", distance_graph)


def find_shortest_distance(start, package_list):
    # print(" pls do something")
    starting_location = "4001 South 700 East"
    '''print("Starting Location BEGIN: ")
    print(starting_location)'''
    optimized_list = []
    distance_list = []
    total_distance = 0
    current_location = start
    next_delivery = None

    # Time-complexity of O(n^2)
    # Space-complexity of O(n)
    for i in range(len(package_list)):
        min_distance = 5000
        for j in range(len(package_list))[i:]:
            package = package_list[j]
            '''print("Package: ")
            print(package)'''
            package_address = package.get_address()
            # print(distance_graph.search(current_location, package_address))
            distance = distance_graph.search(current_location, package_address)

            # print(len(distance_graph.search(current_location, package_address)))
            # print("Package list j: " + str(package))
            '''print("distance DURING: ")
            print(distance)'''

            if distance < min_distance:
                # print("loop")
                # print("Distance[0]: " + distance[0])
                min_distance = distance
                next_delivery = package
                temp = package_list[i]
                package_list[i] = next_delivery
                package_list[j] = temp
                '''print("Next Delivery: ")
                print(next_delivery)'''
        optimized_list.append(next_delivery)
        current_location = next_delivery.get_address()
        # print("Current Location: ")
        # print(next_delivery.get_address())
        distance_list.append(min_distance)
    '''print("Current Location AT END: ")
    print(current_location)
    print("Starting Location END: ")
    print(starting_location)
    print("Distance list: END")
    print(distance_list)'''

    for min_distance in distance_list:
        total_distance += min_distance
    '''print("Total Distance: ")
    print(total_distance)

    print("Optimized List: ")
    for next_delivery in optimized_list:
        print("Package {}".format(package.__str__()))'''

    return_to_start = distance_graph.search(current_location, starting_location)
    '''print("Return to hub: ")
    print(return_to_start)'''
    current_location = "4001 South 700 East"
    distance_list.append(return_to_start)

    return optimized_list, distance_list, total_distance
