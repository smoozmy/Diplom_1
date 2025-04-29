import pytest
from praktikum.ingredient import Ingredient

class TestIngridient:

    @pytest.mark.parametrize(
        'ingredient_type, name, price',
        [
            ('sauce', 'Ketchup', 50.0),
            ('filling', 'Beef Patty', 200.0),
            ('sauce', 'Mustard', 30.5),
        ]
    )
    def test_ingredient_getters(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)

        assert ingredient.get_type() == ingredient_type
        assert ingredient.get_name() == name
        assert ingredient.get_price() == price
