from es.weso.pyshex.bag.bag import Bag

__author__ = 'Dani'


import unittest


class TestBag(unittest.TestCase):

    def test_str(self):
        #Different elements
        a = Bag("a", "b", "c", "d")
        # self.assertEquals("{|a,b,c,d|}", str(a))

        #Empty
        b = Bag()
        self.assertEquals("{||}", str(b))

        #Equal elements
        c = Bag("a", "a")
        self.assertEquals("{|a,a|}", str(c))

        #Ints
        d = Bag(1, 2)
        self.assertEquals("{|1,2|}", str(d))

        #Elements of different class
        e = Bag(1, "a")
        self.assertEquals("{|1,a|}", str(e))

        #Manipulated bags
        e.add("b")
        self.assertEquals(str(b), "{|1,a,b|}")

        #TODO: No man... the elements are unordered. If this pass, it is a question of luck. And it is not necessary





        pass

    def test_add(self):
        #TODO
        pass

    def test_times(self):
        #TODO
        pass

    def test_contains_elem(self):
        #TODO
        pass

    def test_contains_bag(self):
        #TODO
        pass

    def test_contained_in_bag(self):
        #TODO
        pass
