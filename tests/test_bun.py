import pytest
from praktikum.bun import Bun

class TestBun:

    @pytest.mark.parametrize(
        'name, price',
        [
            ('White Bun', 100.0),
            ('Black Bun', 200.5),
            ('Red Bun', 150.75),
        ]
    )
    def test_bun_get_name_and_price(self, name, price):
        bun = Bun(name, price)

        assert bun.get_name() == name
        assert bun.get_price() == price
