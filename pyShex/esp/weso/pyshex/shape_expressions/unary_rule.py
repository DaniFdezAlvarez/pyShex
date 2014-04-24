from esp.weso.pyshex.shape_expressions.reduced_shex.shlabel_type import ShLabelType

__author__ = 'Dani'
from .esp.weso.pyshex.shape_expressions.shrule import ShRule


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

    def get_possible_label_types(self):
        result = set()
        if self._is_entering or self._is_negation:
            return result
        result.add(ShLabelType(self._sh_label, self._sh_type))
        return result





