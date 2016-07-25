#!/usr/bin/env python3

def bubble_sort(l):
    end = len(l)
    swapped = True;
    # until a full pass is made with no inverted pairs found
    while swapped:
        swapped = False;
        # iteratively swap each inverted pair
        for i in range(1, end):
            if l[i] < l[i - 1]: # flip sign to reverse order
                swap(l, i, i - 1)
                swapped = True
        # optimization: each iteration places the next highest value correctly
        end -= 1


def swap(l, i, j):
    temp = l[i]
    l[i] = l[j]
    l[j] = temp


if __name__ == '__main__':
    l = [10, 9, 8, 3, 4, 5, 2, 1, 0, 11, 12, 2, 7]
    bubble_sort(l)
    print(l)
