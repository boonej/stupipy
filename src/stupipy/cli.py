import click
from stupipy import structure as struts
from stupipy import constants
from stupipy import content
from stupipy import license
from stupipy import documentation
from click import echo
from datetime import date

valid_licenses = [
    'MIT',
    'BSD',
    'APACHE',
    'ISC',
    'WTFPL',
    ]


@click.group()
def base():
    pass


@click.command()
@click.option(
    '--project-name', '-p',
    help=constants.HELP_PNAME_TEXT,
)
@click.option(
    '--font_name', '-f',
    help=constants.HELP_FONT_TEXT,
    default='slant',
)
def readme(project_name, font_name='slant'):
    """Generates README file.

    :param type project_name: Name of the project.
    :param type font_name: ASCII text font name, should comply with available\
        fonts in pyfiglet.

    """
    try:
        content.make_ascii(project_name, constants.PATH_ASCII, font_name)
        content.make_readme(
            project_name,
            constants.PATH_README,
            constants.PATH_ASCII
            )
    except Exception as ex:
        echo(f'{constants.STR_ERROR} {ex}')


def tests():
    """Creates basic test directory

    """
    struts.make_dir(constants.PATH_TESTS)
    content.make_init(constants.PATH_TESTS)


def docs():
    """Generates base documentation structure.

    """
    try:
        struts.make_dir(constants.PATH_DOCS)
        documentation.generate_base(constants.PATH_DOCS)
    except Exception as ex:
        echo(f'{constants.STR_ERROR} {ex}')


@click.command()
@click.option('--licensename', '-l',
              default='MIT',
              type=click.Choice(
                  valid_licenses,
                  case_sensitive=False))
def make_license(licensename):
    """Generates a license file for a project.

    :param type licensename: Type of license to generate.

    """
    try:
        if licensename not in valid_licenses:
            raise Exception(f'{licensename} {constants.STR_INVALID_LICENSE}')
        year = date.today().year
        holder = input(f'{constants.STR_ENTER_NAME}\n')
        lic_string = ''
        match licensename:
            case 'MIT':
                lic_string = license.mit(year, holder)
            case 'BSD':
                lic_string = license.bsd(year, holder)
            case 'APACHE':
                lic_string = license.apache(year, holder)
            case 'ISC':
                lic_string = license.isc(year, holder)
            case 'WTFPL':
                lic_string = license.wtfpl(year, holder)
            case _:
                raise Exception(f'{constants.STR_NO_LICENSE}, {licensename}.')
        content.make_license(lic_string)
    except Exception as ex:
        echo(f'{constants.STR_ERROR} {ex}')


@click.command()
@click.option(
    '--project_name',
    '-p',
    help=constants.HELP_PNAME_TEXT,
)
@click.option(
    '--font_name', '-f',
    help=constants.HELP_FONT_TEXT,
    default='slant',
)
@click.option(
  '--sphinx/--no-sphinx',
  default=True,
  help=constants.HELP_SPHINX_TEXT,
)
@click.option(
  '--locale/--no-locale',
  default=False,
  help=constants.HELP_LOCALE_TEXT,
)
@click.option('--licensename', '-l',
              default='MIT',
              type=click.Choice(
                  valid_licenses,
                  case_sensitive=False))
def new(project_name, font_name, sphinx, locale, licensename):
    """Creates a new project with all the trimmings.

    :param project_name: Name of project.
    :type project_name: String
    :param font_name: 'Font' for ASCII art in README.
    :type font_name: String
    :param sphinx: Description of parameter `sphinx`.
    :type sphinx: type
    :param locale: Description of parameter `locale`.
    :type locale: type
    :param lic: Description of parameter `lic`.
    :type lic: type

    """
    global valid_licenses
    try:
        if not project_name:
            raise Exception(f'{constants.STR_NO_PROJECT}')
        struts.make_proj_dir(project_name)

        struts.make_dir(project_name)
        content.make_init(project_name)
        tests()
        struts.make_dir(constants.PATH_LOCALES)
    except Exception as ex:
        echo(f'{constants.STR_ERROR} {ex}')
    readme(project_name, font_name)
    if sphinx:
        docs()
    make_license(licensename)


base.add_command(readme)
base.add_command(new)
