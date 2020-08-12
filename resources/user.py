import sqlite3
from flask_restful import Resource,reqparse
from models.user import UserModel

class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help="cannot be empty.")
    parser.add_argument('password',
        type=str,
        required=True,
        help="cannot be empty.")

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {'messgae':'User already exists'},400

        user = UserModel(**data)
        user.save_to_db()

        return {'message':'user created successfully'},201

class UsersList(Resource):
    def get(self):
        return {'users': list(map(lambda x: x.json(),UserModel.query.all()))}
        
