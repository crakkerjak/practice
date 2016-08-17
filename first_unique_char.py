from collections import defaultdict


def first_unique_char(s):
    chars = defaultdict(int)
    for c in s:
        chars[c] = chars[c] + 1
    for c in s:
        if chars[c] == 1:
            return c
    return None

# or yield to find each in order
def unique_chars(s):
    chars = defaultdict(int)
    for c in s:
        chars[c] = chars[c] + 1
    for c in s:
        if chars[c] == 1:
            yield c
    return None



if __name__ == "__main__":
    print (first_unique_char("asdpasd"))
    print (first_unique_char("pasdfasdf"))
    print (first_unique_char("asdfasdfp"))
    print (first_unique_char("aaaaapaaaa"))
    print (first_unique_char("asdpasdf"))
    print (first_unique_char("asdpfasd"))
    unique = unique_chars("asdpzasd")
    print (next(unique))
    print (next(unique))
