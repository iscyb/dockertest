from flask import Flask
from flask import make_response
from flask import request
from flask import jsonify


app = Flask(__name__)

@app.route('/')
def home():
    return('This the backend shoo shoo')

@app.route('/backend', methods = ['POST'])
def backend():
    x = float(request.json.get('x'))
    y = 2*x
    response = {'y':y}
    return make_response(jsonify(response), 400)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80) #80 is exposed in the Dockerfile