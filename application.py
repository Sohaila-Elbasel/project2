import os

from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

channels = {
        'general': {
                'users': ['Sohaila', 'Dodge'],
                'messages': {
                        0: {
                                'username': 'Sohaila',
                                'date': '9-5 15:45',
                                'text': 'This is my first message'
                                },
                        1: {
                                'username': 'Dodge',
                                'date': '9-5 16:00',
                                'text': 'Hi Sohaila'
                                },
                        2: {
                                'username': 'Sohaila',
                                'date': '9-5 18:00',
                                'text': 'Third message'
                                },
                        }
                },
        'Anime': {
                'users': ['Sohaila', 'Lala'],
                'messages': {
                        0: {
                                'username': 'Sohaila',
                                'date': '9-5 15:45',
                                'text': 'first anime message'
                                },
                        1: {
                                'username': 'Lala',
                                'date': '9-5 16:00',
                                'text': 'Hi anime'
                                },
                        2: {
                                'username': 'Sohaila',
                                'date': '9-5 18:00',
                                'text': 'Third message anime'
                                },
                        3: {
                                'username': 'Lala',
                                'date': '9-5 18:00',
                                'text': 'I love anime'
                                },
                        }
                }
        }

@app.route("/", methods=['POST', 'GET'])
def index():
    return render_template('index.html', channels = channels)

@app.route("/create/<string:name>")
def create_channel(name):
    channels[name] = {'text': ['Sohaila', 'Mohamed']}
    return channels

@app.route("/display/<string:name>")
def display_channel(name):
    return channels[name]



if __name__ =='__main__':
    app.run(debug=True)
