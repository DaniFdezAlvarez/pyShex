from esp.weso.pyshex.shape_expressions.reduced_shex.sh_reduced_schema import ShReducedSchema
from esp.weso.pyshex.shape_expressions.reduced_shex.shreduced_shexpression import ShReducedShexpression
from esp.weso.pyshex.shape_expressions.shschema import ShSchema

__author__ = 'Dani'


class ShDetSchema(ShSchema):

    def __init__(self, rules=None):
        super(ShDetSchema, self).__init__(rules)
        self._check_determinism()

    def _check_determinism(self):
        for a_shex in self._shexpressions:
            #TODO: DO SOMETHING
            pass
        return True  # In some point we have to raise something if this is false

    def add_sh_expression(self, sh_expression):
        #TODO: redefine this method. insert only if exp is deterministic.
        #TODO: if not, raise exception
        pass

    def get_reduced_schema(self):
        result = ShReducedSchema()
        for a_shex in self._shexpressions:
            red_shex = ShReducedShexpression(shtype=a_shex.shtype,
                                             shlabel_types=a_shex.get_possible_label_types())
            result.add_reduced_shex(red_shex)
        return result

