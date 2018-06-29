from astroquery.vo import Registry
from astropy.tests.helper import remote_data
import pytest

## To run just this test,
##
## ( cd ../../ ; python setup.py test -t astroquery/vo/tests/test_registry_remote.py --remote-data )
##

from .thetests import TestReg

## Have to decorate the TestReg with remote_data. This is the equivalent to
##   @remote_data
##   class TestReg...
##

remote_data(TestReg)


def test_query_basic():
    t = TestReg()
    t.query_basic()


def test_query_counts():
    t = TestReg()
    t.query_counts()


def test_query_timeout():
    t = TestReg()
    t.query_counts()
