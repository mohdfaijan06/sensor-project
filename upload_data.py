from pymongo.mongo_client import MongoClient
import pandas as pd
import json 

#url 
uri = "mongodb+srv://mohdfaijan775500:Faijan727553@cluster0.eu00y.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# create a new client and connect to server 
client = MongoClient(uri)


# create database name and collection name (and also you can create from mangoDB  )
DATABASE_NAME = "Skills"
COLLECTION_NAME = "waferfault"

df = pd.read_csv("C:\Users\Mohd Faijan\OneDrive\Desktop\sensor_project\notebooks\wafer_23012020_041211.csv") 

df = df.drop("Unnamed: 0" ,axis=1)
df

json_record = list(json.loads(df.T.to_json()).values())

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
