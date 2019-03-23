# revGeocode.py
import reverse_geocoder as rg
# https://github.com/thampiman/reverse-geocoder


def makeCoordinateTuple(latitute, longitude):
    if type(latitute) is str or type(latitute) is str:
        latitute = float(latitute)
        longitude = float(longitude)
    return (latitute, longitude)


def getResult(*args):
    return rg.search(args)


def getDistrictName(result):
    names = []
    for query in result:
        names.append(query['name'])
    return names
