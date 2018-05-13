# This is a test Python module
class hello:
    """ This is a class """
    def __init__(self):
        print('Hello World')

class Nodocstring:
    pass

class Alongdocstring:
    """ This is a long docstring. It is greater than 100 characters
        and will be caught. If not, the analyser is broken
    """
