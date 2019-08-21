from flask import Flask,jsonify, request
from flask_restful import Api, Resource
import requests
import wget

app=Flask(__name__)
#app=Api(api)

#class UNIQUE_ID(Resource):
#    def post(self):
#        #get link
#        link= request.get_json()
#        url=link["url"]
#        
#        #start downloading
#        #generate and return unique id
#        
#class PAUSE(Resource): 
#    def post(self):
#        pass
#        
#class DOWNLOAD_INFO(Resource):
#    def get(self):
#        pass

        
def bar1(current,total,width=80):
    print("finished:%d , remianing:%d"%(current,total-current))
@app.route('/api/check')
def test():
    
    url = 'http://i3.ytimg.com/vi/J---aiyznGQ/mqdefault.jpg'
    r = requests.get(url)
    print(r)
    print('Beginning file download with wget module')

    url = 'http://i3.ytimg.com/vi/J---aiyznGQ/mqdefault.jpg'
    
    status= wget.download(url,bar=bar1)
    print(status)

    # Retrieve HTTP meta-data
    print(status.status_code)
    print(status.headers['content-type'])
    print(status.encoding)
    return '<html><body><h1>broi '+str(status.status_code)+'</h1></body></html>'

if __name__ =='__main__':
    app.run(host='localhost',port=5000)
    print('<html><body><h1>broi</h1></body></html>')
    

