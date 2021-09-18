from bson import ObjectId
from pymongo import MongoClient

client = MongoClient("localhost", 27017)

db = client.LuizaLabsProject



def insert_produto(insert_doc):
    return db.produto.insert_one(insert_doc)


def delete_produto(produtoID):
    return db.produto.delete_one({"_id": ObjectId(produtoID)})


def read_produto_all():
    produto = db.produto.find({})
    return produto


def read_produto_by_id(produtoID):
    return db.produto.find_one({"_id":ObjectId(produtoID)})


def update_produto(produtoID, update_doc):
    print("update",produtoID)
    try:
        db.produto.update_one({"_id": ObjectId(produtoID)}, {"$set": update_doc})
        return True
    except Exception as error:
        print('log:', str(error))
        return False