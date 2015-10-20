import os
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def show_index_page():
    return 'Flask Test Page!!!'

@app.route('/user/')
@app.route('/user/<name>/')
def insert_user(name = None):
    #return 'insert user : %s' % name;
	return render_template('hello.html', name=name)

@app.route('/user/<id>/<name>/')
def insert_user2(id, name):
    return 'insert user [%s, %s]' % (id, name);


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
