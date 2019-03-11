# Question A
#
# Your goal for this question is to write a program that accepts two lines (x1,x2)
# and (x3,x4) on the x-axis and returns whether they overlap. As an example, (1,5)
# and (2,6) overlaps but not (1,5) and (6,8).


def do_they_overlap(x1:tuple, x2:tuple):
    assert(type(x1) == tuple), "x1 should be a tuple (val1, val2)"
    assert(type(x2) == tuple), "x2 should be a tuple (val1, val2)"
    for value in [x1, x2]:
        assert (type(value[0]) == int or type(value[0]) == float), 'the tuples should contains int or float elements'
        assert (type(value[1]) == int or type(value[1]) == float), 'the tuples should contains int or float elements'

    # as both lines should be over the x-axis, i can just reorder the tuples if needed
    def swap_if_needed(x):
        return x if x[0] < x[1] else (x[1], x[0])
    x1 = swap_if_needed(x1)
    x2 = swap_if_needed(x2)

    if (x1[0] > x2[1]) or (x1[1] < x2[0]):
        return False

    return True


# I've make sure that the tuples values are numbers, than I've swapped (if needed) the values of both
# tuples to get them ordered. After this, it is just a matter of checking if they intersect using the
# if statement ( if (x1[0] > x2[1]) or (x1[1] < x2[0]) ).
