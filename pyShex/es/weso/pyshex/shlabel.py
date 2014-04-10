__author__ = 'Dani'


class ShLabel(object):

    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        if not self.name == other.name:
            return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)


    def __hash__(self):
        return hash(self.name)
