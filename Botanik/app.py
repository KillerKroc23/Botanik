from flask import Flask

from config import Config
from Controllers.controller import main_bp
from Models.models import db

app = Flask(__name__)
app.config.from_object(Config)
#Initialize the database
db.init_app(app)

#Register Blueprints

app.register_blueprint(main_bp)

@app.before_request
def create_tables():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)