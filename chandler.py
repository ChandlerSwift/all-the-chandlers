#!/usr/bin/env python3

# NOTE: all math is done in kilometers
# TODO:
#  * Timing code
#  * Static start/end points

import itertools
from math import sin, cos, sqrt, atan2, radians # lat/long distance finding

chandlers = {"Chandler, Arizona": [33.3, -111.833333],
             "Chandler Air Force Station": [43.897778, -95.945833],
             "Chandler State Wayside": [42.407102, -120.289682],
             "Chandler Bay": [44.56, -67.54],
             "Chandler Gulch": [37.283277, -122.377751],
             "Chandlers Valley, Pennsylvania": [41.934167, -79.303611],
             "Chandler, Texas": [32.307222, -95.479444],
             "Chandler, Oklahoma": [35.709167, -96.889722],
             "Chandler Township, Adams County, North Dakota": [46.140278, -102.425556],
             "Chandler, Missouri": [39.300278, -94.382778],
             "Chandler, Minnesota": [43.929167, -95.947222],
#             "Chandler Township, Huron County, Michigan": [43.888333, -83.172222],
#             "Chandler Township, Charlevoix County, Michigan": [45.237222, -84.7825],
#             "Chandler, Pike County, Indiana": [38.421667, -87.352222],
#             "Chandler, Indiana": [38.041944, -87.368889],
#             "Chandler, California": [34.809722, -118.884444],
}

def distance_between(coord1, coord2):

    # approximate radius of earth in km
    R = 6373.0

    lat1 = chandlers[coord1][0]
    lon1 = chandlers[coord1][1]
    lat2 = chandlers[coord2][0]
    lon2 = chandlers[coord2][1]

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c

    return distance

min_dist=9999999999 # kilometers, starting with a wayyyy huge number
best_route = None

for order in itertools.permutations(chandlers):
    sum = 0
    for i in range(len(order) - 1):
        sum += distance_between(order[i], order[i+1])
    if sum < min_dist:
        min_dist = sum
        best_route = order

print(best_route)
