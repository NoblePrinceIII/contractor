from flask import Flask, render_template, redirect, url_for, request
from pymongo import MongoClient
from bson.objectid import ObjectId
from functools import reduce
import os

app = Flask(__name__)

host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/my_app_db')
client = MongoClient(host=f"{host}?retryWrites=false")
db = client.get_default_database()

hoodie_collection = db.hoodies

@app.route('/')
def index():
    """Return homepage."""
    return render_template('index.html', hoodies=hoodie_collection.find())

@app.route('/new')
def new_hoodie():
    """Return new hoodie creation page."""
    return render_template('new_hoodie.html')



if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))
