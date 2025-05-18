import pytest
from unittest.mock import Mock
from praktikum.burger import Burger

@pytest.fixture
def setup_burger():
    burger = Burger()

    bun = Mock()
    bun.get_name.return_value = 'Булочка'
    bun.get_price.return_value = 100
    burger.set_buns(bun)

    return burger