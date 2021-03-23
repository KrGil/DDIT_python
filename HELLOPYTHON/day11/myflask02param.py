from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['post', 'get'])
def hello():
    # param = ''
    # if param != '' :
    param = request.args.get("a", "defaultValue")
    param = request.form['a']
    
    return 'Hello world ' + param

if __name__ == '__main__':
    app.run(host="127.0.0.1", port='80')