import MySQLdb
import datetime


file = open("haslo.txt", "r")
haslo = file.read()
conn =MySQLdb.connect("localhost","admin",haslo,"bazydanych_db")
cur = conn.cursor()


def printContent():

        query = "SELECT * FROM weather "
        cur.execute(query)
        data = cur.fetchone()
        print "Inside database: "
        print  data

def insertWeatherData(content):
        now = datetime.datetime.now()
        time = now.strftime("%X")
        date = now.strftime("%x")
        with conn:
                query = "INSERT INTO weather_data(IdStation,Date,Hour,Temp, Pressure)\
                         VALUES('{}', '{}', '{}', '{}', '{}')".format(
                                content["id"],
                                date,
                                time,
                                content["temperature"],
                                content["humidity"],
                                content["pressure"]
                        )
                cur.execute(query)
                conn.commit()