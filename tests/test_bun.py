import pytest
from praktikum.bun import Bun

class TestBun:

    @pytest.mark.parametrize('name', ['Булочка', 'Чёрная булка', 'Булка с кунжутом'])
    def test_get_name(self, name):
        bun = Bun(name, 100.0)
        assert bun.get_name() == name

    @pytest.mark.parametrize('price', [0.0, 50.5, 199.99])
    def test_get_price(self, price):
        bun = Bun('Булочка', price)
        assert bun.get_price() == price
