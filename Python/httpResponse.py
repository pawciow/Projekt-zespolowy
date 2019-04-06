import requests
import json as parser
import asyncio

# urlsToGet = 'https://samples.openweathermap.org/data/2.5/weather?q=London,uk&appid=b6907d289e10d714a6e88b30761fae22'
urlsToGet = 'http://api.openweathermap.org/data/2.5/forecast?id=3081368&units=metric&cnt=1&APPID=13a95d879be0f0f603e025aedba540b8'
urlToPost = 'https://httpbin.org/post'


async def fullTask(urlToDownload, urlToSend):
    while True:
        await sendWeatherInfo(urlToSend, await getWeatherFromCity(urlToDownload))


async def getWeatherFromCity(url):
    r = requests.get(url)
    loc_weather = r.content.strip()
    tmp = parser.loads(loc_weather)
    dataToSend =[]
    for item in tmp:
        # print(item)
        if item == 'list':
            for data in tmp[item]:
                dataToSend.append(data['main']['temp'])
                dataToSend.append(data['wind']['speed'])
        if item == 'city':
            dataToSend.append(tmp[item]['name'])
            dataToSend.append(tmp[item]['country'])
    print(dataToSend)

    await asyncio.sleep(5)
    return dataToSend


async def sendWeatherInfo(url, data):
    print(data)
    r = requests.post(url, json=data)


loop = asyncio.get_event_loop()
loop.create_task(fullTask(urlsToGet, urlToPost))
loop.run_forever()
loop.close()



