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

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method=='GET':
        #return "hello GET"
        return redner_template ('form.html')
    if request.method=='POST':
        first_name=request.form("first_name")
        # return "Hi, your name is %s" % first_name
        return redner_template ('form.html', first_name=first_name)

if __name__ =='__main__':
    app.run()
