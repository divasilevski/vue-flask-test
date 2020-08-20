from flask import Flask, jsonify, render_template, request
from flask_cors import CORS, cross_origin

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__, static_folder='../dist/static', template_folder='../dist/templates')
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r"/api/*": {"origins": "*"}})

# sanity check route
@app.route('/ping', methods=['GET'])
@cross_origin()
def ping():
    return jsonify('pong!')

@app.route('/pong', methods=['POST'])
@cross_origin()
def pong():
    file = request.files['file']
    read = file.read()
    return read

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()