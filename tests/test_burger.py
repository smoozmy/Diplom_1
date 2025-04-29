import pytest
from unittest.mock import Mock

class TestBurger:
    def test_set_buns(self, setup_burger):
        assert setup_burger.bun.get_name() == 'Булочка', 'Булка не установилась'

    def test_add_ingredient(self,setup_burger):
        ingredient = Mock()
        ingredient.get_name.return_value = 'Котлета'
        setup_burger.add_ingredient(ingredient)

        assert setup_burger.ingredients[0].get_name() == 'Котлета', 'Ингредиент не добавился'

    def test_remove_ingredient(self, setup_burger):
        ingredient1 = Mock()
        ingredient1.get_name.return_value = 'Котлета'
        ingredient2 = Mock()
        ingredient2.get_name.return_value = 'Соус'

        setup_burger.add_ingredient(ingredient1)
        setup_burger.add_ingredient(ingredient2)

        setup_burger.remove_ingredient(0)

        assert setup_burger.ingredients[0].get_name() == 'Соус', 'Ингредиент не удалился'

    def test_move_ingredient(self, setup_burger):
        ingredient1 = Mock()
        ingredient1.get_name.return_value = 'Котлета'
        ingredient2 = Mock()
        ingredient2.get_name.return_value = 'Соус'

        setup_burger.add_ingredient(ingredient1)
        setup_burger.add_ingredient(ingredient2)

        setup_burger.move_ingredient(0, 1)

        assert setup_burger.ingredients[0].get_name() == 'Соус', 'Ингредиенты не поменялись местами'
        assert setup_burger.ingredients[1].get_name() == 'Котлета', 'Ингредиенты не поменялись местами'

    def test_get_price(self, setup_burger):
        ingredient1 = Mock()
        ingredient1.get_price.return_value = 500
        ingredient2 = Mock()
        ingredient2.get_price.return_value = 10

        setup_burger.add_ingredient(ingredient1)
        setup_burger.add_ingredient(ingredient2)

        expected_price = setup_burger.bun.get_price() * 2 + 500 + 10

        assert setup_burger.get_price() == expected_price

    def test_get_receipt(self, setup_burger):
        ingredient1 = Mock()
        ingredient1.get_name.return_value = 'Котлета'
        ingredient1.get_type.return_value = 'Filling'
        ingredient1.get_price.return_value = 500

        ingredient2 = Mock()
        ingredient2.get_name.return_value = 'Соус'
        ingredient2.get_type.return_value = 'Sauce'
        ingredient2.get_price.return_value = 10

        setup_burger.add_ingredient(ingredient1)
        setup_burger.add_ingredient(ingredient2)

        receipt = setup_burger.get_receipt()

        assert 'Булочка' in receipt
        assert '= filling Котлета =' in receipt
        assert '= sauce Соус =' in receipt
        assert f'Price: {setup_burger.get_price()}' in receipt
