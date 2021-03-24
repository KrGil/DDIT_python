from flask import Flask, request, jsonify
from flask.templating import render_template
from day12.templates.mydao import MyEmpDao

app = Flask(__name__, static_url_path="", static_folder="static")

@app.route('/') # 두개 다 넘어간다.
@app.route('/emp')
def emp():
    list = MyEmpDao().getEmps()
    return render_template("emp.html", list = list)

@app.route('/ins.ajax', methods=['POST'])
def ins_ajax():
    data = request.get_json()
    print(data)
    
    sabun = data['sabun']
    e_name= data['e_name']
    dept = data['dept']
    mobile = data['mobile']
    #
    cnt = MyEmpDao().insEmps(sabun, e_name, dept, mobile)
    result = "fail"
    if cnt == 1:
        result = "success"
        
    # print(cnt)
    return jsonify(result = result)

@app.route('/upd.ajax', methods=['POST'])
def upd_ajax():
    data = request.get_json()
    print(data)
    
    sabun = data['sabun']
    e_name= data['e_name']
    dept = data['dept']
    mobile = data['mobile']

    cnt = MyEmpDao().updEmps(sabun, e_name, dept, mobile)
    result = "fail"
    if cnt == 1:
        result = "success"
        
    return jsonify(result = result)

@app.route('/del.ajax', methods=['POST'])
def del_ajax():
    data = request.get_json()
    print(data)
    
    sabun = data['sabun']
    
    cnt = MyEmpDao().delEmps(sabun)
    result = "fail"
    if cnt == 1:
        result = "success"
        
    return jsonify(result = result)

if __name__ == '__main__':
    app.run(host="127.0.0.1", port='80')