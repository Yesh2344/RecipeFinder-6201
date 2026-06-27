import unittest
from main import app, Recipe

class TestMain(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_get_recipes(self):
        response = self.app.get('/recipes')
        self.assertEqual(response.status_code, 200)

    def test_create_recipe(self):
        response = self.app.post('/recipes', json={'name': 'Test Recipe', 'ingredients': 'Ingredient 1, Ingredient 2', 'instructions': 'Test instructions'})
        self.assertEqual(response.status_code, 200)

    def test_get_recipe(self):
        recipe = Recipe(name='Test Recipe', ingredients='Ingredient 1, Ingredient 2', instructions='Test instructions')
        db.session.add(recipe)
        db.session.commit()
        response = self.app.get(f'/recipes/{recipe.id}')
        self.assertEqual(response.status_code, 200)

    def test_update_recipe(self):
        recipe = Recipe(name='Test Recipe', ingredients='Ingredient 1, Ingredient 2', instructions='Test instructions')
        db.session.add(recipe)
        db.session.commit()
        response = self.app.put(f'/recipes/{recipe.id}', json={'name': 'Updated Recipe', 'ingredients': 'Updated Ingredient 1, Updated Ingredient 2', 'instructions': 'Updated instructions'})
        self.assertEqual(response.status_code, 200)

    def test_delete_recipe(self):
        recipe = Recipe(name='Test Recipe', ingredients='Ingredient 1, Ingredient 2', instructions='Test instructions')
        db.session.add(recipe)
        db.session.commit()
        response = self.app.delete(f'/recipes/{recipe.id}')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()