#!/usr/bin/python3

# 2 passes, one with sum in C
# O(n) and Theta(2n) time, O(n) and Theta(n) space
def eq_index(l):
    l_sum = 0
    r_sum = sum(l)
    for i, n in enumerate(l):
        r_sum -= n
        if l_sum == r_sum:
            yield i
        l_sum += n


# 1 pass, but uses another data structure
# O(n) and Theta(n) time, O(n) and Theta(cn) space
def eq_index_one_pass(l):
    from collections import defaultdict
    l_sum = 0
    h = defaultdict(list)
    for i, n in enumerate(l):
        l_sum += n
        # eq_idx exists when l_sum is half of final total sum
        h[l_sum * 2 - n].append(i)
    return h[l_sum]


# this does more math than eq_index, but shows how/why the one_pass
# version works
def eq_index_v2(l):
    l_sum = 0
    total = sum(l)
    for i, n in enumerate(l):
        if l_sum * 2 - n == total:
            yield i
        l_sum += n


if __name__ == '__main__':
    l = [-10,5,4,3,0,0,0,-3,12,-7]

    print(list(eq_index(l)))  # 4,5,6

    print(list(eq_index_v2(l)))  # 4,5,6

    print (eq_index_one_pass(l))
