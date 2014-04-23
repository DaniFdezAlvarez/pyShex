__author__ = 'Dani'

from .shrule import ShRule


class OrRule(ShRule):


    def __init__(self, rules=None, min_occurs=1, max_occurs=1, is_entering=False, is_negation=False):
        super(OrRule, self).__init__(min_occurs=min_occurs,
                                     max_occurs=max_occurs,
                                     is_entering=is_entering,
                                     is_negation=is_negation)
        if rules is None:
            rules = []
        self._rules = rules


    def __eq__(self, other):
        if not type(self) == type(other):
            return False
        if not len(self._rules) == len(other._rules):
            return False
        for i in range(0, len(self._rules)):
            if not self._rules[i] == other._rules[i]:
                return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)


    def __hash__(self):
        result = 0
        for rule in self._rules:
            result ^= hash(rule)  # XOR_EQUAL SIGN... pretty freak =)
        return result

    def get_possible_label_types(self):
        result = set()
        if self._is_entering or self._is_negation:
            return result
        for rule in self._rules:
            result = result.union(rule.get_possible_label_types())
        return result
