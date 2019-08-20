from flask import Flask,jsonify, request
from flask_restful import Api, Resource
import requests

app=Flask(__name__)
app=Api(api)

class UNIQUE_ID(Resource):
    def post(self):
        #get link
        link= request.get_json()
        url=link["url"]
        
        #start downloading
        #generate and return unique id
        
class PAUSE(Resource): 
    def post(self):
        
class DOWNLOAD_INFO(Resource):
    def get(self):

        
@app.route('/api/check')
def test():
    return 'broi'

if __name__ =='__main__':
    app.run(host='localhost',port=5000)

