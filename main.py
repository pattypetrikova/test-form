from app import create_app, mail
from dotenv import load_dotenv
load_dotenv()

flask_app = create_app()

if __name__ == "__main__":
    flask_app.run(debug=True)