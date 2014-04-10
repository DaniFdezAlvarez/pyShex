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
