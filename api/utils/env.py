import dotenv
import os

# init dotenv
dotenv.load_dotenv()


def get_env(key, default=None):
    return os.getenv(key, default)
