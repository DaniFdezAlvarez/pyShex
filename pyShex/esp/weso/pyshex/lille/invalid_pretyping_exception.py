__author__ = 'Dani'


class InvalidPretypingException(BaseException):

    def __int__(self, msg):
        self.message = msg
