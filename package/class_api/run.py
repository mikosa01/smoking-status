from api.app import create_app
from api.config import DevelopConfig


application = create_app(config_object= DevelopConfig)

if __name__ == '__main__':
    application.run()