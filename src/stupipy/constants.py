import gettext

_ = gettext.gettext

PATH_SRC = 'src'
PATH_TESTS = 'src/tests'
PATH_LOCALES = 'src/locales'
PATH_DOCS = 'docs'
PATH_README = 'README.rst'
PATH_ASCII = 'PROJ_ASCII.txt'

FILE_INIT = '__init__.py'

STR_FOLDER_EXISTS = _('Folder exists at')
STR_ERROR = _('Error:')
STR_ENTER_NAME = _('Enter your personal or company name.')
STR_NO_LICENSE = _('No license matches your input:')
STR_INVALID_LICENSE = _('is not a valid input for license type.')

HELP_PNAME_TEXT = _('Project name to create.')
HELP_FONT_TEXT = _('Name of pyfiglet font to use for header.')
HELP_SPHINX_TEXT = _('Creates base structure for sphinx documentation.')
HELP_LOCALE_TEXT = _('Creates base structure for localization.')
