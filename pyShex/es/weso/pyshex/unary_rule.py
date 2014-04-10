__author__ = 'Dani'
from .shrule import ShRule


class UnaryRule(ShRule):

    def __init__(self, sh_label, sh_type, min_occurs=1, max_occurs=1, is_entering=False, is_negation=False):
        super(UnaryRule, self).__init__(min_occurs=min_occurs,
                                        max_occurs=max_occurs,
                                        is_entering=is_entering,
                                        is_negation=is_negation)
        self._sh_label = sh_label
        self._sh_type = sh_type

    def __eq__(self, other):
        if not type(self) == type(other):
            return False
        if not self._sh_label == other._sh_label:
            return False
        if not self._sh_type == other._sh_type:
            return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)


    def __hash__(self):
        return hash(self._sh_label) ^ hash(self._sh_type)



