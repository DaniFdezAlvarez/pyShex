from esp.weso.pyshex.lille.invalid_pretyping_exception import InvalidPretypingException

__author__ = 'Dani'


class ExtensionFinder(object):

    def __init__(self):
        self.schemma = None
        self.graph = None
        self.pre_typing = None

    def run(self, schemma, graph, pre_typing):
        """
        It Rreturns the minimal extension or throws an exception if the pretyping was wrong
        schemma: ShSchemma object
        graph: RdfGraph object
        pre_typyng: set object containing ShEdgeType objects

        """

        self.schemma = schemma
        self.graph = graph
        self.pre_typing = pre_typing

        extension = set()
        candidates = self._elements_in_pretyping()
        while not len(candidates) == 0:
            a_asignation = candidates.pop()  # Choose a random pair of candidates
            if not self._is_valid_asignation(a_asignation):
                raise InvalidPretypingException("Te given pretyping is incorrect. Impossible to find minimal extension")
            extension.add(a_asignation)
            for a_relation in a_asignation.node.out_lab():
                #TODO: continue here! line 8 of the algorithm Now i am developing the sigma
                #TODO: function over deterministic shex
                pass

    def _is_valid_asignation(self, a_asignation):
        #TODO: implement this this
        return True


    def _elements_in_pretyping(self):
        return self.pre_typing  # This method remains here because maybe we must not operate over
                            # the pretyping elements. Now, i think there is no problem with doing it
                            # and, by this, we can avoid extra computation such as making copies...
                            # but let's prepare the scenario to revoke this decission if needed
