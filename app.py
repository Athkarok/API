from flask import Flask, Blueprint
from config import ApplicationConfig
from flask_cors import CORS
from flask_mysqldb import MySQL
from flask_mail import Mail


app = Flask(__name__)
app.config.from_object(ApplicationConfig)

def register_blueprints():
    version = Blueprint("v1", __name__, url_prefix="/v1")

    # BluePrints
    from controllers.user import user_b
    from controllers.zikr import zikr_b
    from controllers.quote import quote_b
    from controllers.radio import radio_b
    from controllers.prayers import prayers_b
    from controllers.progress import progress_b
    from controllers.form import form_b
    
    version.register_blueprint(user_b)
    version.register_blueprint(zikr_b)
    version.register_blueprint(quote_b)
    version.register_blueprint(radio_b)
    version.register_blueprint(prayers_b)
    version.register_blueprint(progress_b)
    version.register_blueprint(form_b)

    app.register_blueprint(version)


with app.app_context():
    mysql = MySQL(app)
    mail = Mail(app)
    CORS(app, resources={r"/*": {"origins": "https://athkarok.me"}})

    register_blueprints()



if __name__ == "__main__":
    app.run(debug=False)
