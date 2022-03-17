from datetime import datetime, timedelta

import main
import packages
from util import distance_graph


class Truck:
    def __init__(self, truck_num, departure_time):
        """
        Initializes truck objects with default capacity of 16, speed of 18, curr_location at the hub, and miles_traveled
        of 0.
        :param truck_num: The number of the truck
        :param departure_time: The time the truck with depart with deliveries
        """
        self.truck_num = truck_num
        self.CAPACITY = 16
        self.loaded_packages = []
        self.curr_location = "4001 South 700 East"
        self.SPEED = 18
        self.miles_traveled = 0
        self.departure_time = departure_time
        self.curr_time = datetime.now().strftime("%H:%M:%S")
        self.delivered_packages = []

    def __str__(self):
        """
        Formats printing a truck as the following with specific attributes listed.
        :return: String representation of a truck object
        """
        return "Truck Number: %s, Packages Loaded: %s, Current Location: %s, Miles Traveled: %s, Current Time: %s" % (
            self.truck_num, self.loaded_packages, self.curr_location, self.miles_traveled, self.curr_time)

    def set_departure_time(self, departure_time):
        """
        Sets the truck's departure time.
        :param departure_time: The time to depart on deliveries
        """
        self.departure_time = departure_time

    def get_miles_traveled(self):
        """
        Gets the miles traveled by the truck.
        :return: Miles traveled
        """
        return self.miles_traveled

    def get_loaded_packages(self):
        """
        Get the packages loaded on the truck.
        :return: Loaded packages list
        """
        return self.loaded_packages

    def get_delivered_packages(self):
        """
        Get the packages delivered by the truck.
        :return: Delivered packages list
        """
        return self.delivered_packages

    def get_delivered_and_loaded_packages(self):
        delivered_and_loaded_packages_list = []
        for p in self.get_loaded_packages():
            delivered_and_loaded_packages_list.append(p)
        for pp in self.get_delivered_packages():
            delivered_and_loaded_packages_list.append(pp)

    def clear_packages(self):
        """
        Clears the loaded packages list.
        """
        for p in self.delivered_packages:
            self.delivered_packages.remove(p)
            self.loaded_packages.append(p)
        # self.loaded_packages.clear()
        # self.delivered_packages.clear()
        # print("CLEARED PACKAGES")

    def update_delivery_status(self, status):
        """
        Updates the delivery status of packages being loaded on the trucks.
        """
        # runs through loaded packages list and updates all the statuses
        if status == "loaded":
            for p in self.loaded_packages:
                p.delivery_status = "Loaded on truck " + str(self.truck_num) + " at " + str(
                    self.departure_time.strftime(
                        "%H:%M:%S")) + ". Still in transit. "
        elif status == "hub":
            for p in self.delivered_packages:
                if "Delayed" in str(p):
                    p.delivery_status = "Delayed. Arriving at hub at " + \
                                        str(datetime.now().replace(hour=9, minute=5, second=0).strftime("%H:%M:%S"))
                else:
                    p.delivery_status = "Arrived at hub at " + \
                                        str(datetime.now().replace(hour=7, minute=30, second=0).strftime("%H:%M:%S"))

    def load_packages(self, truck_num, package_list, set_time):
        """
        Loads the packages from a list onto the specific truck adding them to the loaded packages list
        :param set_time: The set time to stop when looking for specific time status
        :param truck_num: The number of the truck being loaded
        :param package_list: The list of packages to be loaded
        """
        if self.departure_time < set_time:
            # runs through the package list and loads each package onto the truck
            for i in range(len(package_list)):
                package = package_list[i]
                '''package.delivery_status = "Loaded on truck " + str(truck_num) + " at " + str(
                        self.departure_time.strftime(
                            "%H:%M:%S")) + ". Still in transit. "'''
                self.loaded_packages.append(package)
                '''print("Package Id when Loaded: ")
                    print(package.get_package_id())'''

                # print("Packages Loaded on Truck:")
                # print("Package: {}".format(package.__str__()))

    def deliver_packages(self, set_time, shortest_distance_list, distance_list):
        """
        Delivers the packages loaded onto a truck using the shortest_distance list order plus the distance_list to
        calculate miles traveled.
        Space-time complexity of O(n^2).
        :param set_time: The time to stop the delivery process. Default is EOD. Used to check status at specific times.
        :param shortest_distance_list: List with order for delivering packages to optimize mileage
        :param distance_list: The list of distances between each address in the optimized list in order
        :return:
        """
        self.curr_time = self.departure_time
        '''print("Temp Time AT START LOOP: ")
        print(self.curr_time)'''
        # print(type(temp_time))
        self.miles_traveled = 0
        '''print("Distance List: ")
        print(distance_list)'''
        self.update_delivery_status("loaded")

        # run through the distance list to deliver each one
        for i in range(len(distance_list) - 1):  # run through distance list

            # checks to see if the set time is later than the current time. used to determine how far in delivery
            # route to complete for status updates
            if self.curr_time <= set_time:
                # time per iteration
                time_elapsed_in_seconds = ((distance_list[
                                                i] / 18.0) * 60.0) * 60.0  # time elapse in minutes with decimal
                # being the seconds fraction of a minute
                '''print("Temp Time After first temp time < set time check: ")
                print(self.curr_time)'''

                package_delivered_id = shortest_distance_list[i].get_package_id()
                '''print("Loaded Packages: ")
                print(self.loaded_packages)'''
                '''if temp_time + timedelta(seconds=time_elapsed_in_seconds) < set_time:
                    temp_time += timedelta(seconds=time_elapsed_in_seconds)
                    print("Time Temp New: ")
                    print(temp_time)'''

                # checks if elapsed time goes past the set time to tell method to stop
                if (self.curr_time + timedelta(seconds=time_elapsed_in_seconds)) <= set_time:
                    self.curr_time += timedelta(seconds=time_elapsed_in_seconds)
                    # print(self.curr_time + timedelta(seconds=time_elapsed_in_seconds))
                    self.miles_traveled += distance_list[i]  # add distance to the miles traveled
                    # runs through each package in loaded packages
                    for p in self.loaded_packages:
                        # updates the delivery status and removes the package from loaded and onto delivered list
                        if p.get_package_id() == package_delivered_id:
                            self.curr_location = p.get_address()
                            p.set_delivery_status(
                                "Delivered at " + str(
                                    self.curr_time.strftime("%H:%M:%S")))  # but the right time from above
                            self.loaded_packages.remove(p)
                            self.delivered_packages.append(p)

                            # update hash table
                            packages.hash_table.update(p.get_package_id(), p)
                            print("Package delivered: ")
                            print(p)
                            '''for pa in delivered_packages:
                                print("Delivered packages: ")
                                print(pa)'''
                else:
                    self.curr_location = "In transit to next delivery"
                    temp_time = set_time - self.curr_time
                    # print(temp_time)
                    temp_time_seconds = temp_time.total_seconds()
                    # print(temp_time_seconds)
                    temp_time_hours = ((temp_time_seconds / 60) / 60)
                    temp_time_miles = (temp_time_hours * 18)
                    # print(temp_time_miles)
                    self.miles_traveled += temp_time_miles
                    # print(self.miles_traveled)
                    self.curr_time += timedelta(seconds=temp_time_seconds)
        if self.departure_time > set_time:
            print("Truck not yet loaded. Truck will be loaded at " + str(self.curr_time.strftime("%H:%M:%S")))
        elif len(self.loaded_packages) == 0:
            if len(self.delivered_packages) != 0:
                self.return_truck(set_time)
        # prints the packages remaining on truck at the status check time by last delivery timestamp
        elif len(self.loaded_packages) > 0:
            print("\nRemaining packages on truck " + str(self.truck_num) + ": ")
            for p in self.loaded_packages:
                print(p)

        # checks if list empty to return truck to hub

    def return_truck(self, set_time):
        """
        Returns the truck to the hub by checking current location to hub distance and updating truck time and mileage
        """
        hub = "4001 South 700 East"
        dist_to_hub = distance_graph.search(self.curr_location, hub)
        time_elapsed_in_seconds = ((dist_to_hub / 18.0) * 60.0) * 60.0
        if (self.curr_time + timedelta(seconds=time_elapsed_in_seconds)) < set_time:
            self.curr_location = "4001 South 700 East"
            self.miles_traveled += dist_to_hub  # add distance to the miles traveled
            self.curr_time += timedelta(seconds=time_elapsed_in_seconds)
            self.curr_time = self.curr_time.strftime("%H:%M:%S")
        else:
            self.curr_location = "In transit to hub"
            temp_time = set_time - self.curr_time
            # print(temp_time)
            temp_time_seconds = temp_time.total_seconds()
            # print(temp_time_seconds)
            temp_time_hours = ((temp_time_seconds / 60) / 60)
            temp_time_miles = (temp_time_hours * 18)
            # print(temp_time_miles)
            self.miles_traveled += temp_time_miles
            # print(self.miles_traveled)
            self.curr_time += timedelta(seconds=temp_time_seconds)
            self.curr_time = self.curr_time.strftime("%H:%M:%S")
            # print(self.curr_time)
