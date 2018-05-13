import nox

@nox.session
@nox.parametrize('python_version', ['3.6'])
def human_testing(session, python_version):
    session.interpreter = 'python' + python_version
    session.run('pip', 'install', '.')
    session.run('pip', 'install', './example_plugins/py_analyser_class_capwords/')
    session.run('pip', 'install', './example_plugins/py_analyser_class_docstring/')
    session.run('python', 'analyser/main.py', './module_under_test.py')
