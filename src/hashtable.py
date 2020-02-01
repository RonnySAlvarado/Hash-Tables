# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        index = self._hash_mod(key)
        curr_node = self.storage[index]
        if self.storage[index] is None:
            self.storage[index] = LinkedPair(key, value)
            return f'This is the first node and the ({key}, {value}) pair has been inserted at index {index}.'
        if self.storage[index].key == key:
            self.storage[index].value = value
            return f'The key: {key} already exists and has had its value overwritten by {value} at index {index}.'
        while curr_node.next is not None:
            if curr_node.next.key == key:
                curr_node.next.value == value
                return f'The key: {key} already exists and has had its value overwritten by {value} at index {index}.'
            curr_node = curr_node.next
        curr_node.next = LinkedPair(key, value)
        return f'The ({key}, {value}) pair has been inserted at index {index}.'

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        curr_node = self.storage[index]
        next_node = curr_node.next

        if curr_node.key == key:
            self.storage[index] = None
            return f'The first node at this index has been deleted'

        while next_node is not None:
            if next_node.key == key:
                curr_node.next == next_node.next
                next_node = None
                return f'The node with {key} has been deleted'
            curr_node = next_node
            next_node = curr_node.next

        return f'The node with {key} was not found'

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        curr_node = self.storage[index]
        if curr_node.key == key:
            return curr_node.value
        while curr_node.next is not None:
            if curr_node.key == key:
                return curr_node.value
            curr_node = curr_node.next
        return None

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        self.capacity = self.capacity*2
        newStorage = [None] * self.capacity
        tempArr = []
        for idx in self.storage:
            curr_node = idx
            while True:
                tempArr.append((curr_node.key, curr_node.value))
                if curr_node.next is None:
                    break
                curr_node = curr_node.next
        self.storage = newStorage
        for idx in tempArr:
            self.insert(idx[0], idx[1])


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")

# hashTbl = HashTable(5)
# print(hashTbl.insert('Something', 4))
# print(hashTbl.insert('Another', 10))
# print(hashTbl.insert('Last', 15))
# print(hashTbl.insert('Last', 20))
# print(hashTbl.retrieve('Last'))
