import functions as fnc
df = fnc.openDataFile("taxi-trips.csv")
fnc.showInfo(df)

pickup_coords = fnc.getCoords(df.pickup_latitude, df.pickup_longitude)
drop_coords = fnc.getCoords(df.dropoff_latitude, df.dropoff_longitude)

dl = fnc.getDistricts(pickup_coords)
fnc.fillDistrict(df, "pickup_district", dl)

dl = fnc.getDistricts(drop_coords)
fnc.fillDistrict(df, "dropoff_district", dl)

# ''' Save Updated data frame
fnc.saveDataFrame(df, 'taxi-trips_2'.csv)
# '''

for d in ['pickup_district', 'dropoff_district']:
    fnc.printPopularDistrict(df, d)

dl = fnc.getDistances(pickup_coords, drop_coords)
df['distance'] = dl

df['time_of_day'] = fnc.getDayTime(df.pickup_datetime)
