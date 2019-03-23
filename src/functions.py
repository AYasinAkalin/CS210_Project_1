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
