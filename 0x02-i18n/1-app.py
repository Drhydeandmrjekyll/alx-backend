#!/usr/bin/env python3
"""Babel Flask Extension"""

from flask import Flask, render_template
from flask_babel import Babel

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
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
