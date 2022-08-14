import os
from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from src.com.home.work.config.constant import Constant
from firebase_admin import credentials, firestore, initialize_app

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

cred = credentials.Certificate('key.json')
default_app = initialize_app(cred)
db = firestore.client()
client = db.collection('projects')

CORS(app, support_credentials=True)

# db = client.projects
from src.com.home.work.api import routes
