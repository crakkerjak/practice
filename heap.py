#!/usr/bin/env python3

# Heap:
# implementation of priority queue
# array structure visualized as nearly complete binary tree

# root at index 1
# left_child at 2i, right_child at 2i + 1

# max heap: each node's key >= keys of children

class MaxHeap:
    def __init__(self, l=None):
        self.heap = [0]
        if l:
            self._build_max_heap(l)

    def __str__(self):
        return str(self.heap)

    def _build_max_heap(self, l):
        # _build_max_heap
        # upper bound: O(n log n) - n/2 calls to _max_heapify
        # tight bound: Theta(n) - each of those calls is asymptotically O(1)
        self.heap = [0] + [item for item in l]
        # elements n/2+1..n are leaves. all others may have leaves
        for i in range((int)((len(l)+1)/2), 0, -1):
            self._max_heapify(i)

    def _max_heapify(self, i):  # O(log n)
        # precondition: node's children are max heaps
        # leaves are trivially max heaps by definition
        swap_index = None
        for index in [2*i, 2*i+1]:
            if (index < len(self.heap)
                    and self.heap[index] > self.heap[i]
                    and (swap_index is None
                            or self.heap[index] > self.heap[swap_index])):
                swap_index = index
        if swap_index is not None:
            self._swap(i, swap_index)
            self._max_heapify(swap_index)
        # return true if a swap was made - used in insert
        return swap_index is not None

    def _swap(self, i, j):
        temp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = temp

    def size(self):
        return len(self.heap) - 1

    def insert(self, key):
        self.heap.append(key)
        i = (int)((len(self.heap) - 1)/2)
        not_placed = True
        while not_placed and i > 0:
            not_placed = self._max_heapify(i)
            i = (int)(i / 2)

    def max(self):
        return self.heap[1]

    def extract_max(self):
        _max = self.heap[1]
        self.heap[1] = self.heap[-1]
        del self.heap[-1]
        self._max_heapify(1)
        return _max

    def as_sorted_list(self):
        cp = self.copy()
        sl = []
        while cp.heap != [0]:
            sl.append(cp.extract_max())
        return sl

    def copy(self):
        mh = MaxHeap()
        mh.heap = [key for key in self.heap]
        print (mh.heap)
        return mh


if __name__ == '__main__':
    heap = MaxHeap([1, 2, 3, 4, 5])
    print (heap)
    print (heap.as_sorted_list())
    heap.insert(6)
    print (heap)
    heap.insert(4)
    print (heap)
    heap.insert(3)
    print (heap)
    print (heap.max())
    print (heap.extract_max())
    print (heap)
