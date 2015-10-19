from esp.weso.pyshex.rdf_graph.rdf_edge import RdfEdge
from esp.weso.pyshex.rdf_graph.rdf_edge_node import RdfEdgeNode
from esp.weso.pyshex.rdf_graph.rdf_node import RdfNode
from esp.weso.pyshex.rdf_graph.repeated_node_exception import RepeatedNodeException

__author__ = 'Dani'


class RdfGarph(object):

    def __init__(self):
        self._nodes = set()


    def add_node(self, rdf_node):
        if rdf_node in self._nodes:
            raise RepeatedNodeException("Node '{0}' already exists.")
            #Inserting a node object it is not like inserting a triplete. The object comes build and
            #could have relations builted. If we just check it the node exst andm, if it does, we do not
            # add it to the set, it could happen that the programmer expect some relations in its graph
            # that hadn't been added because we reject in a quiet way a node here
            # That's why we need to raise an exception
        self._nodes.add(rdf_node)

    def add_instances_triplete(self, instance_subject, instance_predicate, instance_object):
        if not instance_subject in self._nodes:
            self._nodes.add(instance_subject)
        else:
            self._nodes.update(instance_subject)  # TODO: I think this substitute the "node" in set by my received "node"...
                                            #TODO: BUT I HAVE TO CHECK IT WHEN HAVING INTERNET.
        if not instance_object in self._nodes:
            self._nodes.add(instance_object)
        else:
            self._nodes.update(instance_object)  # TODO: Same as the previous case

        instance_subject.add_relation(edge=instance_predicate,
                                      node=instance_object)

    def add_string_triplete(self, string_subject, string_predicate, string_object):
        node_subjetc = RdfNode(string_subject)
        if not node_subjetc in self._nodes:
            self._nodes.add(node_subjetc)
        else:
            self._nodes.update(node_subjetc)  # TODO: I think this substitute the "node" in set by my received "node"...
                                            #TODO: BUT I HAVE TO CHECK IT WHEN HAVING INTERNET.
        node_object = RdfNode(string_object)
        if not node_object in self._nodes:
            self._nodes.add(node_object)
        else:
            self._nodes.update(node_object)  # TODO: Same as the previous case

        node_subjetc.add_relation(edge=RdfEdge(string_predicate),
                                  node=node_object)
        #Done
