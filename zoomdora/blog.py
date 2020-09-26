from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from zoomdora.auth import login_required
from zoomdora.db import get_db

bp = Blueprint('blog', __name__)

@bp.route('/')
def index():
    db = get_db()
    posts = db.execute(
        'SELECT p.id, title, body, created, author_id, username, category'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()
    return render_template('blog/index.html', posts=posts)

@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        print('request.form=', request.form)
        title = request.form['title']
        body = request.form['body']
        category = request.form['cat']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO post (title, body,' + 
                'category, author_id)' +
                ' VALUES (?, ?, ?, ?)',
                (title, body, category, g.user['id'])
            )
            db.commit()
            cn = get_db().cursor()
            cn.execute("SELECT * from post WHERE title ='" + title + "';")
            print(cn.fetchone()[0])
            return redirect(url_for('blog.index'))
    else:
        cn = get_db().cursor()
        cn.execute('SELECT name FROM categories')
        cat_list = cn.fetchall()
        arr = []
        for row in cat_list:
            arr.append(row[0])
        print("cat_list=", arr)
    return render_template('blog/create.html', cat_list=arr)

def get_post(id, check_author=True):
    post = get_db().execute(
        'SELECT p.id, title, body, created, author_id, username, category'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' WHERE p.id = ?',
        (id,)
    ).fetchone()

    if post is None:
        abort(404, "Post id {0} doesn't exist.".format(id))

    if check_author and post['author_id'] != g.user['id']:
        abort(403)

    return post

@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    post = get_post(id)
    print("post==", post)
    print(post[0])
    print(post[1])
    print(post[2])
    print(post[3])
    print(post[4])
    print(post[5])
    print(post[6])

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        category = request.form['category']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE post SET title = ?, body = ?'
                ' WHERE id = ?',
                (title, body, id)
            )
            db.commit()
            return redirect(url_for('blog.index'))
    else:
        cn = get_db().cursor()
        cn.execute('SELECT name FROM categories')
        cat_list = cn.fetchall()
        arr = []
        for row in cat_list:
            arr.append(row[0])
        print("cat_list=", arr)

    return render_template('blog/update.html', post=post, cat_list=arr)

@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    get_post(id)
    db = get_db()
    db.execute('DELETE FROM post WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('blog.index'))




