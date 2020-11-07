
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.exceptions import abort

from zoomdora.auth import login_required
from zoomdora.db import get_db



bp = Blueprint('user_settings', __name__, url_prefix='/settings', static_folder='static',
                static_url_path='/')

print('hello from settings')

@bp.route("/")
def show_settings():
    print('user id=')
    print(session['user_id']) 
    user_id = session['user_id']
    db = get_db()
    g.user = db.execute("SELECT * from user WHERE id= ?", (user_id,)).fetchone()
    print('id=', g.user['id'])
    print('email=', g.user['email'])
    print('usename=', g.user['username'])
    return render_template('user_settings/settings.html')


