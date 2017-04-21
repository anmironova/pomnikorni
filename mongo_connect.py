from flask import Flask
from flask import jsonify
from flask import request
#from flask.ext.pymongo import PyMongo
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'heroku_5zh4h6hd'
app.config['charset'] = 'utf8'
app.config['MONGO_URI'] = 'mongodb://heroku_5zh4h6hd:cq4eb0novbqq50k8aeg0oee4rb@ds111461.mlab.com:11461/heroku_5zh4h6hd'

mongo = PyMongo(app)

@app.route('/', methods=['GET'])
def index():
    return jsonify({'message' : "hello loser"})


@app.route('/place', methods=['GET'])
def get_all_places():
  place = mongo.db.places
  output = []
  for s in place.find():
    output.append({'place_name' : s['place_name'], 'place_lan' : s['place_lan'], 'place_lon' : s['place_lon']})
  return jsonify({'result' : output})

@app.route('/place/<string:place_name>', methods=['GET'])
def get_one_place(place_name):
  place = mongo.db.places
  output = []
  s = place.find_one({'place_name' : place_name})
  if s:
    output = {'place_name' : s['place_name'], 'place_lan' : s['place_lan'], 'place_lon' : s['place_lon']}
 # else:0
 #   output = "No such name"
  return jsonify({'result' : output})

@app.route('/add')
def add():
	user = mongo.db.users
	user.insert({'name' : 'mamastasia'})
	return 'Add User!'


if __name__ == '__main__':
    app.run(debug=True)
    