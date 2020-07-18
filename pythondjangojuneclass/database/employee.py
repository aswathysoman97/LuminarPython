import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Password@123",
    database="luminar",
    auth_plugin="caching_sha2_password"
)
print (db)
cursor=db.cursor()
cursor.execute("DROP TABLE IF EXISTS EMPLO")
sql="""CREATE TABLE EMPLO(NAME CHAR(20),
    AGE INT,
    SEX CHAR(1),
    SALARY FLOAT)"""
try:
    cursor.execute(sql)
except Exception as e:
    print(e.args)
db.close()