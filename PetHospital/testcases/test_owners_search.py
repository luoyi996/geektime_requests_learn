import pytest

from geektime_requests_learn.PetHospital.api.owners import OwnersMethod
from geektime_requests_learn.PetHospital.utils.log import log


class TestOwnersAdd:
    def setup_class(self):
        """__init__公共数据"""
        self.list = OwnersMethod()
        ...

    def setup(self):
        """加载每次都需要的数据"""
        ...

    def teardown(self):
        """清除每次setup加载的数据"""
        ...

    def teardown_class(self):
        """清除数据"""
        ...

    def test_search_value_isnone(self):
        """测试搜索结果为空的case"""
        r = self.list.search('yi')
        log().debug(f'{self.test_search_value_isnone.__doc__} - 查询结果为：{r}')
        assert len(r) == 0

    def test_search_key_isnone(self):
        """测试搜索值为空的case"""
        r = self.list.search('')
        log().debug(f'{self.test_search_key_isnone.__doc__} - 查询结果为：{r}')
        assert len(r) > 0

    def test_search_value_only_one(self):
        """测试搜索结果只有一个的case"""
        r = self.list.search('McTavish')
        log().debug(f'{self.test_search_value_only_one.__doc__} - 查询结果为：{r}')
        assert len(r) == 1

    def test_search_multiple_values(self):
        """测试搜索结果有多个值的case"""
        r = self.list.search('davis')
        log().debug(f'{self.test_search_multiple_values.__doc__} - 查询结果为：{r}')
        assert len(r) >= 2

    @pytest.mark.parametrize('list_id', [1, 2, 3, 4, 10])
    def test_search_pet_master_success(self, list_id):
        """测试搜索宠物主人成功的case"""
        r = self.list.get_pet_master(list_id)
        log().debug(f"{self.test_search_pet_master_success.__doc__} - 宠物'id={list_id}'的主人是：{r}")

    @pytest.mark.parametrize('list_id', [None])
    def test_search_pet_master_fail(self, list_id):
        """测试搜索宠物主人失败的case"""
        r = self.list.get_pet_master(list_id)
        code = r.status_code
        print(r.json())
        print(code)
        if code == 400:
            assert r.json()["error"] == "Bad Request"
            assert r.json()["status"] == 400
            log().debug(f"{self.test_search_pet_master_fail.__doc__} - Bad request，response code：{code}")
        # elif code ==404:
        #     assert r.json()["error"] == "Bad Request"
        #     assert r.json()["status"] == 400
        #     log().debug(f"{self.test_search_pet_master_fail.__doc__} - Owner not found，response code：{code}")
        # elif code == 500:
        #     assert r.json()["error"] == "Bad Request"
        #     assert r.json()["status"] == 400
        #     log().debug(f"{self.test_search_pet_master_fail.__doc__} - Server error，response code：{code}")
        # else:
        #     ...

