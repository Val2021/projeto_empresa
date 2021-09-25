from bson import ObjectId
from pymongo import MongoClient

client = MongoClient("localhost", 27017)

db = client.LuizaLabsProject



def insert_empresa(empresa):
    return str(db.empresa.insert_one(empresa).inserted_id)


def delete_empresa(empresaID):
    return db.empresa.delete_one({"_id": ObjectId(empresaID)})


def read_empresa_all():
    empresa = db.empresa.find({})
    return empresa


def read_empresa_by_id(empresaID):
    return db.empresa.find_one({"_id":ObjectId(empresaID)})


def update_empresa(id_empresa,empresa):
    try:
        db.empresa.update({"_id": ObjectId(id_empresa)}, {"$set": empresa})
        return True
    except Exception as error:
        print('log:', str(error))
        return False

def update_empresaProduto(id_empresa,produto):
    try:
        db.empresa.update_one({"_id": ObjectId(id_empresa)}, {"$set":produto})
        return True
    except Exception as error:
        print('log:', str(error))
        return False