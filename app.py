from flask import Flask
import json


# blueprints' import
from main.main_views import main_blueprint
from search.search_views import search_blueprint
from api.api import api

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False

# blueprints' register
app.register_blueprint(main_blueprint)
app.register_blueprint(search_blueprint)
app.register_blueprint(api)


# errorhandlers
@app.errorhandler(404)
def page_not_found(e):
    return 'Страница не найдена'


@app.errorhandler(500)
def internal_server_error(e):
    return 'На сервере что-то пошло не так('


if __name__ == "__main__":
    app.run()


