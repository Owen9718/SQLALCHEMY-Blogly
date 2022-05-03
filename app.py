"""Blogly application."""

from flask import Flask,redirect,render_template,request
from models import db, connect_db,User


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

@app.route('/')
def users():

    return redirect('/users')


@app.route('/users')
def list_users():
    users = User.query.order_by(User.last_name,User.first_name).all()
    return render_template('users.html',users = users)


@app.route('/users/new')
def create_user():

    return render_template('home.html')


@app.route('/users/new', methods= ['POST'])
def add_user():
    image_url = request.form['url'] if request.form['url']!= "" else None
    new_user = User(first_name = request.form['first'],last_name = request.form['last'],image_url = image_url)
    db.session.add(new_user)
    db.session.commit()
    return redirect('/users')


@app.route(f'/users/<int:user_id>')
def user_info(user_id):
    user = User.query.get_or_404(user_id)
    print('THIS IS IMAGE', user.image_url)
    return render_template('user_info.html', user= user)


@app.route(f'/users/<int:user_id>/edit')
def edit_temp(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('edit.html',user = user)


@app.route(f'/users/<int:user_id>/edit', methods =["POST"])
def save_edit(user_id):
    user = User.query.get_or_404(user_id)
    user.first_name = request.form['first']
    user.last_name = request.form['last']
    user.image_url = request.form['image']

    db.session.add(user)
    db.session.commit()
    return redirect('/users')


@app.route(f'/users/<int:user_id>/delete', methods =["POST"])
def delete(user_id):

    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()

    return redirect("/users")
