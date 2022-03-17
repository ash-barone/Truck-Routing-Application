import csv

import util
from graph import Graph

distance_graph = Graph()


def load_address_data(file_name, graph):
    """
    Reads distances.csv and adds each row as a vertex(address) to the graph.
    Space-time complexity of O(n^2).
    :param file_name: The csv file to read
    :param graph: The graph to add the vertices(addresses) to
    """
    with open(file_name) as distances:
        distance_data = csv.reader(distances, delimiter=',')
        address_line = next(distance_data)
        # print("address line: " + str(address_line))

        # Space-time complexity of O(n^2)
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
    """
    Calls the load address data method to create the graph of addresses
    """
    util.load_address_data("distances.csv", distance_graph)


def find_shortest_distance(truck_location, package_list):
    """
    Greedy algorithm shortest path method used to determine the order in which to deliver the packages. The algorithm
    uses an outer for loop which keeps track of where to begin looping through the list of packages and an inner for
    loop which loops through that list of packages using the start point from the outer loop. The algorithm then
    compares distances to store the shortest distance per iteration in a separate list. The greedy algorithm provides
    an in-the-moment optimized list since it only considers what is optimal at the exact moment it is comparing
    distance between the start point determined in the outer loop to the next point in the inner loop.
    Time complexity of O(n^2) since there are two for loops running through n times. The algorithm has a space
    complexity of O(n) since only the inner for loop uses an n amount of space with the outer loop only keeping the
    sort's place in the list.

    :param truck_location: The location of the truck
    :param package_list: The list of packages
    :return:
    """
    curr_location = truck_location
    next_location = None
    shortest_distance_list = []
    distance_list = []
    total_distance = 0

    # runs the count of package list length as a placeholder
    # Space-time complexity of O(n^2)
    for j in range(0, len(package_list)):
        shortest_distance = 9999
        # runs through the contents of package list to compare distances and find the lowest distance
        for k in range(len(package_list))[j:]:
            package = package_list[k]
            '''print("Package: ")
            print(package)'''

            # if the current shortest distance is no longer shortest, swap
            if shortest_distance > int(distance_graph.search(curr_location, package.get_address())):
                # print("loop")
                shortest_distance = int(distance_graph.search(curr_location, package.get_address()))
                temp_package = package_list[j]
                next_location = package
                package_list[k] = temp_package
                package_list[j] = next_location
                '''print("Next Location: ")
                print(next_location)'''
        # move list forward
        curr_location = next_location.get_address()

        # print("Current Location: ")
        # print(next_location.get_address())

        # add next location to the list
        shortest_distance_list.append(next_location)

        # add distance to the distance list for calculating total distance
        distance_list.append(shortest_distance)
    '''print("Current Location AT END: ")
    print(curr_location)
    print("Starting Location END: ")
    print(starting_location)
    print("Distance list: END")
    print(distance_list)'''

    starting_location = "4001 South 700 East"
    '''print("Return to hub: ")
        print(return_to_start)'''

    # add the return distance to the list for calculating
    distance_list.append(distance_graph.search(curr_location, starting_location))

    # run through the distances and add them up for total distance
    # Space-time complexity of O(n)
    for shortest_distance in distance_list:
        total_distance += shortest_distance

    '''print("Total Distance: ")
    print(total_distance)

    print("shortest_distance List: ")
    for next_location in shortest_distance_list:
        print("Package {}".format(package.__str__()))'''

    return shortest_distance_list, distance_list, total_distance
