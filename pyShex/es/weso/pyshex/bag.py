__author__ = 'Dani'


class Bag(object):
    """
    Let's do it with dicts... by hash =)

    Data structure that contains unordered elements allowing repetition.


    """

    def __init__(self, **initial_elements):
        """
        Constructor. It could be extrange to allow people introduce it elements

        """
        self._elements = {}  # it will be a dict of object(of the represented object --> int (number of occurrences)
        for elem in initial_elements:
            self.add(elem)

    def __str__(self):
        result = "{|"
        for key in self._elements:
            result += "," + str(self._elements(key))
        result += "|}"
        return result

    def add(self, elem):
        """
        If the object is not on the dict, it creates its entry initialized in 1.
        Else, increments one the counter of its entry.
        """

        if elem in self._elements:
            self._elements[elem] = 1
        else:
            self._elements[elem] += 1


