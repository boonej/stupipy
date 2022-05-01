::

             __              _
       _____/ /___  ______  (_)___  __  __
      / ___/ __/ / / / __ \/ / __ \/ / / /
     (__  ) /_/ /_/ / /_/ / / /_/ / /_/ /
    /____/\__/\__,_/ .___/_/ .___/\__, /
                  /_/     /_/    /____/


stupipy
###############################################################################

.. note::
  Full disclosure: this project was an exercise. I wanted to get a feel for a
  few features of python that I have not used to this point: notably
  localization.

This project was intended to provide a useful function while I learned
something new. *Stupipy* generates a project structure that fits my coding
style standards.


Installation
-------------------------------------------------------------------------------

To install stupipy, execute:

.. code-block:: console

  pip install stupipy


Usage
-------------------------------------------------------------------------------

You only need a name for your project to get started. Create a no-frills
folder structure by executing:

.. code-block:: console

  stupipy -p mysweetproject

A folder structure will be created with all the files required to distribute
your project to pypi. If you have additional needs, stupipy supports the
following options:

Font Name
```````````

`--font_name -f`
  Specifies the *font* for the ASCII art generated for files. See pyfiglet's
  documentation for available fonts.
