from .views import bp


def blueprints(api):
    api.register_blueprint(bp)