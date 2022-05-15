import stupipy.structure as struct
import os
from os import makedirs, path
from stupipy import constants
from pytest import fail
from shutil import rmtree

TESTPATH = 'stupidtestpath'
TESTDIR = 'dirdir'


def mkachgtestdir():
    global TESTPATH

    if path.exists(TESTPATH):
        rmtree(TESTPATH)

    makedirs(TESTPATH)


def test_make_testdir():
    mkachgtestdir()
    os.chdir(TESTPATH)
    try:
        struct.make_testdir()
    except Exception as ex:
        os.chdir('..')
        rmtree(TESTPATH)
        fail(f'make_testdir() raised exception: {ex}')
        return
    finally:
        if not path.exists(constants.PATH_TESTS):
            os.chdir('..')
            if (path.exists(TESTPATH)):
                rmtree(TESTPATH)
            fail(f'failed to create {constants.PATH_TESTS}.')
        else:
            os.chdir('..')
            rmtree(TESTPATH)


def test_fail_make_testdir():
    mkachgtestdir()
    os.chdir(TESTPATH)
    makedirs(constants.PATH_TESTS)

    try:
        struct.make_testdir()
    except Exception as ex:
        print(f'make_testdir() returned: {ex}')
        os.chdir('..')
        rmtree(TESTPATH)
    else:
        os.chdir('..')
        rmtree(TESTPATH)
        fail(
            'make_testdir() attempted to create directory while directory'
            + ' present.'
        )


def test_make_locales():
    mkachgtestdir()
    os.chdir(TESTPATH)
    try:
        struct.make_locales()()
    except Exception as ex:
        os.chdir('..')
        if (path.exists(TESTPATH)):
            rmtree(TESTPATH)
        else:
            rmtree(TESTPATH)
            fail(f'make_testdir() raised exception: {ex}')
        return


def test_fail_make_locales():
    mkachgtestdir()
    os.chdir(TESTPATH)
    makedirs(constants.PATH_LOCALES)

    try:
        struct.make_locales()
    except Exception as ex:
        os.chdir('..')
        print(f'make_testdir() returned: {ex}')
        rmtree(TESTPATH)
    else:
        os.chdir('..')
        rmtree(TESTPATH)
        fail(
            'make_testdir() attempted to create directory while directory'
            + ' present.'
        )
