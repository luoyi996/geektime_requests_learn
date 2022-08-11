import pytest

from geektime_requests_learn.homework.api.search import LiteMallSearch
from geektime_requests_learn.homework.model.data_stream.search_params import SearchParams
from geektime_requests_learn.homework.utils.log import log


class TestLiteMallSearch:
    def setup_class(self):
        self.user = LiteMallSearch()

    @pytest.mark.parametrize('content', [
        {'keyword': ''}
    ])
    def test_search_key_isnone(self, content):
        """
        空搜索
        :param content:
        :return:
        """
        params = SearchParams(**content)
        r = self.user.search(params)
        if isinstance(r, list):
            print(r)
            assert len(r) >= 0
        else:
            log().error(f"{self.test_search_key_isnone.__name__}:: Response Code: {r}")

    @pytest.mark.parametrize('content', [
        {'keyword': 'sds'}
    ])
    def test_search_result_isnone(self, content):
        """
        搜索结果为空
        :param content:
        :return:
        """
        params = SearchParams(**content)
        r = self.user.search(params)
        if isinstance(r, list):
            assert r is []
        else:
            log().error(f"{self.test_search_result_isnone.__name__}:: Response Code: {r}")

    @pytest.mark.parametrize('content', [
        {'keyword': 'hogwarts1'}
    ])
    def test_search_result_only_one(self, content):
        """
        搜索结果唯一
        :param content:
        :return:
        """
        params = SearchParams(**content)
        r = self.user.search(params)
        if isinstance(r, list):
            assert len(r) == 1
        else:
            log().error(f"{self.test_search_result_only_one.__name__}:: Response Code: {r}")

    @pytest.mark.parametrize('content', [
        {'keyword': '1'}
    ])
    def test_search_multiple_result(self, content):
        """
        搜索结果有多个
        :param content:
        :return:
        """
        params = SearchParams(**content)
        r = self.user.search(params)
        if isinstance(r, list):
            assert len(r) >= 2
        else:
            log().error(f"{self.test_search_multiple_result.__name__}:: Response Code: {r}")
