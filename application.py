import os

from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

@app.route("/", methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        check_name = request.form.get('displayname')
        if check_name.isspace() or check_name == '':
            message = "Invalid name"
            return render_template('index.html',message = message)
    return render_template('index.html')


if __name__ =='__main__':
    app.run(debug=True)
