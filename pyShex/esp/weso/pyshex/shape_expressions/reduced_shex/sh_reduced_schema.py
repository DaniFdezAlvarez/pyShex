from esp.weso.pyshex.shape_expressions.no_type_in_schema_error import NoTypeInSchemaError
from esp.weso.pyshex.shape_expressions.reduced_shex.shreduced_shexpression import ShReducedShexpression

__author__ = 'Dani'



class ShReducedSchema:
    """
    It represents a reduced vision of a ShEx Schemma. It assigns to each type what type you could reach using
    only an edge with a concrete label.
    i.e.: with a ShEx like:

    A {
     :b B *,
     :c B +,
     :d G
    }

    We will have a ShSchemma that stores that, from type A,
    with an arist b you can reach a B; with a c, a B; with a d, a G


    """


    def __init__(self):
        self._sh_reduced_shexs = {}

    def add_reduced_shex(self, shreduced_shex):
        self._sh_reduced_shexs[shreduced_shex.shtype] = shreduced_shex

    def add_reachable_type_to_type(self, origin, sh_label_type):
        if origin in self._sh_reduced_shexs:
            self._sh_reduced_shexs[origin].add_shlabel_type(sh_label_type)

        #If the if's body does nto execute
        new_red_shex = ShReducedShexpression(origin)
        new_red_shex.add_shlabel_type(sh_label_type)
        self._sh_reduced_shexs[origin] = new_red_shex

    def get_reduced_shex_of_a_type(self, shtype):
        if shtype in self._sh_reduced_shexs:
            return self._sh_reduced_shexs[shtype]
        else:
            raise NoTypeInSchemaError("Type '{0}' not found in schema".format(shtype.name))






