__author__ = 'Tim Berla'

import pymssql
conn = pymssql.connect(host='mss1.cxtheffccik1.us-west-2.rds.amazonaws.com:1433', user='root', password='1deadparrot', database='topaz2')
cur = conn.cursor()
cur.execute("SELECT * FROM dailydemo2")

row = cur.fetchone()
while row:
    print ("row: " , row)
    row = cur.fetchone()

conn.close()

