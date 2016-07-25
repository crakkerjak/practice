#!/usr/bin/env python3

class hash_table:

    def __init__(self):
        num_buckets = 128
        self.buckets = [[] for i in range(self.num_buckets)]
        self.size = 0

    def __str__(self):
        return str(self.buckets)

    def put(self, key, value):
        # check for key, get index
        bucket, i = self._look_up(key)
        # update bucket
        if i is None:
            bucket.append((key, value))
            self.size += 1
        else:
            bucket[i] = (key, value)

    def get(self, key):
        # check for key, get index
        bucket, i = self._look_up(key)
        # return value or None
        if i is None:
            return None
        else:
            return bucket[i][1]

    def remove(self, key):
        bucket, i = self._look_up(key)

        if i is None:
            return None
        else:
            self.size -= 1
            return bucket.pop(i)[1]

    # find a key in the hashtable and return it's bucket and index
    def _look_up(self, key):
        i = 0
        bucket = self.buckets[hash(key) % self.num_buckets]
        found = False

        while i < len(bucket) and not found:
            if bucket[i][0] == key:
                found = True
            else:
                i += 1

        if not found:
            i = None

        return (bucket, i)

    def _cheesy_hash(self, key):
        from functools import reduce

        if is_digit(key):
            return key % self.num_buckets
        elif isinstance(key, str):
            return (reduce(lambda x, y: x+y, [ord(ch) for ch in key])
                    % self.num_buckets)
        else:
            return hash(key)


if __name__ == '__main__':
    ht = hash_table()
    key, value = 'one_key', 'one_value'
    print (hash(key)%100)
    print (ht)
    ht.put (key, value)
    print (ht)
    print (ht.get(key))

    key, value = 'two_key', 'two_value'
    print (hash(key)%100)
    ht.put (key, value)
    print (ht)
    print (ht.get('one_key'))
    print (ht.get('two_key'))
    print (ht.get('not_there'))

    for i in range(200):
        ht.put(i, i*2)

    print (ht)
    print (ht.get(36))
    print (ht.get(136))
    print (ht.get('one_key'))
    print (ht.get(100))
    print (ht.remove(100))
    print (ht.get(100))
