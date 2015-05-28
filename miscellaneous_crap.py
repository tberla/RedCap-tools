__author__ = 'od0236'


__author__ = 'od0236'


import pymssql
conn = pymssql.connect(host='mss1.cxtheffccik1.us-west-2.rds.amazonaws.com:1433', user='root', password='1deadparrot', database='topaz2')
cur = conn.cursor()





cur.execute("select table_name from information_schema.tables")
#   cur.execute("select * from trail1")
row = cur.fetchone()
while row:
#    print "ID=%d, Name=%s" % (row[0], row[1])
    print ("table name = " , row[0])
    row = cur.fetchone()

# if you call execute() with one argument, you can use % sign as usual
# (it loses its special meaning).
cur.execute("SELECT * FROM Emerge_Output")



row = cur.fetchone()
while row:
#    print "ID=%d, Name=%s" % (row[0], row[1])
    print ("table name = " , row[0])
    row = cur.fetchone()




conn.close()

print ("yahoooo")


from sqlalchemy import *

db = create_engine('sqlite:///tutorial.db')

db.echo = False  # Try changing this to True and see what happens

metadata = BoundMetaData(db)

users = Table('users', metadata,
    Column('user_id', Integer, primary_key=True),
    Column('name', String(40)),
    Column('age', Integer),
    Column('password', String),
)
users.create()

i = users.insert()
i.execute(name='Mary', age=30, password='secret')
i.execute({'name': 'John', 'age': 42},
          {'name': 'Susan', 'age': 57},
          {'name': 'Carl', 'age': 33})

s = users.select()
rs = s.execute()

row = rs.fetchone()
print 'Id:', row[0]
print 'Name:', row['name']
print 'Age:', row.age
print 'Password:', row[users.c.password]

for row in rs:
    print row.name, 'is', row.age, 'years old'

    ========================================