from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    # return "hello judy yang"
    return render_template ('index.html')

@app.route('/greeting')
def greeting():
    import random
    greeting_list = ['Ciao', 'Hei', 'Salut', 'Hola', 'Nihao']
    return random.choice(greeting_list)

@app.route('/user')
def user():
    return "this is the page for users"


@app.route('/users/<string:username>')
def users(username):
    # return "hello %s" %username
    return render_template('users.html', uname=username)

@app.route('/form')
def form():
    return render_template ('form.html')

if __name__ =='__main__':
    app.run()
