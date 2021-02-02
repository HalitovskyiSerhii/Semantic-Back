from app import create_app
import os

app = create_app(os.environ.get('ENV', 'DEV'))

if __name__ == "__main__":
    app.run()
