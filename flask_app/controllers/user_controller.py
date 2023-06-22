from flask_app import app
from flask import render_template, request, redirect, url_for
from flask_app.models.user import User

@app.route('/')
def button():
    return redirect(url_for('add_user'))

@app.route('/users', methods=['GET'])
def user_list():
    users = User.get_all()
    return render_template("user.html", users=users)

@app.route('/users', methods=['POST'])
def create_user():
    data = {
        'first_name': request.form.get('first_name'),
        'last_name': request.form.get('last_name'),
        'email': request.form.get('email')
    }
    if data['first_name']:
        User.add_user(data)
        return redirect(url_for('user_list'))
    else:
        return render_template("add_user.html")

@app.route('/users/<int:user_id>', methods=['GET', 'POST'])
def show_user(user_id):
    if request.method == 'POST':
        user = User.get_user(user_id)
        if user:
            User.delete(user_id)
        return redirect(url_for('user_list'))

    user = User.get_user(user_id)
    if user:
        return render_template("user_info.html", user=user)
    else:
        return redirect(url_for('user_list'))

@app.route('/users/<int:user_id>/edit', methods=['GET'])
def edit_user(user_id):
    user = User.get_user(user_id)
    if user:
        return render_template("edit_user.html", user=user)
    else:
        return redirect(url_for('user_list'))

#Over again
@app.route('/users/<int:user_id>/edit', methods=['POST'])
def update_user(user_id):
    user = User.get_user(user_id)
    if user:
        getting = {
            'id': user_id,
            'first_name': request.form.get('first_name'),
            'last_name': request.form.get('last_name'),
            'email': request.form.get('email')
        }
        user.update(getting)
        return redirect(url_for('show_user', user_id=user_id))
    else:
        return redirect(url_for('user_list'))

#Deelete
@app.route('/users/<int:user_id>/delete', methods=['GET', 'POST'])
def delete_user(user_id):
    user = User.get_user(user_id)
    if user:
        User.delete(user_id)
    return redirect(url_for('user_list'))

@app.route('/users/add', methods=['GET'])
def add_user():
    return render_template("add_user.html")