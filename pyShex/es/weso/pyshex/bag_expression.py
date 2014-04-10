__author__ = 'Dani'

from .and_rule import AndRule


class BagExpression(object):

    def __init__(self, and_rule=None):
        if and_rule is None:
            and_rule = AndRule()
        self._and_rule = and_rule

