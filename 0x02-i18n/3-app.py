#!/usr/bin/env python3
"""Babel Flask Extension"""

from flask import Flask, render_template
from flask_babel import Babel, _

app = Flask(__name__)
babel = Babel(app)


class Config:
    """Config class with LANGUAGES attribute"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


@app.route('/')
def index():
    """Renders index.html template."""
    return render_template('3-index.html')


@babel.localeselector
def get_locale():
    """Determine best match for user's preferred language."""
    return request.accept_languages.best_match(Config.LANGUAGES)


if __name__ == '__main__':
    app.run()

