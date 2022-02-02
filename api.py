from flask import Flask, json, request
from flask_cors import CORS

companies = [{"id": 1, "name": "Company One"}, {"id": 2, "name": "Company Two"}]
users = [{"id": 1, "name": "user 1"}, {"id": 2, "name": "user 2"}]

api = Flask(__name__)
CORS(api)

@api.route('/', methods=['GET'])
def get():
  return json.dumps({"success": True, "message":"Welcome API v1"})

@api.route('/companies', methods=['GET'])
def get_companies():
  return json.dumps(companies)

@api.route('/user', methods=['POST'])
def post_user():
  data = json.loads(request.data)
  print(data)
  return json.dumps({"success": True}), 201

@api.route('/users', methods=['GET'])
def get_users():
  return json.dumps(users)

if __name__ == '__main__':
    api.run() 