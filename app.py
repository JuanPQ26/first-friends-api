from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Welcome to my friends API!'


@app.route('/friend/', methods=['GET'])
def get_all_friends():
    return 'friends found'


if __name__ == '__main__':
    app.run()
