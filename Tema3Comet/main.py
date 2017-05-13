from gevent import monkey
from flask import Flask, render_template, request
import random

monkey.patch_all()

app = Flask(__name__)

message_list = []
db = dict()
db['connected'] = 0
username = 'Unnamed User ' + str(random.randint(0, 123456))


@app.route('/')
def chat():
    return render_template('chat.html')


@app.route('/chat')
def ws_conn():
    db['connected'] = db['connected'] + 1
    c = db['connected']
    return c


@app.route('/getmessages')
def get_msg():
    global message_list
    response=''
    for iterator in message_list:
        response=response+'<h3>' + iterator + '<h3>'
    return response


@app.route('/postmessages',methods=['POST'])
def post_msg():
    global message_list
    message_list.append(username + ' : ' + request.get_json())
    return username + ' : ' + request.get_json()


@app.route('/setname',methods=['POST'])
def set_name():
    global username
    username = request.get_json()
    return username


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
