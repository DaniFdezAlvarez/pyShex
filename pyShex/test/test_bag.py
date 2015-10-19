from esp.weso.pyshex.bag.bag import Bag
from esp.weso.pyshex.bag.no_bag_received_exception import NoBagReceivedException

__author__ = 'Dani'


import unittest


class TestBag(unittest.TestCase):

    def test_str(self):
        #Different elements
        a = Bag("a", "b", "c", "d")
        # self.assertEquals("{|a,b,c,d|}", str(a))
        self.assertEquals(len(str(a)), 11)
        self.assert_(str(a).__contains__("a"))
        self.assert_(str(a).__contains__("b"))
        self.assert_(str(a).__contains__("c"))
        self.assert_(str(a).__contains__("d"))


        #Empty
        b = Bag()
        self.assertEquals("{||}", str(b))

        #Equal elements
        c = Bag("a", "a")
        self.assertEquals("{|a,a|}", str(c))

        #Ints
        d = Bag(1, 2)
        # self.assertEquals("{|1,2|}", str(d))
        self.assertEquals(len(str(d)), 7)
        self.assert_(str(d).__contains__("1"))
        self.assert_(str(d).__contains__("2"))

        #Elements of different class
        e = Bag(1, "a")
        # self.assertEquals("{|1,a|}", str(e))
        self.assertEquals(len(str(e)), 7)
        self.assert_(str(e).__contains__("1"))
        self.assert_(str(e).__contains__("a"))


        #Manipulated bags
        e.add("b")
        # self.assertEquals(str(e), "{|1,a,b|}")
        self.assertEquals(len(str(e)), 9)
        self.assert_(str(e).__contains__("1"))
        self.assert_(str(e).__contains__("a"))
        self.assert_(str(e).__contains__("b"))

        print "passed!"


    def test_add(self):
        a = Bag()
        #Adding first element
        a.add("a")
        self.assertEquals(1, len(a))
        self.assertEquals(a.times("a"), 1)
        #Adding an element repeated
        a.add("a")
        self.assertEquals(a.times("a"), 2)
        #Adding many elements repeated
        a.add("a")
        a.add("a")
        self.assertEquals(a.times("a"), 4)
        #Adding a new element
        a.add("b")
        self.assertEquals(5, len(a))
        self.assertEquals(a.times("b"), 1)
        #Adding other repeated element
        a.add("b")
        self.assertEquals(6, len(a))
        self.assertEquals(a.times("b"), 2)
        #Adding an element of different nature
        a.add(1)
        self.assertEquals(7, len(a))
        self.assertEquals(a.times(1), 1)

        print "passed!"


    def test_times(self):
        bag = Bag()
        #Empty bag
        self.assertEquals(0, bag.times("a"))
        #One element bag
        bag.add("a")
        self.assertEquals(1, bag.times("a"))
        self.assertEquals(0, bag.times("b"))
        self.assertEquals(0, bag.times(BaseException()))  # A random different object
        #One duplicated element
        bag.add("a")
        self.assertEquals(2, bag.times("a"))
        self.assertEquals(0, bag.times("b"))
        self.assertEquals(0, bag.times(BaseException()))  # A random different object
        #One object with many occurs
        bag.add("a")
        bag.add("a")
        bag.add("a")
        self.assertEquals(5, bag.times("a"))
        self.assertEquals(0, bag.times("b"))
        self.assertEquals(0, bag.times(BaseException()))  # A random different object
        #With a new object
        bag.add("b")
        self.assertEquals(5, bag.times("a"))
        self.assertEquals(1, bag.times("b"))
        self.assertEquals(0, bag.times(BaseException()))  # A random different object
        #More occurs of that new object
        bag.add("b")
        bag.add("b")
        self.assertEquals(5, bag.times("a"))
        self.assertEquals(3, bag.times("b"))
        self.assertEquals(0, bag.times(BaseException()))  # A random different object
        #Removing "b", only one instance will remain
        bag.remove("b")
        bag.remove("b")
        self.assertEquals(5, bag.times("a"))
        self.assertEquals(1, bag.times("b"))
        self.assertEquals(0, bag.times(BaseException()))  # A random different object
        #"b" completely removed
        bag.remove("b")
        self.assertEquals(5, bag.times("a"))
        self.assertEquals(0, bag.times("b"))
        self.assertEquals(0, bag.times(BaseException()))  # A random different object
        #removing all occurs of "a" but one
        bag.remove("a")
        bag.remove("a")
        bag.remove("a")
        bag.remove("a")
        self.assertEquals(1, bag.times("a"))
        self.assertEquals(0, bag.times("b"))
        self.assertEquals(0, bag.times(BaseException()))  # A random different object
        #Completely removing "a"
        bag.remove("a")
        self.assertEquals(0, bag.times("a"))
        self.assertEquals(0, bag.times("b"))
        self.assertEquals(0, bag.times(BaseException()))  # A random different object
        #Objects with another nature
        bag.add(1)
        self.assertEquals(1, bag.times(1))
        bag.remove(1)
        self.assertEquals(0, bag.times(1))

        print "passed!"


    def test_contains_elem(self):
        #Empty bag
        bag = Bag()
        self.assertFalse(bag.contains_elem("a"))
        self.assertFalse(bag.contains_elem("b"))
        self.assertFalse(bag.contains_elem(1))

        #Bag one element
        bag.add("a")
        self.assertTrue(bag.contains_elem("a"))
        self.assertFalse(bag.contains_elem("b"))
        self.assertFalse(bag.contains_elem(1))

        #Bag one repeated element
        bag.add("a")
        self.assertTrue(bag.contains_elem("a"))
        self.assertFalse(bag.contains_elem("b"))
        self.assertFalse(bag.contains_elem(1))

        #Both elements present
        bag.add("b")
        self.assertTrue(bag.contains_elem("a"))
        self.assertTrue(bag.contains_elem("b"))
        self.assertFalse(bag.contains_elem(1))

        #Both elements repeated
        bag.add("b")
        self.assertTrue(bag.contains_elem("a"))
        self.assertTrue(bag.contains_elem("b"))
        self.assertFalse(bag.contains_elem(1))

        #Removing repetitions of one element
        bag.remove("b")
        self.assertTrue(bag.contains_elem("a"))
        self.assertTrue(bag.contains_elem("b"))
        self.assertFalse(bag.contains_elem(1))

        #Completly removing one element
        bag.remove("b")
        self.assertTrue(bag.contains_elem("a"))
        self.assertFalse(bag.contains_elem("b"))
        self.assertFalse(bag.contains_elem(1))

        #Completely removing both elements
        bag.remove("a")
        bag.remove("a")
        self.assertFalse(bag.contains_elem("a"))
        self.assertFalse(bag.contains_elem("b"))
        self.assertFalse(bag.contains_elem(1))

        #Object of different nature
        bag.add(1)
        self.assertFalse(bag.contains_elem("a"))
        self.assertFalse(bag.contains_elem("b"))
        self.assertTrue(bag.contains_elem(1))
        bag.remove(1)
        self.assertFalse(bag.contains_elem("a"))
        self.assertFalse(bag.contains_elem("b"))
        self.assertFalse(bag.contains_elem(1))

        print "passed!"


    def test_contains_bag(self):
        a = Bag()
        b = Bag()

        #A different instance than a bag
        other = Warning()
        with self.assertRaises(NoBagReceivedException):
            b.contains_bag(other)

        #Empty bags
        self.assertTrue(a.contains_bag(b))
        self.assertTrue(b.contains_bag(a))

        # a with one element (a, none)
        a.add("a")
        self.assertTrue(a.contains_bag(b))
        self.assertFalse(b.contains_bag(a))

        #both with the same element (a,a)
        b.add("a")
        self.assertTrue(a.contains_bag(b))
        self.assertTrue(b.contains_bag(a))

        #a with repeated elements. b not (aaa, a)
        a.add("a")
        a.add("a")
        self.assertTrue(a.contains_bag(b))
        self.assertFalse(b.contains_bag(a))

        #both qith the same number of repeated elements
        b.add("a")
        b.add("a")
        self.assertTrue(a.contains_bag(b))
        self.assertTrue(b.contains_bag(a))

        # a with a new element. b hasn't got it (aaab, aaa)
        a.add("b")
        self.assertTrue(a.contains_bag(b))
        self.assertFalse(b.contains_bag(a))

        #Bpth with the new element (aaab, aaab)
        b.add("b")
        self.assertTrue(a.contains_bag(b))
        self.assertTrue(b.contains_bag(a))

        #Adding elements in a different order (aaabccd, aaabdcc)
        a.add("c")
        a.add("c")
        a.add("d")
        b.add("d")
        b.add("c")
        b.add("c")
        self.assertTrue(a.contains_bag(b))
        self.assertTrue(b.contains_bag(a))

        #Bags taht does not contain each other
        a.add(1)
        b.add(2)
        self.assertFalse(a.contains_bag(b))
        self.assertFalse(b.contains_bag(a))

        #Simpler bags that does not contain each other
        c = Bag("a")
        d = Bag("b")
        self.assertFalse(c.contains_bag(d))
        self.assertFalse(d.contains_bag(c))

        print "passed!"


    def test_contained_in_bag(self):
        a = Bag()
        b = Bag()

        #A different instance than a bag
        other = Warning()
        with self.assertRaises(NoBagReceivedException):
            b.contains_bag(other)

        #Empty bags
        self.assertTrue(a.contained_in_bag(b))
        self.assertTrue(b.contained_in_bag(a))

        # a with one element (a, none)
        a.add("a")
        self.assertFalse(a.contained_in_bag(b))
        self.assertTrue(b.contained_in_bag(a))

        #both with the same element (a,a)
        b.add("a")
        self.assertTrue(a.contained_in_bag(b))
        self.assertTrue(b.contained_in_bag(a))

        #a with repeated elements. b not (aaa, a)
        a.add("a")
        a.add("a")
        self.assertFalse(a.contained_in_bag(b))
        self.assertTrue(b.contained_in_bag(a))

        #both qith the same number of repeated elements
        b.add("a")
        b.add("a")
        self.assertTrue(a.contained_in_bag(b))
        self.assertTrue(b.contained_in_bag(a))

        # a with a new element. b hasn't got it (aaab, aaa)
        a.add("b")
        self.assertFalse(a.contained_in_bag(b))
        self.assertTrue(b.contained_in_bag(a))

        #Bpth with the new element (aaab, aaab)
        b.add("b")
        self.assertTrue(a.contained_in_bag(b))
        self.assertTrue(b.contained_in_bag(a))

        #Adding elements in a different order (aaabccd, aaabdcc)
        a.add("c")
        a.add("c")
        a.add("d")
        b.add("d")
        b.add("c")
        b.add("c")
        self.assertTrue(a.contained_in_bag(b))
        self.assertTrue(b.contained_in_bag(a))

        #Bags taht does not contain each other
        a.add(1)
        b.add(2)
        self.assertFalse(a.contained_in_bag(b))
        self.assertFalse(b.contained_in_bag(a))

        #Simpler bags that does not contain each other
        c = Bag("a")
        d = Bag("b")
        self.assertFalse(c.contained_in_bag(d))
        self.assertFalse(d.contained_in_bag(c))

        print "passed!"

    def test_len(self):
        a = Bag()
        #Empty
        self.assertEquals(0, len(a))

        #One element
        a.add("a")
        self.assertEquals(1, len(a))

        #One repeated element (3)
        a.add("a")
        a.add("a")
        self.assertEquals(3, len(a))

        #Two elements (4)
        a.add("b")
        self.assertEquals(4, len(a))

        #Two repeated elements (6)
        a.add("b")
        a.add("b")
        self.assertEquals(6, len(a))

        #Different nature (7)
        a.add(1)
        self.assertEquals(7, len(a))

        # Removing repetitions of b (5)
        a.remove("b")
        a.remove("b")
        self.assertEquals(5, len(a))

        #Completely removing (4)
        a.remove("b")
        self.assertEquals(4, len(a))

        #Removing all elements but one (1)
        a.remove("a")
        a.remove("a")
        a.remove("a")
        self.assertEquals(1, len(a))

        #Removing all elements
        a.remove(1)
        self.assertEquals(0, len(a))

        print "passed!"


    def test_eq(self):
        a = Bag()
        b = Bag()

        #Empty bags
        self.assertEquals(a, b)

        #Empty bag vs bag one element
        a.add("a")
        self.assertNotEquals(a, b)

        #Bags with same elements (a,a)
        b.add("a")
        self.assertEquals(a, b)

        #(aaa, a) NO
        a.add("a")
        a.add("a")
        self.assertNotEquals(a, b)

        #(aaa, aaa) YES
        b.add("a")
        b.add("a")
        self.assertEquals(a, b)

        #(aaab,aaa) NOT
        a.add("b")
        self.assertNotEquals(a, b)

        #(aaab, aaab) YES
        b.add("b")
        self.assertEquals(a, b)

        #(aaabcd, aaabdc) different order of adiccion YES
        a.add("c")
        a.add("d")
        b.add("d")
        b.add("c")

        self.assertEquals(a, b)

        #Different nature (...1, ...1) YES
        a.add(1)
        b.add(1)
        self.assertEquals(a, b)

        #Different (...m, ...n) NO
        a.add("n")
        b.add("m")
        self.assertNotEquals(a, b)

        #Constructor vs add (a, a) YES
        a = Bag("a")
        b = Bag()
        b.add("a")
        self.assertEquals(a, b)

        #Constructor vs add (aa, aa) YES
        a = Bag("a", "a")
        b = Bag()
        b.add("a")
        b.add("a")
        self.assertEquals(a, b)

        #Constructor vs add (aab, aab)
        a = Bag("a", "a", "b")
        b = Bag()
        b.add("a")
        b.add("a")
        b.add("b")


        #Constructor vs add different (aa, ab) NO

        a = Bag("a", "a")
        b = Bag()
        b.add("a")
        b.add("b")
        self.assertNotEquals(a, b)

    def test_iter(self):
        #Empty bag
        a = Bag()
        items = 0
        for elem in a:
            items += 1
        self.assertEquals(items, 0)

        #One element (a)
        a = Bag("a")
        items = 0
        for elem in a:
            items += 1
        self.assertEquals(items, 1)

        #Many elements (aaa)
        a = Bag("a", "a", "a")
        items = 0
        for elem in a:
            self.assertEquals(elem, "a")
            items += 1
        self.assertEquals(items, 3)

        # Different elements (aaab)
        a = Bag("a", "a", "a", "b")
        items = 0
        items_a = 0
        items_b = 0
        for elem in a:
            if elem == "a":
                items_a += 1
            elif elem == "b":
                items_b += 1
            items += 1
        self.assertEquals(items, 4)
        self.assertEquals(items_a, 3)
        self.assertEquals(items_b, 1)

        # Different repeated elements (aaabbb)
        a = Bag("a", "a", "a", "b", "b", "b")
        items = 0
        items_a = 0
        items_b = 0
        for elem in a:
            if elem == "a":
                items_a += 1
            elif elem == "b":
                items_b += 1
            items += 1
        self.assertEquals(items, 6)
        self.assertEquals(items_a, 3)
        self.assertEquals(items_b, 3)


        #After removing repetitions of one element (aaab)
        a.remove("b")
        a.remove("b")
        items = 0
        items_a = 0
        items_b = 0
        for elem in a:
            if elem == "a":
                items_a += 1
            elif elem == "b":
                items_b += 1
            items += 1
        self.assertEquals(items, 4)
        self.assertEquals(items_a, 3)
        self.assertEquals(items_b, 1)

        #After removing completely an element (aaa)
        a.remove("b")
        items = 0
        items_a = 0
        items_b = 0
        for elem in a:
            if elem == "a":
                items_a += 1
            elif elem == "b":
                items_b += 1
            items += 1
        self.assertEquals(items, 3)
        self.assertEquals(items_a, 3)
        self.assertEquals(items_b, 0)

        #After removing everything
        a.remove("a")
        a.remove("a")
        a.remove("a")
        items = 0
        items_a = 0
        items_b = 0
        for elem in a:
            if elem == "a":
                items_a += 1
            elif elem == "b":
                items_b += 1
            items += 1
        self.assertEquals(items, 0)
        self.assertEquals(items_a, 0)
        self.assertEquals(items_b, 0)


