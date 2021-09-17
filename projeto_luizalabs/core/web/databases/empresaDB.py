from bson import ObjectId
from pymongo import MongoClient

client = MongoClient("localhost", 27017)

db = client.LuizaLabsProject



def insert_empresa(empresa):
    return db.empresa.insert_one(empresa)


def delete_empresa(empresaID):
    return db.empresa.delete_one({"_id": ObjectId(empresaID)})


def read_empresa_all():
    empresa = db.empresa.find({})
    return empresa


def read_empresa_by_id(empresaID):
    return db.empresa.find_one({"_id":ObjectId(empresaID)})


def update_empresa(empresaID, update_doc):
    print("update", empresaID)
    try:
        db.empresa.update_one({"_id": ObjectId(empresaID)}, {"$set": update_doc})
        return True
    except Exception as error:
        print('log:', str(error))
        return False