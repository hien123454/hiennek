import os
from firebase_admin import credentials, firestore, initialize_app
import pdb
import firebase_admin
from firebase_admin import credentials
import pandas as pd
cred = credentials.Certificate('home/datakey.json')
default_app = initialize_app(cred)
db = firestore.client()

todo_ref = db.collection('csvjson')
all_todos = [doc.to_dict() for doc in todo_ref.stream()]
data = pd.DataFrame(all_todos)

print(data)




