from flask import Flask, request, jsonify
from database import init_db, create_tables
from models import Recipe

app = Flask(__name__)
init_db(app)
create_tables(app)

@app.route('/recipes', methods=['GET'])
def get_recipes():
    recipes = Recipe.query.all()
    return jsonify([recipe.to_dict() for recipe in recipes])

@app.route('/recipes', methods=['POST'])
def create_recipe():
    recipe = Recipe(
        name=request.json['name'],
        ingredients=request.json['ingredients'],
        instructions=request.json['instructions']
    )
    db.session.add(recipe)
    db.session.commit()
    return jsonify(recipe.to_dict())

@app.route('/recipes/<int:id>', methods=['GET'])
def get_recipe(id):
    recipe = Recipe.query.get(id)
    if recipe is None:
        return jsonify({'error': 'Recipe not found'}), 404
    return jsonify(recipe.to_dict())

@app.route('/recipes/<int:id>', methods=['PUT'])
def update_recipe(id):
    recipe = Recipe.query.get(id)
    if recipe is None:
        return jsonify({'error': 'Recipe not found'}), 404
    recipe.name = request.json['name']
    recipe.ingredients = request.json['ingredients']
    recipe.instructions = request.json['instructions']
    db.session.commit()
    return jsonify(recipe.to_dict())

@app.route('/recipes/<int:id>', methods=['DELETE'])
def delete_recipe(id):
    recipe = Recipe.query.get(id)
    if recipe is None:
        return jsonify({'error': 'Recipe not found'}), 404
    db.session.delete(recipe)
    db.session.commit()
    return jsonify({'message': 'Recipe deleted'})

if __name__ == '__main__':
    app.run(debug=True)