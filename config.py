import os

class ApplicationConfig:
    SECRET_KEY = os.environ.get('APP_SECRET_KEY')

    # Database Config
    MYSQL_HOST = os.environ.get('DB_HOST')
    MYSQL_USER = os.environ.get('DB_USER')
    MYSQL_PASSWORD = os.environ.get('DB_PASSWORD')
    MYSQL_DB = os.environ.get('DB_NAME')
    MYSQL_PORT = 3306
    MYSQL_CUSTOM_OPTIONS = {"ssl": {"ca": "DigiCertGlobalRootCA.crt.pem"}}
    MYSQL_USE_UNICODE = True

    # Mail Config
    MAIL_SERVER = os.environ.get("M_SERVER")
    MAIL_PORT =  os.environ.get("M_PORT")
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = os.environ.get("M_USER")
    MAIL_PASSWORD = os.environ.get("M_PASSWORD")
    MAIL_DEFAULT_SENDER = os.environ.get("M_USER")

