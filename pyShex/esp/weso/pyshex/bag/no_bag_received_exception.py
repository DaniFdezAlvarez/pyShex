__author__ = 'Dani'


class NoBagReceivedException(BaseException):

    def __init__(self, msg):
        self.message = msg