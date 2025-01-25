from common.logger import log
import pytest
from common.excel_utils import merge_cells, style_cells, format_cells, style_header


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
        file = "data/搜索指标DIFF报告示范.xlsx"
        style_header(file, font_size=12)
        merge_cells(file, "字段路径", "综搜-相似度")
        merge_cells(file, "相似")
        style_cells(file, "数量", bg_color='FF0000', condition=lambda value: value >= 30)
        format_cells(file, "请求占比", "0.0%")
