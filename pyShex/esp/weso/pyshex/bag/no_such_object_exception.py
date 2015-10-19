__author__ = 'Dani'


class NoSuchObjectException(BaseException):

    def __init__(self, msg):
        self.message = msg
