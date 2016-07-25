#!/usr/bin/env python3

def merge(l1, l2):
    merged_list = []
    # merge lists (assumed ordered) until one is empty
    while len(l1) != 0 and len(l2) != 0:
        if l1[0] < l2[0]:
            merged_list.append(l1.pop(0))
        else:
            merged_list.append(l2.pop(0))
    # append remaining elements
    merged_list.extend(l1);
    merged_list.extend(l2);
    return merged_list

def merge_sort(l):
    len_l = len(l)
    # base case
    if len_l < 2:
        return l
    # recurse on two list halves
    return merge(merge_sort(l[:(int)(len_l/2)]), merge_sort(l[(int)(len_l/2):]))

if __name__ == '__main__':
    print(merge_sort([10, 9, 8, 3, 4, 5, 2, 1, 0, 11, 12, 2, 7]))
