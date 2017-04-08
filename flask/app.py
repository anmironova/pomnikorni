from flask import Flask, jsonify, request
app = Flask(__name__)

addresses = [
{
'location' : '56.844494, 60.653655',
'name' : 'URFU'
},
{
'location' : '56.840469, 60.597754',
'name' : 'Theather'
}, 
{
'location' : '56.837956, 60.596268',
'name' : 'Square'
}]

@app.route('/', methods=['GET'])
def index():
    return jsonify({'message' : "hello"})

@app.route('/addr', methods=['GET'])
def returnAll():
    return jsonify({'addresses' : addresses})

@app.route('/addr/<string:name>', methods=['GET'])
def returnOne(location):
	addr = [address for address in addresses if address['location'] == location]
	return jsonify({'address' : addr[0]})

@app.route('/addr', methods=['POST'])
def addOne():
	address = {'location' : request.json['location']}

	addresses.append(address)
	return jsonify({'adresses' : addresses})


@app.route('/addr', methods=['PUT'])
def editOne(location):
	addr = [address for address in adresses if address['location'] == location]
	addr[0]['location'] = request.json['location']
	return jsonify({'address' : addr[0]})


if __name__ == "__main__":
    app.run(debug=True, port=8080)
