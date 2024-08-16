from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_client')
def start_client():
    os.system('python client.py')  # Use os.system for Windows compatibility
    return "Client started. You can close this tab."

@app.route('/start_server')
def start_server():
    os.system('python server.py')  # Use os.system for Windows compatibility
    return "Server started. You can close this tab."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
