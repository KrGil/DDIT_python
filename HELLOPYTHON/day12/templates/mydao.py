import pymysql
from numba.core.datamodel.testing import DataModelTester

class MyEmpDao:
    def __init__(self):
        pass
    
    def getEmps(self):
        ret = [] 
        conn = pymysql.connect(
            user='root', 
            passwd='python', 
            host='127.0.0.1', 
            db='python', 
            charset='utf8'
        )
        cur = conn.cursor()
        
        #* 쓰는걸 지양하자. 파이썬 ;이 있거나 없거나 상관이 없다.
        sql = "SELECT sabun, e_name, dept, mobile FROM emp;"
        cur.execute(sql)
        rows = cur.fetchall()
        for e in rows:
            temp = {'sabun' : e[0], "e_name" : e[1], "dept": e[2], "mobile" : e[3] }
            ret.append(temp)
            
        conn.close()
        return ret

    def getEmp(self, sabun):
        ret = [] 
        conn = pymysql.connect(
            user='root', 
            passwd='python', 
            host='127.0.0.1', 
            db='python', 
            charset='utf8'
        )
        cur = conn.cursor()
        
        #* 쓰는걸 지양하자. 파이썬 ;이 있거나 없거나 상관이 없다.
        sql = "SELECT sabun, e_name, dept, mobile FROM emp where sabun = %s"
        cur.execute(sql, (sabun))
        rows = cur.fetchall()
            
        conn.close()
        return rows
    
    def insEmps(self, sabun, e_name, dept, mobile):
        gil_db = pymysql.connect(
            user='root', 
            passwd='python', 
            host='127.0.0.1', 
            db='python', 
            charset='utf8'
        )
        cursor = gil_db.cursor(pymysql.cursors.DictCursor)
        
        sql = "INSERT INTO emp (sabun, e_name, dept, mobile) VALUES (%s, %s, %s, %s)"
        cnt = cursor.execute(sql,(sabun, e_name, dept, mobile))

        gil_db.commit()
        gil_db.close()
        
        return cnt

    def updEmps(self, sabun, e_name, dept, mobile):
        gil_db = pymysql.connect(
            user='root', 
            passwd='python', 
            host='127.0.0.1', 
            db='python', 
            charset='utf8'
        )
        cursor = gil_db.cursor(pymysql.cursors.DictCursor)
        
        sql = "update emp set e_name=%s, dept=%s, mobile=%s WHERE sabun = %s"
        cnt = cursor.execute(sql,(e_name, dept, mobile,sabun ))

        gil_db.commit()
        gil_db.close()
        
        return cnt

    def delEmps(self, sabun):
        gil_db = pymysql.connect(
            user='root', 
            passwd='python', 
            host='127.0.0.1', 
            db='python', 
            charset='utf8'
        )
        cursor = gil_db.cursor(pymysql.cursors.DictCursor)
        
        sql = "delete FROM emp WHERE sabun = %s"
        cnt = cursor.execute(sql,(sabun))

        gil_db.commit()
        gil_db.close()
        
        return cnt
    

    
if __name__ == '__main__':
    # select
    # list = MyEmpDao().getEmps()
    # print(list)
    
    # insert
    # cnt = MyEmpDao().insEmps('3','3','3','3')
    # print(cnt)
    
    # update
    # cnt = MyEmpDao().updEmps('3','4','4','4')
    # print(cnt)
    
    # delete
    cnt = MyEmpDao().delEmps('3')
    print(cnt)
    
    
    

