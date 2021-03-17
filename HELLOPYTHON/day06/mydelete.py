# 삭제하기
import pymysql

gil_db = pymysql.connect(
    user='root', 
    passwd='python', 
    host='127.0.0.1', 
    db='python', 
    charset='utf8'
)
cursor = gil_db.cursor(pymysql.cursors.DictCursor)

sql = """
        DELETE FROM sample 
        WHERE col01=%s 
        """
cnt = cursor.execute(sql,('6'))
print("cnt",cnt)
gil_db.commit()
gil_db.close()