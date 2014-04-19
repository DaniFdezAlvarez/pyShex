__author__ = 'Dani'


class RepeatedNodeException(BaseException):

    def __init__(self, msg):
        self.message = msg