import pytest
from geektime_requests_learn.PetHospital.api.owner_data import Owner
from geektime_requests_learn.PetHospital.api.owners import OwnersMethod
from geektime_requests_learn.PetHospital.utils.log import log


class TestOwnersAdd:
    def setup_class(self):
        """
        __init__公共数据
        在执行 case 之前清除影响 case 的数据
        """
        self.add = OwnersMethod()
        self.add.clear('geek')

    def setup(self):
        """加载每次都需要的数据"""

    def teardown(self):
        """清除每次setup加载的数据"""

    def teardown_class(self):
        self.add.clear('geek')
        """清除数据"""

    @pytest.mark.parametrize('owners', [
        {'telephone': '1234567911', 'city': 'ShenZhen'},
        {'telephone': '123456', 'city': '1'},
        {'telephone': '1234567911', 'city': '11'}
    ])
    def test_add_success(self, owners):
        """测试添加成功的case"""

        owner = Owner(**owners)
        owner.lastName = 'geek'
        owner.firstName = 'My'
        owner.address = 'NanShan'
        r = self.add.add(owner)
        log().debug(f'{self.test_add_success.__doc__}-添加的宠物信息为：{r.json()}')
        assert r.status_code == 201

    @pytest.mark.parametrize('owners', [
        {'telephone': '1234567911', 'firstName': ''},
        {'telephone': '1234567911', 'firstName': '11'},
        {'telephone': '', 'firstName': '1a'},
        {'telephone': 'asdfqw', 'firstName': 'fffff'},
    ])
    def test_add_fail(self, owners):
        """测试添加失败的case"""
        owner = Owner(**owners)
        owner.lastName = 'geek'
        owner.city = 'ShenZhen'
        owner.address = 'NanShan'
        log().debug(f'{self.test_add_fail.__doc__}-测试数据为：{owner}')
        r = self.add.add(owner)
        assert r.status_code != 201
