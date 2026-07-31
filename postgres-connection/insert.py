from db_config import getConnection

def select():
    connection = getConnection()
    cursor = connection.cursor()
    cursor.execute("select * from user_db.user_detail")
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    connection.close()


def insert():
    connection = getConnection()
    cursor = connection.cursor()

    cursor.execute("insert into user_db.user_detail(name)values('11july')")
    # connection.commit()
    # connection.rollback()
    print("insert into db")
    cursor.close()
    connection.close()
    
# insert()

# # banking
# # 500
# # a to b