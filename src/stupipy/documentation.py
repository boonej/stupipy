import os


SPHINX_QUICKSTART = 'sphinx-quickstart'


def generate_base(directory, project_name, author, version, language):
    """Generates vanilla documentation directory.


    :param type directory: Documentation directory.
    :param type project_name: Name of project.
    :param type author: Author or company name/contact.
    :param type version: Version number.
    :param type language: Language code..

    """
    cwd = os.getcwd()
    os.chdir(directory)
    cmd = f'{SPHINX_QUICKSTART} -p {project_name} -a "{author}"\
      -v {version} -l {language}'
    os.system(cmd)
    os.chdir(cwd)
