# Lost Suitcase Tracker

Jerry went to Chicago then rode a bus at route 22 to see his long time friend Victor. At the stop over, he went off the bus to buy some ice cream without noticing that the bus had already left. After a while he realized that he’d left the suitcase on the bus! Jerry needs to get it back but he needs your support. Your task is to help Jerry get it back.

1.) Jerry has no idea what’s the number of the bus he was riding at that time. Find all possible candidates by parsing the data from this API:

http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route={route number}

We need all buses going north bound. Victor’s location is at 41.980262 latitude and -87.668452 longitude.

2.) Create a program/script which monitors the identified buses and reports their current distance from Victor’s office. When the bus gets closer than 1 kilometer, the program must issue an alert by popping up a web-page showing the bus location on a map so that Jerry could meet them and get the suitcase back.

Supposedly you should only have 3 hours to solve his issue but since I’m good you will have 8 hours to solve this.


Readings:
https://developers.google.com/maps/documentation/static-maps/intro#location

Rules & Restrictions:
None, you can browse the internet all the way!
