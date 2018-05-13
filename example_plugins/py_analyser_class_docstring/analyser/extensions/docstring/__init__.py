from analyser.bases import BaseClassCheck
import ast

class CheckDocStringPresent(BaseClassCheck):

    @classmethod
    def check_violation(cls, node):
        docstring = ast.get_docstring(node)
        if not docstring:
            cls.report_violation(node, 'No docstring found in class')

class CheckDocStringLength(BaseClassCheck):

    @classmethod
    def check_violation(cls, node):
        docstring = ast.get_docstring(node)
        if docstring:
            if len(docstring) > 100:
                cls.report_violation(node, 'Docstring is greater than 100 characters')
