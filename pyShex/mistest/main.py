__author__ = 'Dani'

from esp.weso.pyshex.shape_expressions.and_rule import AndRule
from esp.weso.pyshex.bag.bag import Bag




def substringing():
    a = "Helo with an l"
    print a[:2] + a[3:]


def approach_to_bags():
    a = AndRule()
    b = AndRule()
    # c = OrRule()
    print str(a)
    print a
    print hash(a)
    print hash(b)
    a.name = "Pepe"
    print hash(a)

    b = Bag()
    print b

    b.add(a)
    b.add(a)
    # b.add(c)

    print b

    # h = Bag(a, a, c)
    h = Bag(a, b, b)

    print h


def approach_to_sets():
    a = set()
    a.add("a")
    print len(a)
    a.add("a")
    a.add("b")
    print len(a)
    element = a.pop()
    print element
    print len(a)


# substringing()
# approach_to_bags
approach_to_sets()






