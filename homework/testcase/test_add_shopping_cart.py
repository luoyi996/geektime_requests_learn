import pytest

from geektime_requests_learn.homework.api.add_shopping_cart import AddShoppingCart
from geektime_requests_learn.homework.model.data_stream.add_shopping_cart_params import AddShoppingCartParams


class TestAddShoppingCart:
    def setup_class(self):
        self.user = AddShoppingCart()
        self.user.clear_shopping_cart()

    def teardown_class(self):
        self.user.clear_shopping_cart()

    @pytest.mark.parametrize('add_product', [
        {'goodsId': 1130037, 'number': 2, 'productId': 189},
        {'goodsId': 1023034, 'productId': 36},
    ])
    def test_add_shopping_cart_success(self, add_product):
        """
        添加购物车成功的校验
        :param add_product:
        :return:
        """
        value = AddShoppingCartParams(**add_product)
        r = self.user.add_shopping_cart(value)
        assert r.json()['errno'] == 0
        assert r.json()['errmsg'] == '成功'
        assert (value.goodsId, value.productId) in \
               [(i['goodsId'], i['productId']) for i in self.user.get_shopping_cart_list()]

    @pytest.mark.parametrize('add_product', [
        {'goodsId': 1130037, 'number': 1, 'productId': 140},
        {'goodsId': 1023034, 'number': 1, 'productId': 68},
    ])
    def test_add_shopping_cart_fail(self, add_product):
        """
        商品id和规格id不匹配时添加购物车校验
        :param add_product:
        :return:
        """
        value = AddShoppingCartParams(**add_product)
        r = self.user.add_shopping_cart(value)
        assert (value.goodsId, value.productId) in \
               [(i['goodsId'], i['productId']) for i in self.user.get_shopping_cart_list()]
        assert r.json()['errmsg'] != "成功"
        assert r.json()['errno'] != 0

    @pytest.mark.parametrize('add_product', [
        {'goodsId': 1, 'number': 2, 'productId': 36},
        {'goodsId': 2, 'number': 1, 'productId': 36},
        {'goodsId': 13, 'number': 1, 'productId': 36},
    ])
    def test_add_had_withdrawn_shopping(self, add_product):
        """
        添加已下架商品的校验
        :param add_product:
        :return:
        """
        value = AddShoppingCartParams(**add_product)
        r = self.user.add_shopping_cart(value)
        assert r.json()['errno'] == 710
        assert r.json()['errmsg'] == '商品已下架'

    @pytest.mark.parametrize('add_product', [
        {'goodsId': '中文', 'number': 1, 'productId': 36},
        {'goodsId': "abc", 'number': 1, 'productId': 36},
        {'goodsId': 1130037, 'number': 1, 'productId': '中文'},
        {'goodsId': 1130037, 'number': 1, 'productId': 'abc'},
    ])
    def test_add__shopping_params_value_error(self, add_product):
        """
        错误的参数值的校验
        :param add_product:
        :return:
        """
        value = AddShoppingCartParams(**add_product)
        r = self.user.add_shopping_cart(value)
        assert r.json()['errno'] == 402
        assert r.json()['errmsg'] == '参数值不对'

    @pytest.mark.parametrize('add_product', [
        {'goodsId': 1130037, 'number': 0, 'productId': 36},
    ])
    def test_add_shopping_key_error(self, add_product):
        """
        添加 0 个商品的校验
        :param add_product:
        :return:
        """
        value = AddShoppingCartParams(**add_product)
        r = self.user.add_shopping_cart(value)
        assert r.json()['errno'] == 401
        assert r.json()['errmsg'] == '参数不对'

    @pytest.mark.parametrize('product_id', [
        [36],
        [189, 140, 68]
    ])
    def test_delete_shopping_success(self, product_id):
        """
        成功删除购物车商品校验
        :param product_id:
        :return:
        """
        product_count = [i['id'] for i in self.user.get_shopping_cart_list()]
        r = self.user.delete_shopping_cart(product_id)
        surplus_count = [i['id'] for i in self.user.get_shopping_cart_list()]
        assert r.json()["errno"] == 0
        assert r.json()["errmsg"] == '成功'
        assert len(product_count) == len(surplus_count) + len(product_id)

    @pytest.mark.parametrize('product_id', [
        [1],
        [12, 2, 4],
        [''],
        [' ']
    ])
    def test_delete_shopping_fail(self, product_id):
        """
        删除购物车商品失败的校验
        :param product_id:
        :return:
        """
        product_count = [i['id'] for i in self.user.get_shopping_cart_list()]
        r = self.user.delete_shopping_cart(product_id)
        surplus_count = [i['id'] for i in self.user.get_shopping_cart_list()]
        assert r.json()["errno"] == 0
        assert r.json()["errmsg"] == '成功'
        assert len(product_count) == len(surplus_count)

    # @pytest.mark.parametrize('product_id', [
    #
    # ])
    # def test_delete_shopping_error401(self, product_id):
    #     """
    #     参数错误校验
    #     :param product_id:
    #     :return:
    #     """
    #     r = self.user.delete_shopping_cart(product_id)
    #     print(r.json())
    #     assert r.json()["errno"] == 401
    #     assert r.json()["errmsg"] == '参数不对'

    @pytest.mark.parametrize('product_id', [
        ['a'], ['中文'], ['%$#@^']
    ])
    def test_delete_shopping_error402(self, product_id):
        """
        参数值错误校验
        :param product_id:
        :return:
        """
        r = self.user.delete_shopping_cart(product_id)
        print(r.json())
        assert r.json()["errno"] == 402
        assert r.json()["errmsg"] == '参数值不对'
