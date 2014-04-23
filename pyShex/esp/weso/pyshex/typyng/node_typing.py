__author__ = 'Dani'


class NodeTyping(object):

    def __init__(self, node, types_set=None):
        if types_set is None:
            types_set = set()
        self.node = node
        self._types = types_set

    def add_type(self, shtype):
        self._types.add(shtype)

    def get_node_type_units(self):
        result = set()
        for shtype in self._types:
            result.add()
        return result