from flask import Flask
from flask import request
import json


app = Flask(__name__, static_url_path='', static_folder='static')

@app.route('/')
def index():
    #return send_file('./web/static/index.html')
    return app.send_static_file('index.html')
    
@app.route('/ip')
def ip():
    return json.dumps({"client": request.remote_addr})

app.run(host='0.0.0.0', port=8182)


