__author__ = 'Dani'


class ShReducedShexpression(object):

    def __init__(self, shtype, shlabel_types=None):
        if shlabel_types is None:
            shlabel_types = set()
        self.shtype = shtype
        self._shlabel_types = shlabel_types


    def add_shlabel_type(self, shlabel_type):
        self._shlabel_types.add(shlabel_type)

    def get_shlabel_types(self):
         # It does not look too useful... No reason to put it private
        return self._shlabel_types
