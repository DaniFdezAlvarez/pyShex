__author__ = 'Dani'



class ShSchema(object):
    """
    Represents a complete ShEx schema

    """

    def __init__(self, rules=None):
        if rules is None:
            rules = []
        self._rules = rules

    def add_sh_expression(self, sh_expression):
        self._rules.append(sh_expression)


