__author__ = 'Dani'

from esp.weso.pyshex.and_rule import AndRule
from esp.weso.pyshex.or_rule import OrRule
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

substringing()






