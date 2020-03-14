import schedule
import time
from xml.etree import ElementTree
import requests

#apikey: JNTQivSRb4qxRVbQc5gHCB56M
#victorslocation: Latitude: 41.980262, Longitude: -87.668452

url = "http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22"

def pullRequests():
    global busid, direction, latitude, longitude
    tree = requests.get(url)
    root = ElementTree.fromstring(tree.content)

    for bus in root.findall('bus'):
        busid = bus.find("id").text
        direction = bus.find("dd").text
        latitude = bus.find("lat").text

        print("Bus ID: " + busid, "Direction: " + direction, "Latitude: " + latitude)


schedule.every(10).seconds.do(pullRequests)

while True:
    schedule.run_pending()
