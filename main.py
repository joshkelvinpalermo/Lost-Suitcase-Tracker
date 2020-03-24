import schedule
import requests
import folium
import branca
import numpy
from selenium import webdriver
from geopy import distance
from xml.etree import ElementTree

#CTABusTrackerAPIKey: JNTQivSRb4qxRVbQc5gHCB56M

victorsLocation = (41.980262, -87.668452)
url = "http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22"

def pullRequests():
    global busid, direction, latitude, longitude
    tree = requests.get(url)
    root = ElementTree.fromstring(tree.content)

    for bus in root.findall(".bus/[dd = 'Northbound']"):
        ws = '     '
        busid = bus.find('id').text
        latitude = bus.find('lat').text
        longitude = bus.find('lon').text
        direction = bus.find('dd').text
        coordinates = latitude, longitude
        dist = ("{0:.2f}".format(distance.distance(victorsLocation, coordinates).km))
        length = len(root.findall(".bus/[dd = 'Northbound']"))

        print("Bus ID: " + busid, ws,
              "Direction: " + direction, ws,
              "Distance from Victor: " + dist + "km"
              )

        if dist <= str(1):
            displayer = folium.Map(location=coordinates, zoom_start=20)
            marker = folium.Marker(radius=100, location=coordinates, popup=busid)
            marker.add_to(displayer)
            displayer.save("my_map.html")

            driver = webdriver.Chrome()
            driver.get("file:///C:/Users/imsof/PycharmProjects/bustracker/my_map.html")

#Change n to your preferred seconds/minutes
schedule.every(n).seconds.do(pullRequests)

while True:
    schedule.run_pending()
