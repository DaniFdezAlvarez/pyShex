from esp.weso.pyshex.bag.bag import Bag
from esp.weso.pyshex.lille.invalid_pretyping_exception import InvalidPretypingException
from esp.weso.pyshex.shape_expressions.shtype import ShType
from esp.weso.pyshex.typyng.node_type_unit import NodeTypeUnit

__author__ = 'Dani'


class ExtensionFinder(object):

    def __init__(self):
        self.deterministic_schema = None
        self.graph = None
        self.pre_typing = None
        self._reduced_schema = None

    def run(self, deterministic_schema, graph, pre_typing):
        """
        It Rreturns the minimal extension or throws an exception if the pretyping was wrong
        schemma: ShSchemma object
        graph: RdfGraph object
        pre_typyng: Typing object

        """

        self.deterministic_schema = deterministic_schema
        self._reduced_schema = deterministic_schema.get_reduced_schema()
        self.graph = graph
        self.pre_typing = pre_typing

        extension_set = set()
        candidates = self.pre_typing.get_node_type_units()
        while not len(candidates) == 0:
            a_asignation = candidates.pop()  # Choose a random pair of candidates
            if not self._is_valid_asignation(a_asignation):
                raise InvalidPretypingException("The given pretyping is incorrect. Impossible to find minimal extension")
            extension_set.add(a_asignation)
            for a_relation in a_asignation.node.out_lab():
                resulting_type = self.resulting_type_from_a_given_type_and_edge(a_asignation.type, a_relation.edge)
                if not ShType.is_universal_type(resulting_type) and\
                        not self._is_pair_node_type_in_set(a_relation.node, a_asignation.type, extension_set) and\
                        not self._is_pair_node_type_in_set(a_relation.node, a_asignation.type, candidates):
                    self._add_pair_node_type_to_set(a_relation.node, a_asignation.type, candidates)

        return extension_set


    @staticmethod
    def _add_pair_node_type_to_set(node, shtype, set_of_pairs):
        set_of_pairs.add(NodeTypeUnit(node, shtype))

    @staticmethod
    def _is_pair_node_type_in_set(node, shtype, set_of_pairs):
        return NodeTypeUnit(node, shtype) in set_of_pairs

    def _is_valid_asignation(self, a_asignation):
        #TODO: continue here

        return True

    def resulting_type_from_a_given_type_and_edge(self, shtype, label):
        reduced_shex = self._reduced_schema.get_reduced_shex_of_a_type(shtype)

        for unit_label_type in reduced_shex:
            if unit_label_type.label == label:
                return unit_label_type.shtype
        return None


