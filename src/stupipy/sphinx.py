import os


SPHINX_QUICKSTART = 'sphinx-quickstart'


def generate_base(directory):
    """Generates a base structure for Sphinx

    :param type directory: Directory to create sphinx documentation structure.

    """
    cwd = os.getcwd()
    os.chdir(directory)
    os.system(SPHINX_QUICKSTART)
    os.chdir(cwd)
