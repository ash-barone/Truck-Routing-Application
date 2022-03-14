class HashTable:

    def __init__(self, capacity=40):

        self.table = []
        for i in range(capacity):
            self.table.append([])

    def insert(self, key, item):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    def update(self, key, item):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for key_value in bucket_list:
            # print (key_value)
            if key_value[0] == key:
                key_value[1] = item
                return True
            else:
                print(key + " could not be updated. Please try again.")

    def search(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        # print(bucket_list)

        for key_value in bucket_list:
            # print (key_value)
            if key_value[0] == key:
                return key_value[1]
        return None

    def remove(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for key_value in bucket_list:
            # print (key_value)
            if key_value[0] == key:
                bucket_list.remove([key_value[0], key_value[1]])
