from models.store import StoreModel
from flask_restful import Resource,reqparse

class Store(Resource):

    #parser = reqparse.RequestParser()
    #parser.add_argument('name',type=str,required=True,help='cannot empty')
    
    def get(self,name):

        #data = Store.parser.parse_args()

        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'message':'Not found'},404

    def post(self,name):
        #data = Store.parser.parse_args()
        if StoreModel.find_by_name(name):
            return {'message':'store found'}
    
        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {'message','something went wrong'},500
        
        return store.json(),201

    def delete(self,name):
        #data = Store.parser.parse_args()
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
            return {'message':'Store deleted'},200
        return {'message','store not found'}
        

class StoreList(Resource):
    def get(self):
        return {'store':list(map(lambda x: x.json(),StoreModel.query.all()))}
        