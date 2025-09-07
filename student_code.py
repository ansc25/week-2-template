'''Representing graphs'''

node_dict={'a':0,'b':1,'c':2,'d':3,'e':4}

def part_1_graph():
    """
    Returns the part 1 graph represented as a list of sets.
    """
    graph = [
        {'b', 'e'},      # a
        {'c'},           # b
        {'d', 'e'},      # c
        {'b'},           # d
        set()            # e
    ]
    return graph

def part_2_graph():
    """
    Returns the part 2 graph represented as a list of lists.
    """
    graph = [
        ['a', 'b', 'e'],     # a
        ['c'],               # b
        ['a', 'd', 'e'],     # c
        [],                  # d
        ['d']                # e
    ]
    return graph

def part_3_graph():
    """
    Returns the part 3 graph (weighted) represented as a list of dicts with weights.
    """
    graph = [
        {'a': 8, 'b': 1, 'e': 4},  # a
        {'c': 3},                  # b
        {'a': 2, 'e': 4},          # c
        {},                        # d
        {}                         # e
    ]

    return graph

def part_4_graph():
    """
    Returns the part 4 graph represented as a dict of sets.
    """
    graph = {
        'a': {'a', 'b', 'e'},
        'b': {'c'},
        'c': {'a'},
        'd': set(),
        'e': set()
    }
    return graph

def part_5_graph():
    """
    Returns the weighted part 5 graph represented as a dict of dicts.
    """
    graph = {
        'a': {'b': 5},
        'b': {'e': 3},
        'c': {},
        'd': {},
        'e': {'a': 6, 'b': 2}
    }
    return graph
