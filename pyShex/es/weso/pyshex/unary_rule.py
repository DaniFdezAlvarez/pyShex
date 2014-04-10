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



