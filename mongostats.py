from pymongo import MongoClient
import time
import pickle

def main():
    loaded_pols = []
    client = MongoClient('localhost', 27017)
    politician_db = client['politician_db']
    total_docs = 0
    for i, politician in enumerate(politician_db.list_collection_names()):
        ### change the .find() to something that will accurately reflect number of articles
        print(politician, politician_db[politician].count_documents({}))
        loaded_pols.append(politician)
        total_docs += politician_db[politician].count_documents({})
        if i%8 == 0:
            time.sleep(5)
    #print(loaded_pols)
    print(total_docs, 'articles loaded total')
    pickle.dump(loaded_pols, open('pols_in_mongo.pkl', 'wb'))
main()

