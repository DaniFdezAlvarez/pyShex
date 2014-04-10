__author__ = 'Dani'

from es.weso.pyshex.and_rule import AndRule
from es.weso.pyshex.or_rule import OrRule
from es.weso.pyshex.bag import Bag

a = AndRule()
b = AndRule()
c = OrRule()
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
b.add(c)

print b

h = Bag(a,a,c)
print h




