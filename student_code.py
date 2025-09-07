'''Representing graphs'''

node_dict={'a':0,'b':1,'c':2,'d':3,'e':4}

def part_1_graph():
    """
    Returns the part 1 graph represented as a list of sets.
    """
    graph = [
        {1, 4},  # a -> b, e
        {2},     # b -> c
        {3, 4},  # c -> d, e
        {1},     # d -> b
        set()    # e -> (no outgoing edges)
    ]
    return graph

def part_2_graph():
    pass

def part_3_graph():
    pass

def part_4_graph():
    pass

def part_5_graph():
    pass
