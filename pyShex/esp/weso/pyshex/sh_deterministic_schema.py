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

    def get_possible_label_types(self):
        #TODO: REVISE ALL THIS
        result = set()
        for rule in self._rules:
            result = result.union(rule)

    def resulting_type_from_a_given_type_and_edge(self, shtype, shlabel):
        """
        sigma function of two parameters in Iovka et al's algorithm

        """
        units_of_type =

        #TODO:
        return "Aa"