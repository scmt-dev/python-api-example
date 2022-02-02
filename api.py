from flask import Flask, json, request, jsonify
from flask_cors import CORS


import db

companies = [{"id": 1, "name": "Company One"}, {"id": 2, "name": "Company Two"}]
users = [{"id": 1, "name": "user 1"}, {"id": 2, "name": "user 2"}]

app = Flask(__name__)

import jwt
import testApi
CORS(app)

@app.route('/', methods=['GET'])
def get():
  return json.dumps({"success": True, "message":"Welcome API v1"})

@app.route('/companies', methods=['GET'])
def get_companies():
  return json.dumps(companies)

@app.route('/user', methods=['POST'])
def post_user():
  data = json.loads(request.data)
  email = data['email']
  password = data['password']
  cur = db.cur
  statement = "INSERT INTO users (email, password) VALUES (%s, %s)"
  data = (email, password)
  cur.execute(statement, data)
  db.con.commit()
  return json.dumps({"success": True}), 201

@app.route('/users', methods=['GET'])
def get_users():
  cur = db.cur
  cur.execute("SELECT * FROM users")
  r = [dict((cur.description[i][0], value)
  for i, value in enumerate(row)) for row in cur.fetchall()]
  return jsonify(r)

if __name__ == '__main__':
    app.run() 