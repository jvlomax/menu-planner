from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    instructions = db.Column(db.Text)
    ingredients = db.relationship("RecipeIngredient", backref="recipe")

    def __str__(self):
        return "<Recipe {}>".format(self.title)


class RecipeImage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_uri = db.Column(db.String, nullable=False)


class RecipeIngredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ingredient_id = db.Column(db.Integer, db.ForeignKey("ingredient.id"))
    ingredient = db.relationship("Ingredient")
    amount = db.Column(db.Integer)
    recipe_id = db.Column(db.Integer, db.ForeignKey("recipe.id"))

    @property
    def name(self):
        return self.ingredient.name

    def __str__(self):
        return "<RecipeIngredient {}".format(self.ingredient.name)


class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)

    def __str__(self):
        return "<Ingredient {}>".format(self.name)


class Meal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey("recipe.id"))
    recipe = db.relationship("Recipe")
    date = db.Column(db.Date)

    def __str__(self):
        return "<Meal {} for {}>".format(self.recipe, self.date)

"""
class ShoppingList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    items = db.relationship("ShoppingItem", back_populates="shoppinglist")

    def __str__(self):
        return "<Shopping List {}>".format(self.name)


class ShoppingItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    amount = db.Column(db.Integer)
    amount_notation = db.Column(db.VARCHAR, nullable=True)
    notes = db.Column(db.Text, nullable=True)

    ingredient_id = db.Column(db.Integer, db.ForeignKey("Ingredient.id"))
    ingredient = db.relationship("Ingredient")

    shoppinglist_id = db.Column(db.Integer, db.ForeignKey("ShoppingList.id"))
    shoppinglist = db.relationship("ShoppingList", back_populates="items")

    def __str__(self):
        return "<ShoppingItem {} {}>".format(" ".join([self.amount, self.amount_notation]), self.ingredient.name)
"""