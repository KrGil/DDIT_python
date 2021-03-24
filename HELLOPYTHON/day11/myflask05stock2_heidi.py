from flask import Flask, request
from flask import render_template
from day11.myheidi02_json import getStocks

app = Flask(__name__)

@app.route('/')
def myindex():
    return render_template('index.html')

@app.route('/stock', methods =['get','post'])
def mylist():
    s_name = request.form["s_name"]
    list = getStocks(s_name)
    print(list)
    return render_template('stock_json.html', list = list, s_name = s_name)

if __name__ == '__main__':
    app.run(host="127.0.0.1", port='80')