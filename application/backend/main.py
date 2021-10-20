from re import DEBUG
from src.app import Application

def start() -> None:
    app = Application.create_app()
    app["socketio"].run(app["app"], host="localhost", port=4000, debug=True, load_dotenv=True)
    

if __name__ == '__main__':
    start()