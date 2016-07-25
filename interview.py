#!/usr/bin/env python3
def is_unique(s):
    chars = {}
    for i in range(0, len(s)):
        if s[i] in chars:
            return False
        chars.add(s[i])
    return True


def is_unique_no_ds(s):
    for i in range(0, len(s)):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                return False
    return True

def check_permutation(s1, s2):
    return count_chars_in_string(s1) == count_chars_in_string(s2)

def count_chars_in_string(s):
    chars = {}
    for i in range(0, len(s)):
        if s[i] not in chars:
            chars[s[i]] = 1
        else:
            chars[s[i]] += 1
    return chars


def urlify(s):
    return s.replace(' ', '%20')


def palindrome_permutation(s):
    chars = count_chars_in_string(s.lower());
    odd_found = False
    for char in chars:
        if char == ' ':
            continue
        if chars[char] % 2 != 0:
            if odd_found:
                return False
            else:
                odd_found = True
    return True


def one_away(s1, s2):
    if abs(len(s1) - len(s2)) > 1:
        return False
    i1, i2, distance = (0, 0, 0)
    while i1 < len(s1) and i2 < len(s2):
        if s1[i1] != s2[i2]:
            distance += 1
            if distance > 1:
                return False
            # 3 cases: len(s1) < len(s2), vice versa, ==
            if len(s1) < len(s2):
                i2 += 1
            if len(s1) == len(s2):
                i1 += 1
                i2 += 1
            if len(s1) > len(s2):
                i1 += 1
        else:
            i1 += 1
            i2 += 1
    return True


def rotate_matrix(m):
    # if not square, return unchanged
    if len(m) != len(m[0]):
        return m
    # transpose
    for i in range(0, len(m)):
        for j in range (i, len(m)):
            temp = m[i][j]
            m[i][j] = m[j][i]
            m[j][i] = temp
    # reverse 'rows'
    for i in range(0, len(m)):
        m[i].reverse()
    return m


def zero_matrix(m):
    from copy import deepcopy
    zeroed = deepcopy(m)
    for i in range(0, len(m)):
        for j in range (i, len(m)):
            if m[i][j] == 0:
                zero_row(i, zeroed)
                zero_column(j, zeroed)
    return zeroed

def zero_row(i, m):
    for n in range(0, len(m[i])):
        m[i][n] = 0

def zero_column(j, m):
    for n in range(0, len(m)):
        m[n][j] = 0


def first_duplicate(s):
    all_words = {}
    word_list = s.split()
    for word in word_list:
        if word in all_words:
            return word
        else:
            all_words.add(word)
    return None


def get_duplicates(s):
    all_words = {}
    duped_words = {}
    word_list = s.split()
    for word in word_list:
        if word in all_words:
            duped_words.add(word)
        else:
            all_words.add(word)
    return duped_words


def recursive_fib(n):  # O(2^n)
    if n < 2:
        print('1')
        return n
    return recursive_fib(n-1) + recursive_fib(n-2)


def iterative_fib(n):  # O(n)
    last_1 = 0;
    last_2 = 1;
    for i in range(1, n):
        fib = last_1 + last_2
        last_1 = last_2
        last_2 = fib
    return fib


def reverse_alnum_chars(s):
    char_list = list(s)
    i = 0
    j = len(char_list) - 1
    while i < j:
        while i < j and not char_list[i].isalnum():
            i += 1
        while i < j and not char_list[j].isalnum():
            j -= 1
        if i < j:
            temp = char_list[i]
            char_list[i] = char_list[j]
            char_list[j] = temp
            i += 1
            j -= 1
    return ''.join(char_list)


if __name__ == '__main__':
    # print(is_unique('asdf'))  # True
    # print(is_unique('asdfa'))  # False
    # print(is_unique_no_ds('asdf'))  # True
    # print(is_unique_no_ds('asdfa'))  # False

    # print(check_permutation('asdf', 'fdsa'))  # True
    # print(check_permutation('asdfa', 'asdfb'))  # False
    # print(check_permutation('fff', 'fff'))  # True
    # print(check_permutation('aabbc', 'abcba'))  # True

    # print(palindrome_permutation('tact coa'))  # True
    # print(palindrome_permutation('tact coaa'))  # False

    # print(one_away('asdf', 'asdf'))  # True
    # print(one_away('asdf', 'assf'))  # True
    # print(one_away('asdf', 'asf'))  # True
    # print(one_away('asdf', 'asdxf'))  # True
    # print(one_away('asdfa', 'asdf'))  # True
    # print(one_away('asdf', 'fdsa'))  # False
    # print(one_away('asdf', 'asdfaa'))  # False

    # print(str(rotate_matrix([[1,2,3],[4,5,6],[7,8,9]])))
    # print(str(rotate_matrix([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])))

    # print(str(zero_matrix([[1,2,3],[4,0,6],[7,8,9]])))

    # print(first_duplicate('a s d a f d'))

    # print(get_duplicates('a s d a f d'))

    # print(str(recursive_fib(10)))
    # print(str(iterative_fib(10)))

    print(reverse_alnum_chars('<script>alert(1)</script>'))
