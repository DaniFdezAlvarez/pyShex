from esp.weso.pyshex.typyng.node_typing import NodeTyping

__author__ = 'Dani'


class Typing(object):

    def __init__(self, node_typings_set=None):
        if node_typings_set is None:
            node_typings_set = set()
        self._node_typings = node_typings_set


    def get_node_type_units(self):
        result = set()
        for n_typ in self._node_typings:
            result = result.union(n_typ.get_node_type_units())
        return result

    def get_node_typings(self):
        return self._node_typings

    def add_type_to_node(self, node, shtype):
        for n_typ in self._node_typings:
            if n_typ.node == node:
                n_typ.add_type(shtype)
                return
        #If we dind't enter in the previous if's body:
        new_node_typyng = NodeTyping(node)
        new_node_typyng.add_type(shtype)
        self._node_typings.add(new_node_typyng)
