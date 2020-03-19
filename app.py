from flask import Flask, render_template, redirect

from flask_restless import APIManager
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from forms import RecipeForm
from models import db, Recipe, RecipeIngredient, Ingredient

def create_app():
    app = Flask(__name__)
    app.config["DEBUG"] = True
    app.config["SECRET_KEY"] = "My secret key"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.db"

    # set optional bootswatch theme
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    db.init_app(app)
    return app

app = create_app()
app.app_context().push()

admin = Admin(app, name='microblog', template_mode='bootstrap3')
# Add administrative views here


db.create_all()
admin.add_view(ModelView(Recipe, db.session))
admin.add_view(ModelView(RecipeIngredient, db.session))
admin.add_view(ModelView(Ingredient, db.session))
#manager = APIManager(app, flask_sqlalchemy_db=db)
#manager.create_api(Recipe, methods=["GET", "POST", "PUT", "DELETE"])


@app.route('/')
def hello_world():
    return recipes()


@app.route('/recipes', methods=["GET"])
def recipes():

    recipes = Recipe.query.all()
    context = {"recipes": recipes}
    print(context)
    return render_template("recipe-list.html", recipes=recipes)


@app.route("/recipe/create", methods=["GET", "POST"])
def create_recipe():
    form = RecipeForm()
    if form.validate_on_submit():

        return redirect("/recipes")
    return render_template("recipe-create.html", form=form)


@app.route("/recipe/<recipe_id>")
def recipe(recipe_id):
    print(recipe_id)
    recipe = Recipe.query.filter_by(id=recipe_id).first()
    print(recipe)
    return render_template("recipe.html", recipe=recipe)


@app.route("/menu")
def menu():
    return render_template("menu.html")


if __name__ == '__main__':
    app.run()
