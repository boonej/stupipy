import click
from stupipy import structure as struts
from stupipy import constants
from stupipy import content
from stupipy import licenses
from click import echo
from datetime import date

valid_licenses = [
    'MIT',
    'BSD',
    'APACHE',
    'ISC',
    'LGPL',
    'GPLV2',
    'GPLV3',
    ]


@click.group()
def base():
    pass


@click.command()
@click.option(
    '--license', '-l',
    help=constants.HELP_LICENSE_TEXT,
    default='MIT',
    type=click.Choice(
        valid_licenses,
        case_sensitive=False
        )
    )
def writelicense(lic):
    """Creates a license file based on user input. Accepted license values are:
        * MIT
        * BSD
        * APACHE
        * ISC
        * LGPL
        * GPLV2
        * GPLV3

    :param lic: Type of license.
    :type lic: String

    """
    global valid_licenses
    try:
        if lic not in valid_licenses:
            raise Exception(f'{lic} {constants.STR_INVALID_LICENSE}')
        year = date.today().year
        holder = input(f'{constants.STR_ENTER_NAME}\n')
        lic_string = ''
        match lic:
            case 'MIT':
                lic_string = license.mit(year, holder)
            case _:
                raise Exception(f'{constants.STR_NO_LICENSE}, {lic}.')
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
  default=True,
  help=constants.HELP_LOCALE_TEXT,
)
@click.option('--license', '-l',
              default='MIT',
              type=click.Choice(
                  valid_licenses,
                  case_sensitive=False))
def new(project_name, font_name, sphinx, locale, lic):
    try:
        struts.make_proj_dir(project_name)
        content.make_ascii(project_name, constants.PATH_ASCII, font_name)
        struts.make_testdir()
        if sphinx:
            struts.make_docs()
        if locale:
            struts.make_locales()
    except Exception as ex:
        echo(f'{constants.STR_ERROR} {ex}')
    writelicense(lic)


base.add_command(new)
base.add_command(writelicense)
