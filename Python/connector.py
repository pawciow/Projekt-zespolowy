import MySQLdb

conn =MySQLdb.connect("localhost","admin","tajnedane","mydb")
cur = conn.cursor()

def printContent():

        query = "SELECT * FROM weather "
        cur.execute(query)
        data = cur.fetchone()
        print "Inside database: "
        print  data

def insertWeatherData(content):
        with conn:
                query = "INSERT INTO weather(Temperature, City, Wind, Country)\
                         VALUES('{}', '{}', '{}', '{}')".format(
                                content["temperature"],
                                content["city"],
                                content["wind"],
                                content["country"]
                        )
                cur.execute(query)
                conn.commit()
