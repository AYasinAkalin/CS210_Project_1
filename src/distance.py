import geopy.distance as dist


def measureDist(*args, method='geodesic'):
    gc = ['great_circle', 'Great Circle', 'Great circle', 'GREAT_CIRCLE']
    gd = ['geodesic', 'Geodesic', 'GEODESIC', 'Geo-desic']

    coord1, coord2 = args[:2]
    if method in gd:
        return float(dist.geodesic(coord1, coord2).kilometers)
    elif method in gc:
        return float(dist.great_circle(coord1, coord2).kilometers)
