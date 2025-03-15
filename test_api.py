from common.logger_utils import log
import pytest


class TestApi:
    @pytest.fixture(params=[1,2,3,4,5], ids=['a+','b','c','d','e'], scope='function')
    def context(self, request):
        return request.param

    def test_run(self, context):
        var = 998

        log.info("test")
        log.info("test")
        log.info("test")

        log.info(context)

    def test_lay(self, context):
        pass