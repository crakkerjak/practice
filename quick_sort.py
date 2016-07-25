#!/usr/bin/env python3

def quick_sort(l, lo, hi):
    if lo < hi:
        # position 1 value (the 'pivot') correctly
        # with all lesser values before it and greater values after it
        p = partition(l, lo, hi)
        # recurse on lesser and greater partitions
        quick_sort(l, lo, p - 1)
        quick_sort(l, p + 1, hi)

# move all values less than the pivot to the first partition and place pivot
def naive_partition(l, lo, hi):
    pivot = l[hi]
    i = lo
    # tracking the number moved (and shifting the write index) with i
    for j in range(lo, hi):
        if l[j] < pivot:
            swap (l, i, j)
            i += 1
    # place the pivot in its proper position
    swap (l, i, hi)
    # return index of properly placed pivot
    return i

def partition(l, lo, hi):
    # can optimize by choosing middle, random, or median of several values
    if hi - lo > 3:
        swap(l, (int)((lo+hi)/2), hi)
    pivot = l[hi]
    i = lo
    j = hi

    while i < j:
        # find value less than pivot
        while i < j and l[i] <= pivot:
            i += 1
        # find value greater than pivot
        while i < j and l[j] >= pivot:
            j -= 1
        # swap if both found
        if i < j:
            swap(l, i, j)
    # place pivot
    swap (l, i, hi)
    return i


def swap(l, i, j):
    temp = l[i]
    l[i] = l[j]
    l[j] = temp


if __name__ == '__main__':
    l = [10, 9, 7, 3, 4, 5, 2, 1, 0, 11, 12, 2, 7]
    quick_sort(l, 0, len(l) - 1)
    print(l)
