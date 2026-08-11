from pyramid.config import Configurator

from portfolio import views


def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.include("pyramid_jinja2")
    config.add_route("home", "/")
    config.add_static_view(name="static", path="portfolio:static")
    config.scan()
    return config.make_wsgi_app()
