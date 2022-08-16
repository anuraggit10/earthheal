import os
from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from src.com.home.work.config.constant import Constant
from firebase_admin import credentials, firestore, initialize_app
from google.cloud import storage


app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

CLOUD_STORAGE_BUCKET = os.environ['CLOUD_STORAGE_BUCKET']


gcs = storage.Client()
bucket = gcs.get_bucket(CLOUD_STORAGE_BUCKET)

cred = credentials.Certificate('key.json')
default_app = initialize_app(cred)
db = firestore.client()
client = db.collection('projects')

CORS(app, support_credentials=True)

# db = client.projects
from src.com.home.work.api import routes
