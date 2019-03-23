import functions as fnc
df = fnc.openDataFile("taxi-trips.csv")
fnc.showInfo(df)
pickup_coords = fnc.getCoords(df.pickup_latitude, df.pickup_longitude)
drop_coords = fnc.getCoords(df.dropoff_latitude, df.dropoff_longitude)
