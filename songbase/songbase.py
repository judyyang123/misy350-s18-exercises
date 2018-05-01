from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    # return "hello judy yang"
    return render_template ('index.html')


@app.route('/user')
def user():
    return "this is the page for users"


@app.route('/users/<string:username>')
def users(username):
    # return "hello %s" %username
    return render_template('user.html', uname=username)


if __name__ =='__main__':
    app.run()
