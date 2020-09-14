import os

from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

channels = {
        'general': {
                'users': ['Sohaila', 'Dodge'],
                'messages': [
                        {
                                'username': 'Sohaila',
                                'date': '9-5 15:45',
                                'text': 'This is my first message'
                                },
                        {
                                'username': 'Dodge',
                                'date': '9-5 16:00',
                                'text': 'Hi Sohaila'
                                },
                        {
                                'username': 'Sohaila',
                                'date': '9-5 18:00',
                                'text': 'Third message'
                                },
                        ]
                },
        'Anime': {
                'users': ['Sohaila', 'Lala'],
                'messages': [
                        {
                                'username': 'Sohaila',
                                'date': '9-5 15:45',
                                'text': 'first anime message'
                                },
                        {
                                'username': 'Lala',
                                'date': '9-5 16:00',
                                'text': 'Hi anime'
                                },
                        {
                                'username': 'Sohaila',
                                'date': '9-5 18:00',
                                'text': 'Third message anime'
                                },
                        {
                                'username': 'Lala',
                                'date': '9-5 18:00',
                                'text': 'I love anime'
                                },
                        ]
                }
        }

@app.route("/", methods=['POST', 'GET'])
def index():
    return render_template('index.html', channels = channels)

@app.route("/create/<string:name>")
def create_channel(name):
    channels[name] = {}
    return channels

@app.route("/display/<string:name>")
def display_channel(name):
    return channels[name]

@socketio.on('send message')
def send(data):
    dict = {'username': data['username'], 'date': data['date'], 'text': data['text']}
    channels[data['channel']]['messages'].append(dict)
    channel = channels[data['channel']]
    emit('new message', channel, broadcast= True)


if __name__ =='__main__':
    app.run(debug=True)
