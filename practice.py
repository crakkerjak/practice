#!/usr/bin/python3


def min_range_in_k_sorted_lists(lists):
    '''
    You have k lists of sorted integers. Find the smallest range
    that includes at least one number from each of the k lists.

    For example,
    List 1: [4, 10, 15, 24, 26]
    List 2: [0, 9, 12, 20]
    List 3: [5, 18, 22, 30]

    The smallest range here would be [20, 24] as it contains 24 from list 1,
    20 from list 2, and 22 from list 3.
    '''
    search_idx = [0] * len(lists)

    next_min_idx = 0
    smallest_range = (lists[0][0], lists[0][-1])

    while search_idx[next_min_idx] < len(lists[next_min_idx]):
        range_min = lists[0][search_idx[0]]
        range_max = range_min
        next_min = lists[0][-1]

        for i, l in enumerate(lists):
            if search_idx[i] < len(l):
                if l[search_idx[i]] < range_min:
                    range_min = l[search_idx[i]]
                    range_min_idx = i
                elif l[search_idx[i]] > range_max:
                    range_max = l[search_idx[i]]
                    range_max_idx = i
            if search_idx[i] < len(l)-1 and l[search_idx[i]+1] < next_min:
                next_min = l[search_idx[i]+1]
                next_min_idx = i

        search_idx[next_min_idx] += 1

        if range_max - range_min < smallest_range[1] - smallest_range[0]:
            smallest_range = (range_min, range_max)

    return smallest_range


def pots_of_gold(pots):
    '''
    Pots of gold game: Two players A & B. There are pots of gold arranged in a
    line, each containing some gold coins (the players can see how many coins
    are there in each gold pot - perfect information). They get alternating
    turns in which the player can pick a pot from one of the ends of the line.
    The winner is the player which has a higher number of coins at the end. The
    objective is to "maximize" the number of coins collected by A, assuming B
    also plays optimally. A starts the game.

    The idea is to find an optimal strategy that makes A win knowing that B is
    playing optimally as well. How would you do that?

    At the end I was asked to code this strategy!
    '''
    if len(pots) == 0:
        return 0
    if len(pots) == 1:
        return pots[0]
    # else we have two endpoints to choose from
    # one of which is component to the optimal solution
    first = pots[0] + min(pots_of_gold(pots[2:]), pots_of_gold(pots[1:-1]))
    last = pots[-1] + min(pots_of_gold(pots[:-2]), pots_of_gold(pots[1:-1]))
    return max(first, last)


