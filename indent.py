#!/usr/bin/env python3

def check_indentation(raw_code):
    lines = raw_code.split('\n')
    i = 0
    indentation = ''
    reasons_to_indent = ['def', 'class', 'for', 'while', 'if', 'else', 'elif']
    must_increase = False

    # TODO: allow explicit line continuation with '\'
    # TODO: allow implicit line continuation in open groups: (), [], {}
    # TODO: allow multiline comments
    # remove comments in both TODO cases

    # check each subsequent line for correct indentation
    while i < len(lines):
        # skip blank or completely commented lines
        unindented_line = lines[i].lstrip()
        if lines[i] == '' or unindented_line[0] == '#':
            i += 1
            continue

        this_indentation = lines[i][:-1 * len(unindented_line)]
        # if must_increase, require additional whitespace
        if must_increase:
            if len(this_indentation) <= len(indentation):
                return i
            must_increase = False
        # must other wise maintain match with some higher level
        elif not indentation.startswith(this_indentation):
            return i

        # allow decreased indentation
        indentation = this_indentation
        # check if next line should be indented further
        if any (unindented_line.startswith(s) for s in reasons_to_indent):
            must_increase = True
        i += 1

    # indentation correct
    return -1


if __name__ == '__main__':
    s = '\n\ndef asdf(s):\n\tprint("s")\n\n\tprint("indented one tab too many")\n\tprint("correct")\n'
    print(check_indentation(s))
