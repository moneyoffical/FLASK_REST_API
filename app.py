from flask import Flask
from flask_jwt import JWT
from flask_restful import Api

from security import authenticate,identity
from resources.user import UserRegister,UsersList
from resources.item import Item,ItemList
from resources.store import Store,StoreList


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key ='sangam'
api = Api(app)

#when we want to create tables with SQLAlchemy
#@app.before_first_request
#def create_table():
#    db.create_all()


app.config['JWT_AUTH_URL_RULE'] = '/login'   # custom for URL for JWT token
#app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=1800)  # for token time 
jwt = JWT(app,authenticate,identity)         # /auth  
                                            # jwt automatically creates the above path

api.add_resource(Store,'/store/<string:name>')
api.add_resource(Item,'/item/<string:name>')

api.add_resource(StoreList,'/stores')
api.add_resource(ItemList,'/items')
api.add_resource(UserRegister,'/register')
api.add_resource(UsersList,'/users')

if __name__ == '__main__':
    #from db import db
    #db.__init__(app)
    app.run(debug=True)
