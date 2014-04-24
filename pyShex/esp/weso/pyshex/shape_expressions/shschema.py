__author__ = 'Dani'



class ShSchema(object):
    """
    Represents a complete ShEx schema

    """

    def __init__(self, shexpressions=None):
        if shexpressions is None:
            shexpressions = set()
        self._shexpressions = shexpressions

    def add_sh_expression(self, sh_expression):
        self._shexpressions.add(sh_expression)


