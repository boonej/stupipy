import click
from stupipy import structure as struts
from stupipy import constants
from stupipy import content
from stupipy import license
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
    """Short summary.

    :param project_name: Description of parameter `project_name`.
    :type project_name: type
    :param font_name: Description of parameter `font_name`.
    :type font_name: type
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
        content.make_ascii(project_name, constants.PATH_ASCII, font_name)
        content.make_readme(
            project_name,
            constants.PATH_README,
            constants.PATH_ASCII
            )
        struts.make_testdir()
        if sphinx:
            struts.make_docs()
        if locale:
            struts.make_locales
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


base.add_command(new)
