import schedule
import requests
import folium
import branca
import numpy
from selenium import webdriver
from geopy import distance
from xml.etree import ElementTree

driver = webdriver.Chrome()
driver.get("file:///C:/Users/imsof/PycharmProjects/bustracker/my_map.html")

#CTABusTrackerAPIKey: JNTQivSRb4qxRVbQc5gHCB56M

victorsLocation = (41.980262, -87.668452)
url = "http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22"

folium_map = folium.Map(location=[41.881832, -87.623177],
                        zoom_start=10)
marker = folium.CircleMarker(location=(41.881432, -87.627177))
marker.add_to(folium_map)

folium_map.save("my_map.html")

def pullRequests():
    global busid, direction, latitude, longitude
    tree = requests.get(url)
    root = ElementTree.fromstring(tree.content)

    for bus in root.findall(".bus/[dd = 'Northbound']"):
        busid = bus.find('id').text
        latitude = bus.find('lat').text
        longitude = bus.find('lon').text
        direction = bus.find('dd').text
        coordinates = latitude, longitude
        dist = ("{0:.2f}".format(distance.distance(victorsLocation, coordinates).km))
        ws = '     '

        print("Bus ID: " + busid, ws,
              "Direction: " + direction, ws,
              "Distance from Victor: " + dist + "km")


schedule.every(5).seconds.do(pullRequests)

while True:
    schedule.run_pending()
