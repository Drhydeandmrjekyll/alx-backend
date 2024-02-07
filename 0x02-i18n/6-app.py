#!/usr/bin/env python3
"""User Login System Mock with Locale Preference"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _

app = Flask(__name__)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

@app.before_request
def before_request():
    """Executed before all other functions."""
    g.user = get_user(request.args.get('login_as'))

def get_user(user_id):
    """Retrieve user dictionary."""
    if user_id and int(user_id) in users:
        return users[int(user_id)]
    return None

@babel.localeselector
def get_locale():
    """Determine best match for user's preferred language."""
    user_locale = None
    if g.user and 'locale' in g.user:
        user_locale = g.user['locale']
    elif request.args.get('locale'):
        user_locale = request.args.get('locale')
    return user_locale or request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index():
    """Renders index.html template."""
    return render_template('6-index.html')

if __name__ == '__main__':
    app.run()
