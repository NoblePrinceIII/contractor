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

@app.route('/red')
def red_hoodie():
    """Return new hoodie creation page."""
    return render_template('red_hoodie.html')


@app.route('/red', methods=['POST'])
def create_candy():
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

@app.route('/color')
def color_hoodie():
    """Return new hoodie creation page."""
    return render_template('color_hoodie.html')

@app.route('/white')
def white_hoodie():
    """Return new hoodie creation page."""
    return render_template('white_hoodie.html')



# @app.route('/candy/<candy_id>')
# def show_candy(candy_id):
#     """Show a single candy."""
#     candy = candies_collection.find_one({'_id': ObjectId(candy_id)})
#     return render_template('show_candy.html', candy=candy)
#
# def update_candy(candy_id):
#     """Edit page for a candy."""
#     new_candy = {
#         'name': request.form.get('name'),
#         'price': request.form.get('price'),
#         'img_url': request.form.get('img_url')
#     }
#     candies_collection.update_one(
#         {'_id': ObjectId(candy_id)},
#         {'$set': new_candy}
#     )
#     return redirect(url_for('show_candy', candy_id=candy_id))
#
# @app.route('/edit/<candy_id>', methods=['GET'])
# def edit_candy(candy_id):
#     """Page to submit an edit on a candy."""
#     candy = candies_collection.find_one({'_id': ObjectId(candy_id)})
#     return render_template('edit_candy.html', candy=candy)
#
# @app.route('/delete/<candy_id>', methods=['POST'])
# def delete_candy(candy_id):
#     """Delete a candy."""
#     candies_collection.delete_one({'_id': ObjectId(candy_id)})
#     return redirect(url_for('index'))





if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))
