from flask_script import Manager
from api import create_api


manager = Manager(create_api)

if __name__ == "__main__":
    manager.run()