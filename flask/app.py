from flask import Flask
from flask import render_template
from flask import request

abc = Flask(__name__)

@abc.route('/')
@abc.route('/index')
def index():
    name = 'Rosalia'
    return render_template('index.html', title='Welcome', username=name)

if __name__ == '__main__':
    abc.run(host='0.0.0.0', port=80, debug=True)