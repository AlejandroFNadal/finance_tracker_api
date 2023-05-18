import os
import dotenv
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """Configuration data."""
    # pull in the environment variables
    dotenv.load_dotenv()
    SECRET_KEY = os.environ.get('SECRET_KEY')
    db_host = os.getenv('DB_HOST')
    db_pass = os.getenv('DB_PASS')
    db_name = os.getenv('DB_NAME')
    db_user = os.getenv('DB_USER')
    user_pass = f"{db_user}:{db_pass}"
    user_pass_host = f"{user_pass}@{db_host}"
    url = f"mysql+pymysql://{user_pass_host}/{db_name}"
    # now we create the connection string for SQLAlchemy
    SQLALCHEMY_DATABASE_URI = url
    SQLALCHEMY_TRACK_MODIFICATIONS = False

