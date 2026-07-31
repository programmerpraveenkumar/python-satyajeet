import psycopg

# host=localhost
# port=5432
def getConnection():
    conn = psycopg.connect("dbname=ecommerce user=postgres password=roottoor")
    return conn
