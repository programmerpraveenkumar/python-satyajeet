import psycopg

# host=localhost
# port=5432

conn = psycopg.connect("dbname=ecommerce user=postgres password=roottoor")
cursor = conn.cursor()
cursor.execute("select * from user_db.user_detail")
for record in cursor.fetchall():
        print(record)

cursor.close()
conn.close()