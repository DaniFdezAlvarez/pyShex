from esp.weso.pyshex.shschema import ShSchema

__author__ = 'Dani'


class ShDetSchema(ShSchema):

    def __init__(self, rules=None):
        super(ShDetSchema, self).__init__(rules)
        self._check_determinism()

    def _check_determinism(self):
        for a_rule in self._rules:
            #TODO: DO SOMETHING
            pass
        return True  # In some point we have to raise something if this is false

    def add_sh_expression(self, sh_expression):
        #TODO: redefine this method. insert only if exp is deterministic.
        #TODO: if not, raise exception
        pass