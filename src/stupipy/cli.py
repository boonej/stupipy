import click
from stupipy import structure as struts
from stupipy import constants
from stupipy import content
from stupipy import license
from click import echo
from datetime import date


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
  default=True,
  help=constants.HELP_LOCALE_TEXT,
)
@click.option('--license', '-l',
              default='MIT',
              type=click.Choice([
                  'MIT',
                  'BSD',
                  'APACHE',
                  'ISC',
                  'LGPL',
                  'GPLV2',
                  'GPLV3',
                  ], case_sensitive=False))
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
    if lic == 'MIT':
        year = date.today().year
        holder = input('Enter your personal or company name.')
        content.make_license(license.mit(year, holder))


def license(lic):
    """Creates a license file based on user input.

    :param lic: Type of license.
    :type lic: String
    :return: Description of returned object.
    :rtype: type

    """
    try:
        switch(lic):
            case 'MIT':
                year = date.today().year
                holder = input('Enter your personal or company name.')
                content.make_license(license.mit(year, holder))
            case _:
                echo(f'{constants.STR_NO_LICENSE}, {lic}.')
    except Exception as ex:
        echo(f'{constants.STR_ERROR} {ex}')


base.add_command(new)