def max_diff_subarrays(A):
    '''
    Given an array of integers. Find two disjoint contiguous sub-arrays such
    that the absolute difference between the sum of two sub-array is maximum.
    The sub-arrays should not overlap.

    eg- [2 -1 -2 1 -4 2 8] ans - (-1 -2 1 -4) (2 8), diff = 16

    I gave him O(n^2) algorithm but he was not satisfied.
    '''
    max_ending_here = max_so_far = A[0]
    max_ending_here_range = (0, 0)
    max_so_far_range = (0, 0)
    min_ending_here = min_so_far = A[0]
    min_ending_here_range = (0, 0)
    min_so_far_range = (0, 0)

    max_before = []
    min_before = []
    # memoize max and min subset sum before each element
    for i, n in enumerate(A[1:]):
        i += 1
        # track max subset sum with indices
        if (n > max_ending_here +A[i]):
            max_ending_here =A[i]
            max_ending_here_range = (i, i)
        else:
            max_ending_here +=A[i]
            max_ending_here_range = (max_ending_here_range[0], i)
        if max_ending_here > max_so_far:
            max_so_far = max_ending_here
            max_so_far_range = max_ending_here_range
        max_before.append((max_so_far, max_so_far_range))
        # track min subset sum with indices
        if (n < min_ending_here +A[i]):
            min_ending_here =A[i]
            min_ending_here_range = (i, i)
        else:
            min_ending_here +=A[i]
            min_ending_here_range = (min_ending_here_range[0], i)
        if min_ending_here < min_so_far:
            min_so_far = min_ending_here
            min_so_far_range = min_ending_here_range
        min_before.append((min_so_far, min_so_far_range))


    last = len(A) - 1
    max_ending_here = max_so_far = A[-1]
    max_ending_here_range = (last, last)
    max_so_far_range = (last, last)
    min_ending_here = min_so_far = A[-1]
    min_ending_here_range = (last, last)
    min_so_far_range = (last, last)

    max_after = []
    min_after = []
    # memoize max and min subset sum after each element
    for i in range(len(A) - 2, -1, -1):
        # track max subset sum with indices
        if (n > max_ending_here + A[i]):
            max_ending_here = A[i]
            max_ending_here_range = (i, i)
        else:
            max_ending_here += A[i]
            max_ending_here_range = (i, max_ending_here_range[1])
        if max_ending_here > max_so_far:
            max_so_far = max_ending_here
            max_so_far_range = max_ending_here_range
        max_after.append((max_so_far, max_so_far_range))
        # track min subset sum with indices
        if (n < min_ending_here + A[i]):
            min_ending_here = A[i]
            min_ending_here_range = (i, i)
        else:
            min_ending_here += A[i]
            min_ending_here_range = (i, min_ending_here_range[1])
        if min_ending_here < min_so_far:
            min_so_far = min_ending_here
            min_so_far_range = min_ending_here_range
        min_after.append((min_so_far, min_so_far_range))

    max_diff = (0, (0, 0), (0, 0))
    for i in range(len(min_before)):
        diff = abs(min_before[i][0] - max_after[i][0])
        if diff > max_diff[0]:
            max_diff = (diff, min_before[i][1], max_after[i][1])
        diff = abs(max_before[i][0] - min_after[i][0])
        if diff > max_diff[0]:
            max_diff = (diff, max_before[i][1], min_after[i][1])

    return (max_diff)


def longest_palindrome(s):
    '''
    Given a string return the longest palindrome that can be constructed by
    removing or shuffling characters.

    Example:
    'aha' -> 'aha'
    'ttaatta' -> ' ttaaatt'
    'abc' -> 'a' or 'b' or 'c'
    'gggaaa' -> 'gaaag' or 'aggga'

    Note if there are multiple correct answers you only need to return 1
    palindrome.
    '''
    A_ORD = ord('a')
    count = [0] * 27
    s = s.lower()
    # count chars in string
    for ch in s:
        count[ord(ch) - A_ORD] += 1
    # build palindrome
    result = ''
    middle = ''
    # build first half
    for i, c in enumerate(count):
        if not middle and c % 2 == 1:
            middle = chr(i + A_ORD)
        while c > 1:
            result += chr(i + A_ORD)
            c -= 2
    # add middle char and second half
    return result + middle + result[::-1]


def probability_of_alive(N, x, y, n):
    '''
    There is an island which is represented by square matrix NxN.
    A person on the island is standing at any given co-ordinates (x,y). He can
    move in any direction one step right, left, up, down on the island. If he
    steps outside the island, he dies.

    Let island is represented as (0,0) to (N-1,N-1) (i.e NxN matrix) &
    person is standing at given co-ordinates (x,y). He is allowed to move n
    steps on the island (along the matrix). What is the probability that he is
    alive after he walks n steps on the island?

    Write a psuedocode & then full code for function
     " float probabilityOfAlive(int x,int y, int n) ".
    '''
    def p_helper(N, x, y, n):
        # recursive base case
        if n == 0:
            return 1
        if x < 0 or y < 0:  # dead
            return 0

        # symmetry -> one quadrant
        if x > (N - 1) / 2:
            x = (N - 1) - x
        if y > (N - 1) / 2:
            y = (N - 1) - y

        # 4 cases: corner, side, and inner positions
        if x == 0 and y == 0:  # corner
            this_square =  0.5
        elif x == 0 or y == 0:  # side
            this_square = 0.75
        else:                   # inner
            this_square = 1
        return this_square * (
                p_helper(N, x - 1, y, n - 1) * 0.25 +
                p_helper(N, x, y - 1, n - 1) * 0.25 +
                p_helper(N, x + 1, y, n - 1) * 0.25 +
                p_helper(N, x, y + 1, n - 1) * 0.25
        )

    return p_helper(N, x, y, n)
