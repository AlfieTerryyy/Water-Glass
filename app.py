from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_socketio import SocketIO, send, join_room, leave_room
import os
import logging
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey!'
socketio = SocketIO(app)

# Define special key and user storage
SPECIAL_KEY = "chatroom123"
active_users = {}  # {session_id: username}

# File to store profiles
LOGGINGS_FILE = "loggings.json"

# Configure text logging
logging.basicConfig(
    filename="chat.log", 
    level=logging.INFO, 
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Helper functions for profile management
def load_profiles():
    if os.path.exists(LOGGINGS_FILE):
        with open(LOGGINGS_FILE, "r") as file:
            return json.load(file)
    return {}

def save_profiles(profiles):
    with open(LOGGINGS_FILE, "w") as file:
        json.dump(profiles, file, indent=4)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    key = request.form.get('key')
    username = request.form.get('username')

    if key == SPECIAL_KEY and username:
        session['username'] = username
        return redirect(url_for('chat'))
    return "Invalid Key or Username", 403

@app.route('/chat')
def chat():
    if 'username' not in session:
        return redirect(url_for('index'))
    return render_template('chat.html', username=session['username'])

@app.route('/profiles', methods=['GET'])
def get_profiles():
    profiles = load_profiles()
    return jsonify(profiles)

@app.route('/profiles', methods=['POST'])
def add_profile():
    data = request.json
    if not data or "username" not in data:
        return "Invalid data", 400

    profiles = load_profiles()
    profiles[data["username"]] = data
    save_profiles(profiles)
    return jsonify({"message": f"Profile for {data['username']} added successfully."}), 201

@socketio.on('join')
def handle_join(data):
    username = session['username']
    active_users[request.sid] = username
    join_room('main')
    log_message = f"{username} has joined the chat."
    logging.info(log_message)
    send(log_message, room='main')

@socketio.on('message')
def handle_message(data):
    username = active_users.get(request.sid, "Unknown")
    log_message = f"{username}: {data['message']}"
    logging.info(log_message)
    send(log_message, room='main')

@socketio.on('leave')
def handle_leave():
    username = active_users.pop(request.sid, "Unknown")
    leave_room('main')
    log_message = f"{username} has left the chat."
    logging.info(log_message)
    send(log_message, room='main')

@socketio.on('disconnect')
def handle_disconnect():
    username = active_users.pop(request.sid, "Unknown")
    leave_room('main')
    log_message = f"{username} has disconnected."
    logging.info(log_message)
    send(log_message, room='main')

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    socketio.run(app, host='0.0.0.0', port=port)
