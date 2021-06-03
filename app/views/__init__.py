from .views import file_bp


def register_bp(app):
    app.register_blueprint(file_bp)
