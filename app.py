from flask import Flask
from datetime import datetime
import os
import subprocess
import getpass

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Prasanna Kaikala"
    username = getpass.getuser()  # Using getpass to retrieve the username
    server_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S IST")
    top_output = subprocess.getoutput("top -b -n 1 | head -15")  # Runs the top command in non-interactive mode

    return f"""
    <h1>System Information</h1>
    <p><strong>Name:</strong> {name}</p>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Server Time:</strong> {server_time}</p>
    <pre>{top_output}</pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
