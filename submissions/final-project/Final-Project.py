from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from jinja2.exceptions import TemplateNotFound
import secrets
import string

app = Flask(__name__)

passwords = []

@app.route('/')
def index():
    return render_template('landon.html', passwords=passwords)

@app.route('/generate_passw', methods=['POST'])
def generate_passw():
    website = request.form['website']
    email = request.form['email']
    password = passwgenerator()
    passwords.append({'website': website, 'email': email, 'password': password})
    return redirect(url_for('index'))

@app.route('/ud_passw/<int:index>', methods=['POST'])
def ud_passw(index):
    website = request.form['website']
    email = request.form['email']
    password = request.form['password']
    passwords[index] = {'website': website, 'email': email, 'password': password}
    return redirect(url_for('index'))

@app.route('/delete_passw/<int:index>')
def delete_password(index):
    del passwords[index]
    return redirect(url_for('index'))

def passwgenerator(length=15):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

if __name__ == '__main__':
    app.run(debug=True)
