#!/usr/bin/python3

'''
Suppose you have the number 142336327778988999. Determine the highest number in which two or more of the same number are next to each other.
Ex: 3,7,8,9 are all consecutive but 9 is the highest.
'''


# kadane's algorithm
def max_subarray(l):
    max_ending_here = 0
    max_so_far = 0
    for x in l:
        max_ending_here = max(0, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

# modified to allow array of all negative values
def neg_friendly_max_subarray(l):
    max_ending_here = l[0]
    max_so_far = l[0]
    for x in l[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far


def max_repeating_decimal_num(n):
    max_so_far = None
    last = n % 10
    n = int(n / 10)
    while n >= 1:
        decimal = n % 10
        n = int(n / 10)
        if decimal == last and (max_so_far is None or max_so_far < decimal):
            max_so_far = decimal
        last = decimal
    return max_so_far


def max_num_made_of_repeats(n):
    max_so_far = 0
    none_found = True
    current = None
    decimal = n % 10
    n = int(n / 10)
    while n >= 1:
        last = decimal
        decimal = n % 10
        n = int(n / 10)
        if decimal == last:
            if not current:
                current = str(decimal)
            none_found = False
            current += str(decimal)
        else:
            current = None
        if current: max_so_far = max(max_so_far, int(current))

    if none_found: max_so_far = None
    return max_so_far



if __name__ == '__main__':
    # print (max_repeating_decimal_num(10101010101))
    # print (max_repeating_decimal_num(10101110101))
    # print (max_repeating_decimal_num(40221433001))
    # print (max_repeating_decimal_num(10001010101))

    print (max_num_made_of_repeats(10101010101))
    print (max_num_made_of_repeats(10101110101))
    print (max_num_made_of_repeats(40221433001))
    print (max_num_made_of_repeats(10001010101))
    print (max_num_made_of_repeats(44221433001))
    print (max_num_made_of_repeats(44221431110))
    print (max_num_made_of_repeats(0))
    print (max_num_made_of_repeats(100))
