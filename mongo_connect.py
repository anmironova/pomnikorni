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

coord = [ 60.600884, 56.911172 ]
def calc():
  #jsonstr = json.loads(output)
  #lon = float(jsonstr['obj1']['loc']['coordinates'][0])
  #lat = float(jsonstr['obj1']['loc']['coordinates'][1])
  diff_lat = coord[0] - lon
  diff_lon = coord[1] - lat

  if diff_lon <= 0.006 and diff_lat <= 0.006:
    return('Успех')

  elif diff_lon <= 0.01 and diff_lat <= 0.01:
    return('Ближе, чем ты думаешь')

  elif diff_lon <= 0.06 and diff_lat <= 0.06:
    return('Ближе')

  else:
   return('Ты очень далеко')

@app.route('/', methods=['GET'])
def index():
    return jsonify({'message' : "hello"})

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

@app.route('/trail/obj1', methods=['GET'])
def get_one_trail1():
  trail = mongo.db.trails
  output = []
  for s in trail.find():
    output.append({'obj1' : s['obj1']})
    lon = float(output['obj1']['loc']['coordinates'][0])
    lat = float(output['obj1']['loc']['coordinates'][1])
  return (calc()) 

@app.route('/trail/obj2', methods=['GET'])
def get_one_trail2():
  trail = mongo.db.trails
  output = []
  for s in trail.find():
    output.append({'obj2' : s['obj2']})
    lon = float(output['obj2']['loc']['coordinates'][0])
    lat = float(output['obj2']['loc']['coordinates'][1])
  return (calc())  


@app.route('/trail/obj3', methods=['GET'])
def get_one_trail3():
  trail = mongo.db.trails
  output = []
  for s in trail.find():
    output.append({'obj3' : s['obj3']})
    lon = float(output['obj3']['loc']['coordinates'][0])
    lat = float(output['obj3']['loc']['coordinates'][1])
  return (calc()) 


@app.route('/trail/obj4', methods=['GET'])
def get_one_trail4():
  trail = mongo.db.trails
  output = []
  for s in trail.find():
    output.append({'obj4' : s['obj4']})
    lon = float(output['obj4']['loc']['coordinates'][0])
    lat = float(output['obj4']['loc']['coordinates'][1])
  return (calc()) 



@app.route('/trail/obj5', methods=['GET'])
def get_one_trail5():
  trail = mongo.db.trails
  output = []
  for s in trail.find():
    output.append({'obj5' : s['obj5']})
    lon = float(output['obj5']['loc']['coordinates'][0])
    lat = float(output['obj5']['loc']['coordinates'][1])
  return (calc())  

@app.route('/trail/obj6', methods=['GET'])
def get_one_trail6():
  trail = mongo.db.trails
  output = []
  for s in trail.find():
    output.append({'obj6' : s['obj6']})
    lon = float(output['obj6']['loc']['coordinates'][0])
    lat = float(output['obj6']['loc']['coordinates'][1])
  return (calc())  

@app.route('/trail/obj7', methods=['GET'])
def get_one_trail7():
  trail = mongo.db.trails
  output = []
  for s in trail.find():
    output.append({'obj7' : s['obj7']})
    lon = float(output['obj7']['loc']['coordinates'][0])
    lat = float(output['obj7']['loc']['coordinates'][1])
  return (calc())  

@app.route('/trail/obj8', methods=['GET'])
def get_one_trail8():
  trail = mongo.db.trails
  output = []
  for s in trail.find():
    output.append({'obj8' : s['obj8']})
    lon = float(output['obj8']['loc']['coordinates'][0])
    lat = float(output['obj8']['loc']['coordinates'][1])
  return (calc()) 

@app.route('/trail/obj9', methods=['GET'])
def get_one_trail9():
  trail = mongo.db.trails
  output = []
  for s in trail.find():
    output.append({'obj9' : s['obj9']})
    lon = float(output['obj9']['loc']['coordinates'][0])
    lat = float(output['obj9']['loc']['coordinates'][1])
  return (calc())   

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


@app.route('/add')
def add():
	user = mongo.db.users
	user.insert({'name' : 'mamastasia'})
	return 'Add User!'

if __name__ == '__main__':
	 app.run(debug=True)
	
