from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from jinja2.exceptions import TemplateNotFound
import secrets
import string

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///passwords.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Password(db.Model):
    __tablename__ = 'passwords'
    index = db.Column(db.Integer, primary_key=True)
    website = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)

    
passwords = []

@app.route('/')
def index():
    passwords = Password.query.all()
    return render_template('landon.html', passwords=passwords)

@app.route('/generate_passw', methods=['POST'])
def generate_passw():
    website = request.form['website']
    email = request.form['email']
    password = passwgenerator()
    new_password = Password(website=website, email=email, password=password)
    db.session.add(new_password)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/ud_passw/<int:index>', methods=['POST'])
def ud_passw(index):
    password = Password.query.get_or_404(index)
    password.website = request.form['website']
    password.email = request.form['email']
    password.password = request.form['password']
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete_passw/<int:index>')
def delete_password(index):
    password = Password.query.get_or_404(index)
    db.session.delete(password)
    db.session.commit()
    return redirect(url_for('index'))

def passwgenerator(length=15):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
