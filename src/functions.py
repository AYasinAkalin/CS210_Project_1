import definitions
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import revGeocode


def openDataFile(file_name):
    definitions.init()
    data_frame = pd.read_csv(definitions.DIR_DATA / file_name)
    return data_frame


def saveDataFrame(data_frame,
                  file_name,
                  verbose=False):
    definitions.init()
    data_frame.to_csv(definitions.DIR_DATA / file_name)
    if verbose:
        print("File saved into", str(definitions.DIR_DATA))


def printInfo(info, description='', info_name=''):
    print("============================================")
    if description:
        print(description)
    print(info)


def showInfo(data_frame):
    printInfo(data_frame.shape, "Shape of the data (rows, columns)")
    printInfo(data_frame.head(), "First 5 rows of the data)")
    printInfo(data_frame.describe(), "Statistical analysis")
    printInfo(data_frame.dtypes, "Data type of columns")


def addColumn(data_frame, column_name, default_value=np.nan):
    data_frame[column_name] = default_value


def dealNanValues(data_frame):
    printInfo(data_frame.isnull().sum())


def getCoords(lat_col, lng_col):
    coordinates = []
    for lat, lng in zip(lat_col, lng_col):
        coordinates.append(revGeocode.makeCoordinateTuple(lat, lng))
    return coordinates


def getDistricts(coordinate_list, verbose=False):
    districts = []
    if verbose:
        print("There are", len(coordinate_list), "coordinates to work on.")
        i = 0
    for instance in coordinate_list:
        result = revGeocode.getResult(instance)
        district = revGeocode.getDistrictName(result)[0]
        districts.append(district)
        if verbose:
            i += 1
            if i % 500 == 0:
                print('500 more rows are done.')
                if i == len(districts):
                    print("In total:", len(districts))
    if verbose:
        print(len(districts), "districts are taken with API")
    return districts


def fillDistrict(data_frame, district_col, districts_list, verbose=False):
    data_frame[district_col] = districts_list
    if verbose:
        print(len(districts_list), "districts are filled")
    return data_frame
