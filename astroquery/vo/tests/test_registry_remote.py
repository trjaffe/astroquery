from astroquery.vo import Registry
from astropy.tests.helper import remote_data
import pytest

## To run just this test,
##
## ( cd ../../ ; python setup.py test -t astroquery/vo/tests/test_registry_remote.py --remote-data )
##


# Find all SIA services from HEASARC.
@remote_data
class TestReg(object):
    def test_basic(self):
        # Find all SIA services from HEASARC.
        heasarc_image_services = Registry.query(source='heasarc',
                                                service_type='image')
        assert(len(heasarc_image_services) >= 108)

    def test_adql_service(self):
        query = Registry._build_adql(service_type="image")
        assert("cap_type like '%simpleimageaccess%'" in query)

    def test_adql_keyword(self):
        query = Registry._build_adql(keyword="foobar", service_type="image")
        assert "res_description like '%foobar%'" in query

    def test_adql_waveband(self):
        query = Registry._build_adql(waveband='foobar', service_type="image")
        assert "waveband like '%foobar%'" in query

    def test_adql_source(self):
        query = Registry._build_adql(source='foobar', service_type="image")
        assert "ivoid like '%foobar%'" in query

    def test_adql_publisher(self):
        query = Registry._build_adql(publisher='foobar', service_type="image")
        assert "role_name like '%foobar%'" in query

    def test_adql_orderby(self):
        query = Registry._build_adql(order_by="foobar", service_type="image")
        assert "order by foobar" in query

    def test_query_counts(self):
        aptable = Registry.query_counts('publisher', 15, verbose=True)
        assert aptable[0][1] > 17000

    def test_timeout(self):
        from requests.exceptions import (Timeout, ReadTimeout)
        myReg = Registry()
        myReg._TIMEOUT = 0.1
        try:
            heasarc_image_services = myReg.query(source='heasarc', service_type='image')
        except (Timeout, ReadTimeout, ConnectionError):
            pass
        except Exception as e:
            pytest.fail("Did not get the expected timeout exception but {}".format(e))
        else:
            pytest.fail("Did not get the expected timeout exception but none")
