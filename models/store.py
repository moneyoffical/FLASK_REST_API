from db import db

class StoreModel(db.Model):

    __tablename__ ='stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    #items = db.relationship('ItemModel',lazy='dynamic')


    def __init__(self,name):
        self.name = name

    def json(self):
        #return {'name':self.name,'items':[x.json() for x in self.items.all()]}   # REFERENCE 
        return {'name':self.name}

    @classmethod
    def find_by_name(cls,name):
        return cls.query.filter_by(name=name).first()   # query is a build-in func from sqlAlchemy(db.Model)

    #@classmethod
    #def insert(cls,item):
    def save_to_db(self):
        db.session.add(self)         # add is for inserting BIF
        db.session.commit()

    #@classmethod
    #def update(cls,item):
    def delete_from_db(self):
        db.session.delete(self)            # delete is BIF
        db.session.commit()
