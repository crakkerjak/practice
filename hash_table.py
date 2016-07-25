#!/usr/bin/python3

class hash_table:

    def __init__(self):
        self.num_buckets = 128
        self.buckets = [[] for i in range(self.num_buckets)]

    def put(self, k, v):
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
        bucket = self.buckets[hash(k) % self.num_buckets]
        v = None
        i = 0
        while v is None and i < len(bucket):
            if k == bucket[i][0]:
                v = bucket[i][1]
            i += 1
        return v

    def remove(self, k):
        bucket = self.buckets[hash(k) % self.num_buckets]
        v = None
        i = 0
        while v is None and i < len(bucket):
            if k == bucket[i][0]:
                v = bucket[i][1]
                del (bucket[i])
            i += 1
        return v
