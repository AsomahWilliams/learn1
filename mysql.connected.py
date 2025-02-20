import mysql.connector

try:
    cnx = mysql.connector.connect(
        user='root',
        password='qwerty123',
        host='127.0.0.1',
        database='app'
    )
    print("Connected to MySQL database")
except mysql.connector.Error as err:
    print("Error connecting to MySQL database: {}".format(err))
except Exception as e:
    print("An unexpected error occurred: {}".format(e))
else:
    # If no exceptions occurred, you can perform database operations here
    
    
    # If no exceptions occurred, you can perform database operations here
    cursor = cnx.cursor()
    # ...
finally:
    if 'cnx' in locals():
        cnx.close()


