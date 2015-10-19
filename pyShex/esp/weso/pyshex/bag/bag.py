from esp.weso.pyshex.bag.no_bag_received_exception import NoBagReceivedException
from esp.weso.pyshex.bag.no_such_object_exception import NoSuchObjectException

__author__ = 'Dani'

from .bag_entry import BagEntry
import copy


# noinspection PyBroadException
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

    def __len__(self):
        result = 0
        for key in self._elements:
            result += self._elements[key].count
        return result

    def __eq__(self, other):
        return self.contained_in_bag(other) and self.contains_bag(other)
        #TODO: It is possible to improve the complexity

    def __ne__(self, other):
        return not self.__eq__(other)

    def __iter__(self):
        for key in self._elements:
            entry = self._elements[key]
            for i in range(0, entry.count):
                yield copy.deepcopy(entry.content)  # Not sure if we need to do this... but it looks like yes:
                #We are not storing original objects, but incrementing a counter. So it wouldn't be logic
                #returning always tha same object when count > 1 when it could not be the original one.
                #It is better to never return originals, always copies...


    def add(self, elem):
        """
        If the object is not on the dict, it creates its entry initialized in 1.
        Else, increments one the counter of its entry.
        """

        if not hash(elem) in self._elements:
            self._elements[hash(elem)] = BagEntry(elem)
        else:
            self._elements[hash(elem)].count += 1

    def remove(self, elem):
        """
        It will remove a single occurs of the object form the bag.
        If it can't remove the object because it does not exist, it throws an exception
        """
        key_elem = hash(elem)
        if not key_elem in self._elements:
            raise NoSuchObjectException("Object {0} not found in the bag".format(str(elem)))
        else:
            entry = self._elements[key_elem]
            if entry.count == 1:
                del self._elements[key_elem]
            else:  # entry.count > 1
                entry.count -= 1


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
        in an equal or superior quantity.
        When receiving something different to a bag, it raises a NoBagReceivedException

        """
        if type(bag) != type(self):
            raise NoBagReceivedException("The parameter should be a bag")
        try:
            for elem_other in bag._elements:
                entry_other = bag._elements[elem_other]
                if self.times(entry_other.content) < entry_other.count:
                    return False
            return True
        except:
            return False

    def contained_in_bag(self, bag):
        """
        It checks if all the elements of self are present in "bag",
        in an equal or lower quantity.
        When receiving something different to a bag, it raises a NoBagReceivedException
        """
        if type(bag) != type(self):
            raise NoBagReceivedException("The parameter should be a bag")

        try:
            for elem_self in self._elements:
                entry_self = self._elements[elem_self]
                if bag.times(entry_self.content) < entry_self.count:
                    return False
            return True
        except:
            return False






