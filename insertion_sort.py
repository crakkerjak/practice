#!/usr/bin/env python3

def insertion_sort(l):
    # for each value from 0 to array end
    for i in range(0, len(l)):
        j = i
        # move current value left into position in sorted "subarray"
        temp = l[j]
        while j > 0 and l[j] < l[j - 1]:
            l[j] = l[j - 1]
            l[j - 1] = temp
            j -= 1;
    return l

if __name__ == '__main__':
    print(insertion_sort([10, 9, 8, 3, 4, 5, 2, 1, 0, 11, 12, 2, 7]))
