from app import create_app
import os

app = create_app(os.environ.get('ENV', 'DEV'))

if __name__ == "__main__":
    app.run(host=os.environ.get('HOST', '0.0.0.0'), port=os.environ.get('PORT', 5000))
