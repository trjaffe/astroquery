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
