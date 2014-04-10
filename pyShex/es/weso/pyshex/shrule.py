__author__ = 'Dani'

class ShRule(object):
    """
    Basic Rules class. Every type of rule should extend this

    """
    def __init__(self, min_occurs=1, max_occurs=1, is_entering=False, is_negation=False):
        """
        Constructor.
         - minOccurs and maxOccurs for multiplicity. there is a constant for UNBOUNDED in maxOccurs
         - is_entering is a boolean that indicates if we are talking of a rule that comes to the type/node.
        Example: if the rule is "a::person" and is_entering is true, that means..... a person should be pointing
        the node with "a" ???
         - is_negation is a boolean that means that must not occur t validate the expression

        The default values are for the most common case: multiplicity 1, not negated and not entering

        """
        # TODO: SURE ABOUT ENTERING RULES?

        self._min_occurs = min_occurs
        self._max_occurs = max_occurs
        self._is_entering = is_entering
        self._is_negation = is_negation






