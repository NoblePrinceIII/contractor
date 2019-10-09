from flask import Flask, render_template, redirect, url_for, request
from pymongo import MongoClient
from bson.objectid import ObjectId
from functools import reduce
import os

app = Flask(__name__)

host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/my_app_db')
client = MongoClient(host=f"{host}?retryWrites=false")
db = client.get_default_database()

hoodies_collection = db.hoodies


@app.route('/')
def index():
    """Return homepage."""
    return render_template('index.html', hoodies=hoodies_collection.find())

@app.route('/red')
def red_hoodie():
    """Return new hoodie creation page."""
    return render_template('red_hoodie.html')


@app.route('/red', methods=['POST'])
def create_hoodie():
    """Make a new hoodie according to user's specifications."""
    hoodie = {
        'name': request.form.get('name'),
        'price': request.form.get('price'),
        'img_url': request.form.get('img_url')
    }
    hoodie_id = hoodies_collection.insert_one(hoodie).inserted_id
    return redirect(url_for('show_hoodie', hoodie_id=hoodie_id))




@app.route('/blue')
def blue_hoodie():
    """Return new hoodie creation page."""
    return render_template('blue_hoodie.html')


@app.route('/blue', methods=['POST'])
def create_hoodie_blue():
    """Make a new hoodie according to user's specifications."""
    hoodie = {
        'name': request.form.get('name'),
        'price': request.form.get('price'),
        'img_url': request.form.get('img_url')
    }
    hoodie_id = hoodies_collection.insert_one(hoodie).inserted_id
    return redirect(url_for('show_hoodie', hoodie_id=hoodie_id))


@app.route('/color')
def color_hoodie():
    """Return new hoodie creation page."""
    return render_template('color_hoodie.html')

@app.route('/color', methods=['POST'])
def create_hoodie_color():
    """Make a new hoodie according to user's specifications."""
    hoodie = {
        'name': request.form.get('name'),
        'price': request.form.get('price'),
        'img_url': request.form.get('img_url')
    }
    hoodie_id = hoodies_collection.insert_one(hoodie).inserted_id
    return redirect(url_for('show_hoodie', hoodie_id=hoodie_id))


@app.route('/white')
def white_hoodie():
    """Return new hoodie creation page."""
    return render_template('white_hoodie.html')


@app.route('/white', methods=['POST'])
def create_hoodie_white():
    """Make a new hoodie according to user's specifications."""
    hoodie = {
        'name': request.form.get('name'),
        'price': request.form.get('price'),
        'img_url': request.form.get('img_url')
    }
    hoodie_id = hoodies_collection.insert_one(hoodie).inserted_id
    return redirect(url_for('show_hoodie', hoodie_id=hoodie_id))





@app.route('/hoodie/<hoodie_id>')
def show_hoodie(hoodie_id):
    """Show a single hoodie."""
    hoodie = hoodies_collection.find_one({'_id': ObjectId(hoodie_id)})
    return render_template('show_hoodie.html', hoodie=hoodie)

@app.route('/<hoodie_id>', methods=['POST'])
def update_hoodie(hoodie_id):
    """Edit page for a hoodie."""
    new_hoodie = {
        'name': request.form.get('name'),
        'price': request.form.get('price'),
        'img_url': request.form.get('img_url')
        }
    hoodies_collection.update_one(
        {'_id': ObjectId(hoodie_id)},
        {'$set': new_hoodie}
    )
    return redirect(url_for('show_hoodie', hoodie_id=hoodie_id))


@app.route('/edit/<hoodie_id>', methods=['GET'])
def edit_hoodie(hoodie_id):
    """Page to submit an edit on a hoodie."""
    hoodie = hoodies_collection.find_one({'_id': ObjectId(hoodie_id)})
    return render_template('edit_hoodie.html', hoodie=hoodie)


@app.route('/delete/<hoodie_id>', methods=['POST'])
def delete_hoodie(hoodie_id):
    """Delete a hoodie."""
    hoodies_collection.delete_one({'_id': ObjectId(hoodie_id)})
    return redirect(url_for('index'))


if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))
