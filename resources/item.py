try:
    import sqlite3
    from flask_restful import Resource, reqparse
    from flask_jwt  import jwt_required
    import sys
except Exception as e:
    print('something went wrong',e)

# insert at 1, 0 is the script path (or '' in REPL)
#sys.path.insert(1, '/models/item/ItemModel')

#from . import models
from models.item import ItemModel


class Item(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('price',type=float,required=True,help='not empty')
    parser.add_argument('store_id',type=int,required=True,help='not empty')

    @jwt_required()
    def get(self,name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message':'Item not found'},404

    def post(self,name):
        if ItemModel.find_by_name(name):
            return {'message':'Item already present'}

        #Item.parser.add_argument('price',required=True,help='not empty')
        data = Item.parser.parse_args()
        item = ItemModel(name,**data)

        try:
            item.save_to_db()
        except:
            return{"message":"An error occured during insert"},500

        return item.json(),201

    def delete(self,name):
        item = ItemModel.find_by_name(name)
        
        if item:
            item.delete_from_db()
            return {'message': 'Item deleted.'}
        return {'message':'item not found'},404

    def put(self,name):
        
        #Item.parser.add_argument('price',required=True,help='not empty')
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)

        if item is None:
            item = ItemModel(name,**data)
        else:
            item.price = data['price']
        item.save_to_db()

        return item.json()



class ItemList(Resource):
     def get(self):
        #return {'item':[x.json() for x in ItemModel.query.all()]}
        return {'item': list(map(lambda x: x.json(),ItemModel.query.all()))}

