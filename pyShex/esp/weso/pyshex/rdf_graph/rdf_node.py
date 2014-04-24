from esp.weso.pyshex.bag.bag import Bag
from esp.weso.pyshex.rdf_graph.rdf_edge_node import RdfEdgeNode

__author__ = 'Dani'


class RdfNode(object):

    def __init__(self, uri):
        self.uri = uri
        self._relations = Bag()
        pass

    def __str__(self):
        return "node: " + self.uri

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        elif self.uri != other.uri:
            return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    def add_relation(self, edge, node):
        self._relations.add(RdfEdgeNode(edge, node))

    def out(self):
        """
        It returns a set with every node reachable from "self" using a single edge

        """
        result = Bag()
        for relation in self._relations:
            result.add(relation.node)
        return result

    def out_lab(self):
        """
        It returns a set of (arist, node) containing all nodes
        reachable from "self" using a single arist, with this arist
        (classes rdf_relation)
        """
        result = Bag()
        for relation in self._relations:
            result.add(relation)
        return result

