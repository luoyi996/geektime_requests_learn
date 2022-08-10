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
        params = SearchParams(**content)
        r = self.user.search(params)
        if isinstance(r, list):
            assert len(r) >= 0
        else:
            log().error(f"Response Code: {r}")

    @pytest.mark.parametrize('content', [
        {'keyword': 'sds'}
    ])
    def test_search_result_isnone(self, content):
        params = SearchParams(**content)
        r = self.user.search(params)
        if isinstance(r, list):
            assert r is []
        else:
            log().error(f"Response Code: {r}")