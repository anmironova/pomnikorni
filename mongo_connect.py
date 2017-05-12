from flask import Flask
from flask import jsonify
from flask import request
import json
#from app import app

from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'heroku_5zh4h6hd'
app.config['charset'] = 'utf8'
app.config['MONGO_URI'] = 'mongodb://<dbuser>:<dbpassword>@ds111461.mlab.com:11461/heroku_5zh4h6hd'

mongo = PyMongo(app)


@app.route('/', methods=['GET'])
def index():
    return jsonify({'message' : "hello"})


@app.route('/coord', methods=['GET'])
def near():
  trail = mongo.db.trails
 # output = []
  #for s in trail.aggregate()
  #output = trail.aggregate([{'$geoNear': { 'near' : { type: "Point", 'coordinates': [60.608783, 56.835970] }, 'distanceField': "dist.calculated", 'maxDistance': 100, 'includeLocs' : "dist.location", 'spherical': "true"}}])
  output = trail.find({'address.loc': { '$near': { '$geometry': { type : "Point", 'coordinates': [60.608783, 56.835970] }, '$maxDistance' :100 }}})
  for s in output:
    print(s)
  return jsonify({'result': s})
  #for s in trail.find():
  #  output.append({'address.loc': { '$near': { '$geometry': { type : "Point", 'coordinates': [60.608783, 56.835970] }, '$maxDistance' :100 }}})
  #return jsonify(output)

@app.route('/place', methods=['GET'])
def get_all_places():
  place = mongo.db.places
  output = []
  for s in place.find():
    output.append({'place_name' : s['place_name'], 'place_lan' : s['place_lan'], 'place_lon' : s['place_lon']})
  return jsonify({'result' : output})


@app.route('/trail', methods=['GET'])
def get_all_trails():
  trail = mongo.db.trails
  output = []
  for s in trail.find():
    output.append({'trail_name' : s['trail_name'], 'obj1' : s['obj1'] })
  return jsonify({'result' : output})


@app.route('/place/lanlon/<string:place_name>', methods=['GET'])
def get_one_lanlon(place_name):
  place = mongo.db.places
  output = []
  s = place.find_one({'place_name' : place_name})
  if s:
    output = {'lan' : s['place_lan'], 'lon' : s['place_lon']}
  return jsonify({'result' : output})

@app.route('/place/alllanlon', methods=['GET'])
def get_all_lanlon():
  place = mongo.db.places
  output = []
  for s in place.find():
    output.append({'place_lan' : s['place_lan'], 'place_lon' : s['place_lon']})
  return jsonify({'result' : output})


@app.route('/place/info/<string:place_name>', methods=['GET'])
def get_one_info(place_name):
  place = mongo.db.places
  output = []
  s = place.find_one({'place_name' : place_name})
  if s:
    output = {'place_name' : s['place_name'], 'info' : s['place_info']}
  return jsonify({'result' : output})



if __name__ == '__main__':
	 app.run(debug=True)
	