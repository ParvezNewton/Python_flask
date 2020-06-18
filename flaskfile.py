from flask import Flask, request, jsonify,render_template
import firebase_admin
import google.cloud
from firebase_admin import credentials, firestore
import pandas as pd

app = Flask(__name__)

#app credentials for development
#cred = credentials.Certificate("serviceAccountKey.json")


#Our app credentials
cred = credentials.Certificate("ordonserviceAccountkey.json")
firebase_admin.initialize_app(cred)

store = firestore.client()

data_frame =pd.read_excel('Products.xlsx')

@app.route('/')
def homepage():

print("Hello world");
