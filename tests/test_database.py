from praktikum.database import Database

class TestDatabase:

    def test_available_buns_structure(self):
        db = Database()
        buns = db.available_buns()

        assert isinstance(buns, list)
        assert len(buns) == 3

        for bun in buns:
            assert hasattr(bun, 'get_name')
            assert hasattr(bun, 'get_price')

    def test_available_ingredients_structure(self):
        db = Database()
        ingredients = db.available_ingredients()

        assert isinstance(ingredients, list)
        assert len(ingredients) == 6

        for ingredient in ingredients:
            assert hasattr(ingredient, 'get_name')
            assert hasattr(ingredient, 'get_type')
            assert hasattr(ingredient, 'get_price')

    def test_bun_names(self):
        db = Database()
        buns = db.available_buns()
        names = []

        for bun in buns:
            names.append(bun.get_name())

        assert names == ['black bun', 'white bun', 'red bun']

    def test_ingredient_names(self):
        db = Database()
        ingredients = db.available_ingredients()
        names = []

        for ingredient in ingredients:
            names.append(ingredient.get_name())

        assert names == [
            'hot sauce',
            'sour cream',
            'chili sauce',
            'cutlet',
            'dinosaur',
            'sausage'
        ]
