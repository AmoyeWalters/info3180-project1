from flask import Flask
<<<<<<< HEAD
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
=======
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config

db = SQLAlchemy()
>>>>>>> 894dfe9ee2c179ee44904e2f3251831aaf09e947

app = Flask(__name__)
app.config.from_object(Config)

<<<<<<< HEAD
db = SQLAlchemy(app)
migrate = Migrate(app, db)

csrf = CSRFProtect(app)

from app import views
from app import models
=======
db.init_app(app)
migrate = Migrate(app, db)

from app import views
>>>>>>> 894dfe9ee2c179ee44904e2f3251831aaf09e947
