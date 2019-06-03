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
        date = datetime.date.today()

        id = getServerId(content["id"])
        if id == -1:
            return

        with conn:
                query = "INSERT INTO weather_data(IdStation,Date,Hour,Temp, Pressure)\
                         VALUES('{}', '{}', '{}', '{}', '{}')".format(
                                id,
                                date,
                                time,
                                content["temperature"],
                                content["humidity"],
                                content["pressure"]
                        )
                cur.execute(query)
                conn.commit()


def getServerId(physical_id):
    with conn:
        query = "SELECT IdStation \
                 FROM  weather_station \
                 WHERE IdUser={}".format(physical_id)
        rows_count = cur.execute(query)
        if rows_count > 0:
            return cur.fetchone()
        else:
            return -1
