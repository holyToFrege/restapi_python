import pymysql

connect = pymysql.connect(host='13.125.158.130', user='deploy', password='', db='smartwatercare',charset='utf8mb4')
cur = connect.cursor()
query = "SELECT * FROM pressure_sensors order by getting_time limit 10"
cur.execute(query)
rows = cur.fetchall()
for row in rows:
    print(row)
    
connect.commit()
connect.close()
