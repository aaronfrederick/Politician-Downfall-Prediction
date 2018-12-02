from bs4 import BeautifulSoup
import requests
import re
from pymongo import MongoClient
import time

client = MongoClient('localhost', 27017)
politician_db = client['politician_db']


for collection in politician_db.list_collection_names():
    print(collection)
    col = politician_db[collection]
    for doc in col.find():
        time.sleep(1.5)
        try:
            url = doc['web_url']
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'lxml')
            text = []
            for item in soup.findAll('p'):
                s = item.text.lower()
                s = re.sub('[^A-Za-z ]', '', s)
                text.append(s)
            submission = ' '.join(text)
            try:
                result = col.find_one_and_update({'web_url' : url}, {'$set':{"full_text" : submission}})
                print(f'Successful Run for {collection}')
            except:
                print('Error in updating phase')
        except:
            print('Error in scraping phase')
