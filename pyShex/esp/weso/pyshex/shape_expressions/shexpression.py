__author__ = 'Dani'


class ShExpression(object):

    def __init__(self, sh_type, bag_rules):
        self._sh_type = sh_type
        self._sh_rules = bag_rules

    def get_possible_label_types(self):
        result = set()
        for a_rule in self._sh_rules:
            result = result.union(a_rule.get_possible_label_types)
        return result


