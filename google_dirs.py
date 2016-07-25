#!/usr/bin/env python3

# split file structure into lines
#     for each line:
#         get depth
#         trim wd
#         if file_name represents an image
#             add wd to set of dirs with images
#         else -> is a sub_dir
#             add sub_dir to wd
#     return total chars in set of sub_dirs


# google directory question:
def solution(s):
    file_structure = s.split('\n')
    wd = []
    current_depth = 0
    dirs = set()
    for entry in file_structure:
        fn = entry.strip()
        current_depth = len(entry) - len(fn)
        wd = wd[:current_depth]
        if '.' in fn:
            if fn.split('.')[1] in ['jpeg','png','gif']:
                dirs.add(''.join(s for s in wd))
        else:
            wd.append('/' + fn)
    return sum(len(s) for s in dirs)


if __name__ == '__main__':
    print (solution('dir1\n dir11\n dir12\n  picture.jpeg\n   dir121\n    file1.txt\ndir2\n file2.gif\n')) # google
