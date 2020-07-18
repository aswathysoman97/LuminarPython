import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Password@123",
    database="luminar",
    auth_plugin="caching_sha2_password"
)
# print (db)
cursor=db.cursor()
sql="""INSERT INTO EMPLO(NAME,AGE,SEX,SALARY)VALUES('ASWATHY',20,'F',20000)"""
try:
    cursor.execute(sql)
    db.commit()
except Exception as e:
    print(e.args)
db.close()