import schedule
import requests
from geopy import distance
from datetime import datetime
from pytz import timezone
from xml.etree import ElementTree

#apikey: JNTQivSRb4qxRVbQc5gHCB56M

victorsLocation = (41.980262, -87.668452)
tz = timezone('EST')
esttime = datetime.now(tz)
url = "http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22"

def pullRequests():
    global busid, direction, latitude, longitude
    tree = requests.get(url)
    root = ElementTree.fromstring(tree.content)

    for bus in root.findall(".bus/[dd = 'Northbound']"):
        busid = bus.find('id').text
        latitude = bus.find('lat').text
        longitude = bus.find('lon').text
        direction = bus.find('dd').text
        ws = '     '

        coordinates = latitude, longitude

        print("Bus ID: " + busid, ws,
              "Direction: " + direction, ws,
              "Distance from Victor: " + ("{0:.2f}".format(distance.distance(victorsLocation, coordinates).km)))


schedule.every(10).seconds.do(pullRequests)

while True:
    schedule.run_pending()
