import os
from datetime import datetime
from pymongo import MongoClient
from bson.objectid import ObjectId
from pprint import pprint

# Define connection to MongoDB
pwd = os.environ.get("MONGO_PWD")
host = 'localhost'
port = 27017
uri = f"mongodb://admin:{pwd}@{host}:{port}/?serverSelectionTimeoutMS=" \
      f"5000&connectTimeoutMS=10000&authSource=admin&authMechanism=SCRAM-SHA-256"


def insert_many(collection):
    names = ['Pedro López', 'Julia García', 'Amparo Mayoral', 'Juan Martínez']
    ages = [25, 22, 28, 30]
    emails = ['pedro@eip.com', 'julia@eip.com', 'amparo@eip.com',
              'juan@eip.com']
    grades = [5.2, 7.3, 8.4, 6.8]

    documents = []

    for name, age, email, grade in zip(names, ages, emails, grades):
        document = {
            'name': name,
            'age': age,
            'email': email,
            'grade': grade,
            # "datetime.datetime" in format str to "datetime.datetime" modified
            'date': datetime.strptime(datetime.now().strftime(
                "%d-%m-%Y %H:%M:%S"), "%d-%m-%Y %H:%M:%S")
        }
        documents.append(document)

    try:
        collection.insert_many(documents)
        print('INSERTED documents: Done!.')
    except Exception as e:
        print(f'INSERT error:\n{e}')


def mdb_update(collection, doc_id, doc_update):
    _id = ObjectId(doc_id)
    try:
        collection.update_one({'_id': _id}, doc_update)
    except Exception as e:
        print(f'UPDATE to {id} ERROR:\n{e}')


def update(collection):
    names = ['Amparo Mayoral', 'Juan Martínez']
    grades = [9.3, 7.2]

    updates = []

    # Create updates documents
    for grade in grades:
        doc_update = {
            '$set': {'grade': grade}
        }
        updates.append(doc_update)

    # Look for id by name
    i = 0
    for name in names:
        # Find the name in document
        query = collection.find_one({'name': name})
        # Update with the id and update[i] document
        mdb_update(collection, query['_id'], updates[i])
        print(f"UPDATE _id {query['_id']}:Done!.")
        i += 1


def read(collection):
    try:
        # Find and count all the documents in collection
        documents = collection.find()
        total = collection.count_documents({})

        # Print documents
        print(f'Total de documentos en {collection.full_name}: {total}\n')
        for document in documents:
            pprint(document)

    except Exception as e:
        print(f'READ error:\n{e}')


def ej_4(collection):
    '''
    Find 7 < grade < 7.5
    :param collection: Collection to operate
    '''
    # Create our conditions for the query
    query = {'grade': {'$gte': 7.0, '$lte': 7.5}}
    # Total
    try:
        total = collection.count_documents(query)

        print(f'Documentos para la busqueda: {total}\n')
        if total > 0:
            # Find documents for the query
            search = collection.find(query)
            for document in search:
                pprint(document)
    except Exception as e:
        print(f'QUERY error:\n{e}')


def delete(collection):
    # Define our query to find Pedro López
    query = {'name': {'$regex': 'Pedro López{1}'}}

    try:
        # Execute DELETE of the query
        result = collection.delete_many(query)

        print(f'Total de documentos borrados: {result.deleted_count}')
    except Exception as e:
        print(f'DELETE error:\n{e}')


if __name__ == '__main__':
    # Create MongoClient and db connection
    client = MongoClient(uri)
    db = client.actividad
    # INSERT
    insert_many(collection=db.notas)
    # UPDATE
    update(collection=db.notas)
    # READ
    read(collection=db.notas)
    # Exercise 4
    ej_4(collection=db.notas)
    # DELETE
    delete(collection=db.notas)
