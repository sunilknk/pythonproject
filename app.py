from flask import Flask,request,json,jsonify
from flask_smorest import abort



app=Flask(__name__)


stores=[
    {
       "name":"mystore",
       "items":[
          {
             "name":"chair",
             "price":200
          }

       ]
    },
      {
       "name":"mystore1",
       "items":[
          {
             "name":"chair",
             "price":150
          }

       ]
    }
 ]

@app.get('/stores')
def  get_stores():
     return {"stores":stores}

@app.post('/stores')
def add_store():
    data=request.get_json()  
    if "name" not in data:
        abort(201,message="bad payload,please provide name")
    for store in stores:
        if data["name"]==store["name"]:
            abort(message="store already exists")
        
    new_store={"name":data["name"],"items":[]}
    stores.append(new_store)
    return new_store

@app.post('/stores/<string:name>/item')
def add_item(name):
    for store in stores:
        if store["name"]==name:
            data=request.get_json()
            new_item={"name":data["name"],"price":data["price"]}
            store["items"].append(new_item)
            return store,201        
      
    abort(404,message="no such store found")

@app.get('/stores/<string:name>')
def  get_spec_store(name):
    for store in stores:
        if store["name"]==name:
            return store
    abort(201,message="no such store found")

@app.get('/stores/<string:name>/<string:itemname>')
def  get_spec_item(name,itemname):
    for store in stores:
        if store["name"]==name:
            for item in store["items"]:
                if item["name"]==itemname:
                    return item
            abort(message="no such item found")
    abort(message="no such store found")