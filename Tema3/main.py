from gevent import monkey
monkey.patch_all()
import cgi
from flask import Flask, render_template, request
from flask_socketio import SocketIO
import random
app = Flask(__name__)
db = dict()
db['connected']=0
username='Unnamed User '+str(random.randint(0,123456))
socketio = SocketIO(app)

@app.route('/')
def chat():
    return render_template('chat.html')

@socketio.on('connect', namespace='/chat')
def ws_conn():
    db['connected']=db['connected']+1
    c = db['connected']
    socketio.emit('msg', {'count': c}, namespace='/chat')

@socketio.on('msg', namespace='/chat')
def ws_msg(message):
    message['msg']=username+' : '+message['msg']
    socketio.emit('msg', {'msg': cgi.escape(message['msg'])},namespace="/chat")


@socketio.on('name', namespace='/chat')
def ws_name(name):
    global username
    username=name['name']
    socketio.emit('name', {'name': cgi.escape(name['name'])},namespace="/chat")

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
