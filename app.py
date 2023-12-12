from flask import Flask, request, jsonify, config
from embed import InstructorEmbeddingService

app = Flask(__name__)


def init_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(config.Config)
    app.config["instructor_svc"] = InstructorEmbeddingService()

    with app.app_context():
        from routes import api

        app.register_blueprint(api)
        return app


if __name__ == "__main__":
    app = init_app()
    app.run()
