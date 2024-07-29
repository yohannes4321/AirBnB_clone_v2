#!/usr/bin/python3
"""Flask app to generate HTML list of all states from storage"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask('web_flask')
app.url_map.strict_slashes = False


@app.route('/states_list')
def list_of_states():
    """Render HTML with unordered list of states from `storage`"""
    states = sorted(storage.all(State).values(), key=lambda s: s.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """Close database or file storage"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
