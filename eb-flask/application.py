from flask import Flask
application = Flask(__name__)
from flask import request, url_for
from flask import render_template
from flask_socketio import SocketIO
from flask_socketio import send, emit
import urllib
import requests
import json
from thread import *

#fetching data from elasticsearch backend, parsing the data into json format
def coordinate(word):
    r = requests.get("" + word + "&size=1000")
    output_coord = []
    dic = json.loads(json.dumps(r.json()))
    length = len(dic["hits"]["hits"])
    for i in xrange(0,length):
        coord = [float(dic['hits']['hits'][i]['_source']['geo'][0]),float(dic['hits']['hits'][i]['_source']['geo'][1])]
        output_coord.append(coord)
    return output_coord

from flask import session

@application.route('/')
def index():
    return render_template('index.html')


socketio = SocketIO(application)
@socketio.on('connect')
def test_connect():
    print('Client connected')
    

@socketio.on('message')
def handle_message(message):
    results = coordinate(message)
    json_Results = json.dumps(results)
    # print (resultsJSON)
    send(json_Results)

if __name__ == '__main__':
	socketio.run(application,debug=True)
