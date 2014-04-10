__author__ = 'Dani'

from .bag_entry import BagEntry


class Bag(object):
    """
    Let's do it with dicts... by hash =)

    Data structure that contains unordered elements allowing repetition.


    """

    def __init__(self, *initial_elements):
        """
        Constructor.

        """
        self._elements = {}  # it will be a dict of object(of the represented object --> int (number of occurrences)
        for elem in initial_elements:
            self.add(elem)

    def __str__(self):
        result = "{|"
        for key in self._elements:
            for i in range(0, self._elements[key].count):
                pass
                result += "," + str(self._elements[key].content)
        result += "|}"
        if len(result) == 4:
            return result  # Empty bag, no need to remove comma
        return result[:2] + result[3:]  # By this, we are removing a ','


    def add(self, elem):
        """
        If the object is not on the dict, it creates its entry initialized in 1.
        Else, increments one the counter of its entry.
        """

        if not hash(elem) in self._elements:
            self._elements[hash(elem)] = BagEntry(elem)
        else:
            self._elements[hash(elem)].count += 1


    def times(self, elem):
        """
        If the element is not in the bag, returns 0
        """
        if not hash(elem) in self._elements:
            return 0
        else:
            return self._elements[hash(elem)].count


    def contains_elem(self, elem):
        if hash(elem) in self._elements:
            return True
        else:
            return False


    def contains_bag(self, bag):
        """
        It checks is every elem of bag is present in self,
        in an equal or superior quantity

        """
        for elem_other in bag._elements:
            entry_other = bag._elements[elem_other]
            if self.times(entry_other.content) < entry_other.count:
                return False
        return True

    def contained_in_bag(self, bag):
        """
        It checks if all the elements of self are present in "bag",
        in an equal or lower quantity
        """
        for elem_self in self._elements:
            entry_self = self._elements[elem_self]
            if bag.times(entry_self.content) < entry_self.count:
                return False
        return True






