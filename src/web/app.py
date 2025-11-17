from flask import Flask
from flask_session import Session
from src.config.settings import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize Flask-Session
    Session(app)

    # Register blueprints
    from src.web.routes import routes
    app.register_blueprint(routes)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)