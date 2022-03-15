from datetime import datetime, timedelta

from package import my_hash_table
from util import distance_graph


class Truck:
    def __init__(self, truck_num, departure_time):
        self.truck_num = truck_num
        self.CAPACITY = 16
        self.loaded_packages = []
        self.curr_location = "4001 South 700 East"
        self.SPEED = 18
        self.miles_traveled = 0
        self.departure_time = departure_time
        self.curr_time = datetime.now().strftime("%H:%M:%S")
        # self.delivered_packages = []

    def __str__(self):
        return "Truck Number: %s, Packages Loaded: %s, Current Location: %s, Miles Traveled: %s, Current Time: %s" % (
            self.truck_num, self.loaded_packages, self.curr_location, self.miles_traveled, self.curr_time)

    def set_departure_time(self, departure_time):
        self.departure_time = departure_time

    def get_miles_traveled(self):
        return self.miles_traveled

    def get_delivered_packages(self):
        return self.delivered_packages

    def clear_packages(self):
        self.loaded_packages.clear()
        # print("CLEARED PACKAGES")

    def update_deliver_status(self):
        for p in self.loaded_packages:
            p.delivery_status = "Loaded on truck " + str(self.truck_num) + " at " + str(
                self.departure_time.strftime(
                    "%H:%M:%S")) + ". Still in transit. "

    def load_packages(self, truck_num, package_list):
        # if self.departure_time <= set_time:
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

    def deliver_packages(self, set_time, optimized_list, distance_list):
        self.curr_time = self.departure_time
        '''print("Temp Time AT START LOOP: ")
        print(self.curr_time)'''
        # print(type(temp_time))
        self.miles_traveled = 0
        '''print("Distance List: ")
        print(distance_list)'''
        delivered_packages = []
        self.update_deliver_status()
        for i in range(len(distance_list) - 1):  # run through distance list

            if self.curr_time < set_time:  # set time is time you want to see statuses at and temp time is the loop
                # time per iteration
                self.miles_traveled += distance_list[i]  # add distance to the miles traveled
                time_elapsed_in_seconds = ((distance_list[
                                                i] / 18.0) * 60.0) * 60.0  # time elapse in minutes with decimal
                # being the seconds fraction of a minute
                # time_elapsed = timedelta(seconds=time_elapsed_in_seconds)
                # temp_time += timedelta(seconds=time_elapsed_in_seconds)
                '''print("Temp Time After first temp time < set time check: ")
                print(self.curr_time)'''

                package_delivered_id = optimized_list[i].get_package_id()
                '''print("Loaded Packages: ")
                print(self.loaded_packages)'''
                '''if temp_time + timedelta(seconds=time_elapsed_in_seconds) < set_time:
                    temp_time += timedelta(seconds=time_elapsed_in_seconds)
                    print("Time Temp New: ")
                    print(temp_time)'''

                if (self.curr_time + timedelta(seconds=time_elapsed_in_seconds)) < set_time:
                    self.curr_time += timedelta(seconds=time_elapsed_in_seconds)
                    count = 0
                    for p in self.loaded_packages:

                        if p.get_package_id() == package_delivered_id and ("10:30" in p.get_delivery_deadline() or
                                                                           "9:00" in p.get_delivery_deadline()):

                            self.curr_location = p.get_address()
                            p.set_delivery_status(
                                "Delivered at " + str(
                                    self.curr_time.strftime("%H:%M:%S")))  # but the right time from above
                            self.loaded_packages.remove(p)
                            delivered_packages.append(p)
                            print("Package delivered: ")
                            print(p)
                            # my_hash_table.update(p.get_package_id(), p)
                            '''for pa in delivered_packages:
                                print("Delivered packages: ")
                                print(pa)'''

                        elif p.get_package_id() == package_delivered_id:
                            self.curr_location = p.get_address()
                            p.set_delivery_status(
                                "Delivered at " + str(
                                    self.curr_time.strftime("%H:%M:%S")))  # but the right time from above
                            self.loaded_packages.remove(p)
                            delivered_packages.append(p)

                            # update hash table
                            my_hash_table.update(p.get_package_id(), p)
                            print("Package delivered: ")
                            print(p)
                            '''for pa in delivered_packages:
                                print("Delivered packages: ")
                                print(pa)'''
        if len(self.loaded_packages) == 0:
            self.return_truck()
        else:
            print("\nRemaining packages on truck " + str(self.truck_num) + ": ")
            for p in self.loaded_packages:
                print(p)

    def return_truck(self):
        hub = "4001 South 700 East"
        dist_to_hub = distance_graph.search(self.curr_location, hub)
        self.curr_location = "4001 South 700 East"
        self.miles_traveled += dist_to_hub  # add distance to the miles traveled
        time_elapsed_in_seconds = ((dist_to_hub / 18.0) * 60.0) * 60.0
        self.curr_time += timedelta(seconds=time_elapsed_in_seconds)
