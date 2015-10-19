__author__ = 'Dani'


class ShType(object):
    def __init__(self, name):
        self._name = name

    @staticmethod
    def is_universal_type(other_type):
        if type(other_type) == ShUniversalType:
            return True
        return False



class ShUniversalType(ShType):

    def __init__(self):
        super(ShUniversalType, self).__init__("UNIVERSAL_TYPE")
