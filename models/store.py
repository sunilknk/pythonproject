from db import db

class StoreModel(db.Model):
    __tablename__="store"
    id=db.Column(db.integer,primary_key="True")
    name=db.Column(db.String(80),unique="True",nullable="False")