from esp.weso.pyshex.bag.bag import Bag
from esp.weso.pyshex.rdf_graph.rdf_relation import RdfRelation

__author__ = 'Dani'


class RdfNode(object):

    def __init__(self, uri):
        self.uri = uri
        self._relations = Bag()
        pass

    def add_relation(self, edge, node):
        self._relations.add(RdfRelation(edge, node))

    def out(self):
        """
        It returns a set with every node reachable from "self" using a single edge

        """
        result = set()
        for relation in self._relations:  # TODO: no! bag is not iterable
            set.add(relation.node)
        return result

    def out_lab(self):
        """
        It returns a set of (arist, node) containing all nodes
        reachable from "self" using a single arist, with this arist
        (classes rdf_relation)
        """
        result = set()
        for relation in self._relations:  # TODO: no! bag is not iterable
            result.add(relation)
        return result

