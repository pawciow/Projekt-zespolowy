import requests
import json
import asyncio

urlsToGet = 'http://api.openweathermap.org/data/2.5/forecast?id=3081368&units=metric&cnt=1&APPID=13a95d879be0f0f603e025aedba540b8'
# urlToPost = 'http://localhost:8888' # jak jest lokalnie
urlToPost = 'http://mobisp.duckdns.org:8888' # jak jest zdalnie


async def fullTask(urlToDownload, urlToSend):
    while True:
        await sendWeatherInfo(urlToSend, await getWeatherFromCity(urlToDownload))


async def getWeatherFromCity(url):
    r = requests.get(url)
    loc_weather = r.content.strip()
    tmp = json.loads(loc_weather)
    dataToSend =[]
    for item in tmp:
        if item == 'list':
            for data in tmp[item]:
                dataToSend.append(data['main']['temp'])
                dataToSend.append(data['wind']['speed'])
        if item == 'city':
            dataToSend.append(tmp[item]['name'])
            dataToSend.append(tmp[item]['country'])

    jsonToSend = {
        "temperature": dataToSend[0],
        "wind": dataToSend[1],
        "city": dataToSend[2],
        "country": dataToSend[3]
    }
    print(json.dumps(jsonToSend))
    print(dataToSend)

    await asyncio.sleep(5)
    return json.dumps(jsonToSend)


async def sendWeatherInfo(url, data):
    print(data)
    r = requests.post(url, json=data)


loop = asyncio.get_event_loop()
loop.create_task(fullTask(urlsToGet, urlToPost))
loop.run_forever()
loop.close()

