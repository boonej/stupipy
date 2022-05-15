import pyfiglet
import os


def make_ascii(project_name, temp_name, fontname='slant'):
    """Creates a file with the content and font provided.

    :param project_name: Name of project - will be converted to ASCII art.
    :type project_name: String
    :param temp_name: Name of temporary file to save.
    :type temp_name: String
    :param fontname: Font style to convert text to. See the pyfiglet\
        documentation for additional information. Defaults to 'slant'.
    :type fontname: String

    """
    with open(temp_name, 'w') as file:
        file.write(pyfiglet.figlet_format(project_name, font=fontname))


def make_readme(project_name, readme_path, tempfile_path):
    """Creates a readme file at specified path with a header in a temporary
    file.

    :param project_name: Name of project.
    :type project_name: String
    :param readme_path: Path to README file.
    :type readme_path: String
    :param tempfile_path: Path to temorary file holding header.
    :type tempfile_path: String

    """
    with open(readme_path, 'w') as file:
        file.write('::\n\n')
        temp_file = open(tempfile_path, 'r')
        lines = temp_file.readlines()

        for line in lines:
            file.write(f'    {line}')

        file.write(f'\n\n{project_name}\n')
        file.write('#' * 79)
        file.write('\n\n')
    try:
        os.remove(tempfile_path)
    except Exception as ex:
        raise Exception(f'{ex} {tempfile_path}.')


def make_license(license):
    """Creates a license file from string input.

    :param license: Contents of license file.
    :type license: String

    """
    lines = license.split('\n')
    with open('LICENSE.rst', 'w') as file:
        for line in lines:
            file.write(f'        {line}\n')


def make_init(directory):
    """Generates an empty init file.

    :param type directory: Path to generate init file.

    """
    with open(os.path.join(directory, '__init__.py'), 'w') as file:
        file.write('# Silence is compliance.\n\n')
