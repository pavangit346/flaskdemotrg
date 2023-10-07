'''

The sample code demonstrates the basic usage of Flask with
SQLAlchemy to add a user to an SQLite database.
'''

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

@app.route('/')
def index():
    user = User(username='John', email='john@example.com')
    db.session.add(user)
    db.session.commit()
    return 'User added to the database!'

if __name__ == '__main__':
    app.run()
Continued
Picture10.png
The sample code demonstrates a basic Flask app using Flask-PyMongo to retrieve and add users to a MongoDB database.

from flask import Flask, jsonify, request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/your_database'
mongo = PyMongo(app)

@app.route('/')
def index():
    return 'Hello, Flask with MongoDB!'

@app.route('/users', methods=['GET'])
def get_users():
    users = mongo.db.users.find()
    result = []
    for user in users:
        result.append({'username': user['username'], 'email': user['email']})
    return jsonify(result)

@app.route('/users', methods=['POST'])
def add_user():
    user_data = request.get_json()
    mongo.db.users.insert_one(user_data)
    return 'User added to the database!'

if __name__ == '__main__':
    app.run()