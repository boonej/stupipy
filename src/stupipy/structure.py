from os import makedirs, path, chdir
from stupipy import constants


def make_dir(dir):
    """Creates a directory at a relative path. An exception is thrown if a
    directory is present.

    :param dir: directory to create
    :type dir: String
    """
    if path.exists(dir):
        raise Exception(f'{constants.STR_FOLDER_EXISTS} {dir}.')
    makedirs(dir)


def make_proj_dir(project_name):
    """Creates base project dirctory.

    :param project_name: Name of project.
    :type project_name: String

    """
    try:
        make_dir(project_name)
    finally:
        chdir(project_name)
        
