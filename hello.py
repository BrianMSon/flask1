import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def show_index_page():
    return 'Flask Test Page!!!'

@app.route('/user')
def select_user():
    return 'user list...'

@app.route('/user/<id>/<name>')
def insert_user():
    return 'insert user [%s, %s]' % id & name;

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
