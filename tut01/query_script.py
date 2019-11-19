from db.db_utils import db_connect

con = db_connect()
cur = con.cursor()

# view cur obj and just created tables
print(cur.execute("select name from sqlite_master where type='table'"))
print(cur.fetchall())

print(cur.execute("""
select name from sqlite_master where type='table' and name='customers'
"""))
print(cur.fetchone()[0])
