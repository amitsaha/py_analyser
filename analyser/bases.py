class BaseClassCheck():

    @classmethod
    def check_violation(cls, node):
        raise NotImplementedError('Method not implemented')
    
    @classmethod
    def report_violation(cls, node, msg):
        print('{0}: Class {1}: {2}'.format(node.lineno, node.name, msg))
