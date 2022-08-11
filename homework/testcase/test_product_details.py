import pytest

from geektime_requests_learn.homework.api.product_details import ProductList


class TestProductDetails:
    def setup_class(self):
        self.user = ProductList()
        ...

    @pytest.mark.parametrize('product_id', [1046044, 1181380])
    def test_get_product_list_success(self, product_id):
        """
        正确的商品 id 检查
        :param product_id:
        :return:
        """
        r = self.user.details(product_id)
        assert r.json()["errno"] == 0
        assert product_id in [j['goodsId'] for i in r.json()['data']['specificationList'] for j in i['valueList']]

    @pytest.mark.parametrize('product_id', ['a', "中文", '$$'])
    def test_get_product_error402(self, product_id):
        """
        错误的 id 类型
        :param product_id:
        :return:
        """
        r = self.user.details(product_id)
        assert r.json()["errno"] == 402
        assert r.json()["errmsg"] == '参数值不对'

    @pytest.mark.parametrize('product_id', [2046044])
    def test_get_product_fail(self, product_id):
        """
        不存在的 id 检查
        :param product_id:
        :return:
        """
        r = self.user.details(product_id)
        assert r.json()["errno"] == 502
        assert r.json()["errmsg"] == '系统内部错误'

    @pytest.mark.parametrize('product_id', [''])
    def test_get_product_key_isnone(self, product_id):
        """
        空值检查
        :param product_id:
        :return:
        """
        r = self.user.details(product_id)
        assert r.json()["errno"] == 402
        assert r.json()["errmsg"] == 'arg1must not be null'
