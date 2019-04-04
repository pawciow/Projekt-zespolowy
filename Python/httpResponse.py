import requests
import json as parser
import asyncio

urlsToGet = 'https://samples.openweathermap.org/data/2.5/weather?q=London,uk&appid=b6907d289e10d714a6e88b30761fae22'
urlToPost = 'https://httpbin.org/post'


async def fullTask(urlToDownload, urlToSend):
    while True:
        await sendWeatherInfo(urlToSend, await getWeatherFromCity(urlToDownload))


async def getWeatherFromCity(url):
    r = requests.get(url)
    loc_weather = r.content.strip()
    tmp = parser.loads(loc_weather)
    dataToSend =[]
    [print(tmp[item]) for item in tmp]
    [dataToSend.append(tmp[item]) for item in tmp if item == 'name']
    [dataToSend.append(tmp[item]['temp']) for item in tmp if item == 'main']
    [dataToSend.append(tmp[item]['speed']) for item in tmp if item == 'wind']
    [dataToSend.append(tmp[item]['lon']) for item in tmp if item == 'coord']
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



