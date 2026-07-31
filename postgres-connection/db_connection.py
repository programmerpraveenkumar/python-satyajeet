import psycopg

# host=localhost
# port=5432

with psycopg.connect("dbname=ecommerce user=postgres password=roottoor") as conn:
    with conn.cursor() as cursor:
        cursor.execute("select * from user_db.user_detail limit 3")
        for record in cursor:
            print(record)