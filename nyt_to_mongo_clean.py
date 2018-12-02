#!/Users/aaronfrederick/Desktop/venv python

from pymongo import MongoClient
from nytimesarticle import articleAPI
import time
import pandas as pd
import pickle


def date_query(date):
    if len(str(date.month)) == 2 and len(str(date.day)) == 2:
        date_string = int(str(date.year)+str(date.month)+str(date.day))
    elif len(str(date.month)) == 1:
        if len(str(date.day)) == 1:
            date_string = int(str(date.year)+'0'+str(date.month)+'0'+str(date.day))
        else:
            date_string = int(str(date.year)+'0'+str(date.month)+str(date.day))
    return date_string


def main():
    client = MongoClient('localhost', 27017)
    politician_db = client['politician_db']
    api = articleAPI('API KEY')
    df = pd.read_pickle('pol_df.pkl')
    already_loaded = pickle.load(open('pols_in_mongo.pkl', 'rb'))
    #print(already_loaded)


    pol_list = df.Name

    for politician in pol_list:
        article_pages = []
        time.sleep(1)
        df_entry = df[df.Name == politician]
        #create collection for politician
        politician_col = politician_db[df_entry['collectionname'][df_entry.index[0]]]
        if df_entry['collectionname'][df_entry.index[0]] in already_loaded:
            print(politician, 'is already in the database')
            continue
        #Set up Query
        beg_d = df_entry['Entered Office'][df_entry.index[0]]
        end_d = df_entry['Exited Office'][df_entry.index[0]]


        #print(beg_d,end_d)
        try:
            beg_d_in = date_query(beg_d)
            # if politician == 'abraham lincoln':
            #     print(beg_d_in, end_d_in)
        except:
            print(politician, end=' ')
            print('Failed at the beginning date step')

        if type(end_d) == str:
            try:
                done = False
                page = 1
                while not done:
                    time.sleep(1)
                    search = api.search(q=politician,
                                        begin_date=beg_d_in,
                                        page = page)
                    politician_col.insert_many(search['response']['docs'])
                    print(politician, page)
                    page += 1
                    if len(search['response']['docs'])%10 != 0 or len(search['response']['docs'])==0:
                        done = True
                print(f'Successful query for {politician};', end=' ')
            except:
                print(politician, end=' ')
                print('failed their attempt to get into our database :(')
        else:
            try:
                end_d_in = date_query(end_d)
                done = False
                page = 1
                while not done:
                    time.sleep(1)
                    search = api.search(q=politician,
                                        begin_date=beg_d_in,
                                        end_date = end_d_in,
                                        page=page)
                    politician_col.insert_many(search['response']['docs'])
                    print(politician, page)
                    page += 1
                    if len(search['response']['docs']) % 10 != 0 or len(search['response']['docs']) == 0:
                        done = True
                print(f'Successful query for {politician};')
            except:
                print(politician, end=' ')
                print('failed their attempt to get into our database :(')

main()