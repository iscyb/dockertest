from flask import Flask
from flask import jsonify
import requests


app = Flask(__name__)

@app.route('/')
def home():
    return('Yoyo')

@app.route('/reach_backend', methods = ['GET'])
def reach_backend():
    a = requests.post(url = 'http://backend-app/backend', json = {'x': 2})
    return jsonify(a.json())
    

#@app.route('/frontend', method = ['POST'])
#def frontend():
#    x = float(request.json.get('x'))
#    from_backend =  123

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80) #80 is exposed in the Dockerfile