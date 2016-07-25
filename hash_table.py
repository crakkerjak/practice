#!/usr/bin/python3
class HashTable:
    '''A simple list-based implementation of a hash table.

    Implements key hashing to place k, v pairs in an 'array' of buckets.

    Attributes:
        num_buckets: The number of buckets in the underlying data structure.
        buckets: A list of lists representing an array of buckets.
    '''

    def __init__(self):
        '''Inits hash_table with num_buckets and an empty bucket array.'''
        self.num_buckets = 128
        self.buckets = [[] for i in range(self.num_buckets)]

    def put(self, k, v):
        '''Places a k, v pair in the HashTable.'''
        bucket = self.buckets[hash(k) % self.num_buckets]
        placed = False
        i = 0
        while not placed:
            if i == len(bucket):
                bucket.append((k, v))
                placed = True
            elif k == bucket[i][0]:
                bucket[i] = (k, v)
                placed = True
            i += 1

    def get(self, k):
        '''Returns a value for a given key, or None if key is not present.'''
        bucket = self.buckets[hash(k) % self.num_buckets]
        v = None
        i = 0
        while v is None and i < len(bucket):
            if k == bucket[i][0]:
                v = bucket[i][1]
            i += 1
        return v

    def remove(self, k):
        '''Removes a k, v from the HashTable and returns v or None.'''
        bucket = self.buckets[hash(k) % self.num_buckets]
        v = None
        i = 0
        while v is None and i < len(bucket):
            if k == bucket[i][0]:
                v = bucket[i][1]
                del (bucket[i])
            i += 1
        return v
