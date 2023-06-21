from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "testingroot"

from user import User

@app.route('/')
def button():
    return render_template("user.html")

@app.route('/submit_game_form', methods=['POST'])
def relocate():
    User.add_game(request.form)
    users = User.get_all()
    return render_template("userList.html", users=users)


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=8000)

