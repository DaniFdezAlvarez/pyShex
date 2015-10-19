__author__ = 'Dani'


class NoTypeInSchemaError(BaseException):

    def __init__(self, msg):
        self.message = msg
