#!/usr/bin/python3

class TreeMaker:
    def __init__(self, data):
        self.structure = _builder(data, structure)

    def _builder(data, structure):
        if not data:
            return structure
        else:
            structure.build_something(data)
            return _builder(data, structure)



if __name__ == '__main__':
    data = {'animal':['cat','dog','horse'],
            'cat':['lion','tiger'],
            'dog':['wolf','coyote','politician'],
            'horse':['race','work','dead'],
            'cat':['lion','tiger','house'],
            'tiger':['foot_ball_player','bengal','zoo_prisoner']}
    print (data)
