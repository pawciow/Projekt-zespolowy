# Backend projektu
Backend projektu skłąda się z trzech głównych rzeczy:
- Serwera nasłuchującego na przychodzące zapytania
- Konektora do bazy danych
- Bota zaludniającego

Serwer nasłuchujący powstał, aby uprościć komunikację bazy danych z urządzeniami w terenie.
 Konektor wymagany był
## Serwer nasłuchujący do bazy danych
W tej części projektu należało zrobić serwer pośredniczący między pomiarami wysłyanymi do głównego serwera, a bazą danych. <br>
Technologią użytą do tego został Pythonowy Torando. Ma on funkcję nasłuchiwania na danym porcie i obsługi dowolnych zapytań http : post i get.
W pierwszej części serwer nasłuchuję na porcie 8888. Gdy dostanie GET'a, to serwer najpierw zapisuje całe zapytanie. Dalej, za pomocą biblioteki JSON parsuje dane zapytanie. Następnie, przekazuje je do konektora.
## Konektor
Dany konektor łączy się z bazą daynch i wrzuca dane do odpowiedniej tabeli.
## Zaludnianie bazy danych
Najważniesjzym narzędziem testowym jest bot służący o zaludniania naszej bazy. Korzysta on z bardzo powszechnego WEB-APi OpenWeatherMap. Pozwala On na wyłyanie zapytań do bazy. Komunikacja z nim opiera się na REST api.
Bot ten co określony interwał: Wysyła odpowiednio skonstruowane zapytanie do webapi. W dalszej części parsuje odpowiedź w celu wyłuskania potrzebnych informacji. Na końcu wysyła dane do serwera z bazą danych.
Najważniejszym elementem tej częsci jest odpowiednie wysyłanei zapytań HTTP. Użyłem do tego bibliotegki "Requests". 
W celu uzyskania asynchroniczości w danych zapytaniach użyłem biblioteki "Asyncio". Pozwala ona tworzyć pętle rutyny, których użyłem.

# Testy
Testy prowadziłem najpierw na komputerze lokalnym. Sprawdzałem jak zachowa się serwer w różnych przypadkach.
- Kiedy serwer dostanie zły format JSONa , to serwer wyrzuci wyjątek i nie obsłuży zapytania, ale dalej będzie działać.
> ERROR:tornado.application:Uncaught exception POST / (193.239.57.158)
HTTPServerRequest(protocol='http', host='mobisp.duckdns.org:8888', method='POST', uri='/', version='HTTP/1.1', remote_ip='193.239.57.158')
Traceback (most recent call last):
  File "/usr/local/lib/python2.7/dist-packages/tornado/web.py", line 1590, in _execute
    result = method(*self.path_args, **self.path_kwargs)
  File "server.py", line 17, in post
    connector.insertWeatherData(content)
  File "/home/pi/pafciof/Projekt-zespolowy/Python/connector.py", line 31, in insertWeatherData
    content["pressure"]
KeyError: 'pressure'
ERROR:tornado.access:500 POST / (193.239.57.158) 38.01ms

- Kiedy serwer dostanie złe dane w poprawnym JSONie, to również nastąpi wyjątek, ale aplikacja będzie działać dalej.    
