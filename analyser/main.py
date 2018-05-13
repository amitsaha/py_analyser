import ast
import sys
import string
import inspect

from analyser.bases import BaseClassCheck
from straight.plugin import load

plugins = load('analyser.extensions', subclasses=BaseClassCheck)

def check_class(node):
    # The call() function yields a function object
    # http://straightplugin.readthedocs.io/en/latest/api.html#straight.plugin.manager.PluginManager.call
    # Not sure why..
    for p in plugins.call('check_violation', node):
        if p:
            p()

def analyse(file_path):
    with open(file_path) as f:
        root = ast.parse(f.read())
        for node in ast.walk(root):
            if isinstance(node, ast.ClassDef):
                check_class(node)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit('Usage: main.py <file path>')
    analyse(sys.argv[1])
