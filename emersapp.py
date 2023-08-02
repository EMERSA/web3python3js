from flask import Flask, render_template, session, redirect, url_for
import time
from web3 import Web3

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Initialize Web3
w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/your_infura_project_id'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'account' in session:
        return render_template('dashboard.html', account=session['account'])
    return redirect(url_for('login'))

@app.route('/authenticate')
def authenticate():
    if 'account' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)