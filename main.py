import os, random, time, websockets
from ppadb.client import Client as AdbClient
import threading

from ADBTools import adb_tools_v2
from ADBTools.adb_tools_v2 import AdbToolsV2
from WebsocketHelper.MessageEmitter import MessageEmitter
from WebsocketHelper.MessageSender import MessageSender
from flask import Flask, jsonify, render_template, Response
from flask_cors import CORS
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)
CORS(app)  # Enable CORS for all routes

emitter = MessageEmitter(socketio)
sender = MessageSender(emitter)
adb_tools = AdbToolsV2(socketio)

path_to_scripts = "<PATH TO SCRIPTS>"
timeout_seconds = 3
os.environ["ADB_PATH"] = "<PATH TO ADB>"
os.environ["DPATH"] = "<PATH TO LOGS>"

# ---------------------------------------
# Manager class to handle function calls
# ---------------------------------------
class Manager:
    @staticmethod
    def check_version():
        return adb_tools.version_check()

    @staticmethod
    def check_ppi():
        return adb_tools.ppi_check()

    @staticmethod
    def check_antenna():
        return adb_tools.antenna_check()

    @staticmethod
    def get_adb_version():
        try:
            client = AdbClient(host="127.0.0.1", port=5037)
            version = client.version()
            return version
        except Exception as e:
            return f"Error getting ADB version: {str(e)}"

# ---------------------------------------
# API routes
# ---------------------------------------
@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/api/check_version', methods=['GET'])
def api_check_version():
    command = [path_to_scripts + "version_check.bat"]

@app.route('/api/check_ppi', methods=['GET'])
def api_check_ppi():
    result = Manager.check_ppi()
    return jsonify({'message': result})

@app.route('/api/check_antenna', methods=['GET'])
def api_check_antenna():
    result = Manager.check_antenna()
    return jsonify({'message': result})

@app.route('/api/adb_version', methods=['GET'])
def api_get_adb_version():
    result = Manager.get_adb_version()
    return jsonify({'message': result})

# ---------------------------------------
# Socket functions
# ---------------------------------------
@socketio.on('connect')
def handle_connect():
    print("Client connected")
    sender.send_green_message("Connected")

@socketio.on('disconnect')
def handle_disconnect():
    print("Client disconnected")

def background_task():
    while True:
        time.sleep(5)  # Wait for 5 seconds
        sender.send_message("Hello from the background task!")

@socketio.on('adb_version_check')
def handle_adb_version_check():
    print("Received ADB version check request")
    result = Manager.get_adb_version()
    emit('server_response', result)

@socketio.on('dcm_version_check')
def handle_adb_version_check():
    print("Received DCM version check request")
    adb_tools.version_check()

@socketio.on('client_message')
def handle_client_message(data):
    print(f"Received message from client: {data}")
    # Process the message and prepare a response
    response = f"Processed: {data}"
    # Send the response back to the client
    emit('server_response', response)

# ---------------------------------------
# App start
# ---------------------------------------
if __name__ == '__main__':
    # Run the Flask application
    socketio.run(app, host='0.0.0.0', port=5000, allow_unsafe_werkzeug=True, debug=True)
