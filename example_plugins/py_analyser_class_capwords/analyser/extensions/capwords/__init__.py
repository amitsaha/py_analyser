from analyser.bases import BaseClassCheck
import string

class CheckCapwords(BaseClassCheck):

    @classmethod
    def check_violation(cls, node):
        if string.capwords(node.name) != node.name:
            cls.report_violation(node, 'Class name not in CapWords')
