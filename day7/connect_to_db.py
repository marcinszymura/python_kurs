import psycopg2
try:
    connection = psycopg2.connect(user = "postgres",
                                  password = "qwe123",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "zawodnicy")

    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print ( connection.get_dsn_parameters(),"\n")

    # Print PostgreSQL version
    cursor.execute("SELECT * from zawodnicy;")
    record = cursor.fetchall()
    print("You are connected to - ", record,"\n")

except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
finally:
    # closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")