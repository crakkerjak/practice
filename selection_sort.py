#!/usr/bin/env python3
from sys import maxsize

def selection_sort(l):
    # swap each element with the minimum remaining element
    for i in range(0, len(l) - 1):
        min_index = 0
        rest_min = maxsize
        # find index of minimum element
        for j in range(i + 1, len(l)):
            if l[j] < rest_min:
                min_index = j
                rest_min = l[j]
        # swap current element with minimum
        if rest_min < l[i]:
            temp = rest_min
            l[min_index] = l[i]
            l[i] = temp
    return l


if __name__ == '__main__':
    print(selection_sort([10, 9, 8, 3, 4, 5, 2, 1, 0, 11, 12, 2, 7]))
