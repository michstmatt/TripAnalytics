# TripAnalytics

This project is a python API to recieve information regarding NYC traffic data. This app is based on Flask's python module to provide the API service


## Dependencies

Python Flask

```
pip3 install flask
```

SciKit Learn
```
pip3 install sklearn
```

## Instructions to run

```
python3 ./TripAnalyticsCode/run.py
```


## API Endpoints


### Predict travel time given a pickup, dropoff IDs and time of departure
```
/predict?pickupID=<INT>&dropoffID=<INT>&timeString=HH:MM
/predict?pickupID=1&dropoffID=75&timeString=12:00
{ "DOLocationID": 75, "PULocationID": 1, "PickupDateTime": "1900-01-01 12:00:00", "TravelTime": 410.0 }

```

### Get Records filter by Count and offset
```
getRecods?count=<INT>&offset=<INT>
/getRecords?count=10&offset=0

[{"TaxiService": "GreenTaxi", "VendorID": 2, "LpepPickupDateTime": "2018-01-01 00:18:50", "LpepDropOffDateTime": "2018-01-01 00:24:39", "PULocationID": 236, "DOLocationID": 236}, {"TaxiService": "GreenTaxi", "VendorID": 2, "LpepPickupDateTime": "2018-01-01 00:30:26", "LpepDropOffDateTime": "2018-01-01 00:46:42", "PULocationID": 43, "DOLocationID": 42}, {"TaxiService": "GreenTaxi", "VendorID": 2, "LpepPickupDateTime": "2018-01-01 00:07:25", "LpepDropOffDateTime": "2018-01-01 00:19:45", "PULocationID": 74, "DOLocationID": 152}, {"TaxiService": "GreenTaxi", "VendorID": 2, "LpepPickupDateTime": "2018-01-01 00:32:40", "LpepDropOffDateTime": "2018-01-01 00:33:41", "PULocationID": 255, "DOLocationID": 255}, {"TaxiService": "GreenTaxi", "VendorID": 2, "LpepPickupDateTime": "2018-01-01 00:32:40", "LpepDropOffDateTime": "2018-01-01 00:33:41", "PULocationID": 255, "DOLocationID": 255}, {"TaxiService": "GreenTaxi", "VendorID": 2, "LpepPickupDateTime": "2018-01-01 00:38:35", "LpepDropOffDateTime": "2018-01-01 01:08:50", "PULocationID": 255, "DOLocationID": 161}, {"TaxiService": "GreenTaxi", "VendorID": 2, "LpepPickupDateTime": "2018-01-01 00:18:41", "LpepDropOffDateTime": "2018-01-01 00:28:22", "PULocationID": 189, "DOLocationID": 65}, {"TaxiService": "GreenTaxi", "VendorID": 2, "LpepPickupDateTime": "2018-01-01 00:38:02", "LpepDropOffDateTime": "2018-01-01 00:55:02", "PULocationID": 189, "DOLocationID": 225}, {"TaxiService": "GreenTaxi", "VendorID": 2, "LpepPickupDateTime": "2018-01-01 00:05:02", "LpepDropOffDateTime": "2018-01-01 00:18:35", "PULocationID": 129, "DOLocationID": 82}, {"TaxiService": "GreenTaxi", "VendorID": 2, "LpepPickupDateTime": "2018-01-01 00:35:23", "LpepDropOffDateTime": "2018-01-01 00:42:07", "PULocationID": 226, "DOLocationID": 7}]
```

### Get records filter by time
```
getRecordsForTime?pickupTimeString=YYYY-mm-dd HH:MM:SS&dropoffTimeString=YYYY-mm-dd HH:MM:SS
/getRecordsForTime?pickupTimeString=2018-01-02 00:00:00&dropoffTimeString=2018-01-02 00:00:00

[{"TaxiService": "GreenTaxi", "VendorID": 2, "LpepPickupDateTime": "2018-01-02 00:00:00", "LpepDropOffDateTime": "2018-01-02 00:00:00", "PULocationID": 188, "DOLocationID": 97}, {"TaxiService": "GreenTaxi", "VendorID": 2, "LpepPickupDateTime": "2018-01-02 00:00:00", "LpepDropOffDateTime": "2018-01-02 00:00:00", "PULocationID": 133, "DOLocationID": 181}, {"TaxiService": "GreenTaxi", "VendorID": 2, "LpepPickupDateTime": "2018-01-02 00:00:00", "LpepDropOffDateTime": "2018-01-02 00:00:00", "PULocationID": 134, "DOLocationID": 19}, {"TaxiService": "GreenTaxi", "VendorID": 2, "LpepPickupDateTime": "2018-01-02 00:00:00", "LpepDropOffDateTime": "2018-01-02 00:00:00", "PULocationID": 42, "DOLocationID": 42}, {"TaxiService": "YellowTaxi", "VendorID": 2, "LpepPickupDateTime": "2018-01-02 00:00:00", "LpepDropOffDateTime": "2018-01-02 00:00:00", "PULocationID": 10, "DOLocationID": 141}, {"TaxiService": "YellowTaxi", "VendorID": 2, "LpepPickupDateTime": "2018-01-02 00:00:00", "LpepDropOffDateTime": "2018-01-02 00:00:00", "PULocationID": 165, "DOLocationID": 161}, {"TaxiService": "YellowTaxi", "VendorID": 2, "LpepPickupDateTime": "2018-01-02 00:00:00", "LpepDropOffDateTime": "2018-01-02 00:00:00", "PULocationID": 43, "DOLocationID": 100}]
```

### Get records filter by taxi service
```
/getRecordsForTaxiType?type=<STRING>
/getRecordsForTaxiType?type=GreenTaxi

[{"TaxiService": "GreenTaxi", "VendorID": 2, "LpepPickupDateTime": "2018-01-01 00:18:50", "LpepDropOffDateTime": "2018-01-01 00:24:39", "PULocationID": 236, "DOLocationID": 236}, {"TaxiService": "GreenTaxi", "VendorID": 2, "LpepPickupDateTime": "2018-01-01 00:30:26", "LpepDropOffDateTime": "2018-01-01 00:46:42", "PULocationID": 43, "DOLocationID": 42}, {"TaxiService": "GreenTaxi", "VendorID": 2, "LpepPickupDateTime": "2018-01-01 00:07:25", "LpepDropOffDateTime": "2018-01-01 00:19:45", "PULocationID": 74, "DOLocationID": 152}, {"TaxiService": "GreenTaxi", "VendorID": 2, "LpepPickupDateTime": "2018-01-01 00:32:40", "LpepDropOffDateTime": "2018-01-01 00:33:41", "PULocationID": 255, "DOLocationID": 255}, {"TaxiService": "GreenTaxi", "VendorID": 2, "LpepPickupDateTime": "2018-01-01 00:32:40", "LpepDropOffDateTime": "2018-01-01 00:33:41", "PULocationID": 255, "DOLocationID": 255}, {"TaxiService": "GreenTaxi", "VendorID": 2, "LpepPickupDateTime": "2018-01-01 00:38:35", "LpepDropOffDateTime": "2018-01-01 01:08:50", "PULocationID": 255, "DOLocationID": 161}, {"TaxiService": "GreenTaxi", "VendorID": 2, "LpepPickupDateTime": "2018-01-01 00:18:41", "LpepDropOffDateTime": "2018-01-01 00:28:22", "PULocationID": 189, "DOLocationID": 65}, {"TaxiService": "GreenTaxi", "VendorID": 2, "LpepPickupDateTime": "2018-01-01 00:38:02", "LpepDropOffDateTime": "2018-01-01 00:55:02", "PULocationID": 189, "DOLocationID": 225}, {"TaxiService": "GreenTaxi", "VendorID": 2, "LpepPickupDateTime": "2018-01-01 00:05:02", "LpepDropOffDateTime": "2018-01-01 00:18:35", "PULocationID": 129, "DOLocationID": 82}, {"TaxiService": "GreenTaxi", "VendorID": 2, "LpepPickupDateTime": "2018-01-01 00:35:23", "LpepDropOffDateTime": "2018-01-01 00:42:07", "PULocationID": 226, "DOLocationID": 7}, {"TaxiService": "GreenTaxi", "VendorID": 2, "LpepPickupDateTime": "2018-01-01 00:21:00", "LpepDropOffDateTime": "2018-01-01 00:39:04", "PULocationID": 145, "DOLocationID": 129}, {"TaxiService": "GreenTaxi", "VendorID": 2, "LpepPickupDateTime": "2018-01-01 00:56:29", "LpepDropOffDateTime": "2018-01-01 01:04:44", "PULocationID": 7, "DOLocationID": 223}, {"TaxiService": "GreenTaxi", "VendorID": 2, "LpepPickupDateTime": "2018-01-01 00:11:48", "LpepDropOffDateTime": "2018-01-01 00:30:13", "PULocationID": 255, "DOLocationID": 189}, {"TaxiService": "GreenTaxi", "VendorID": 2, "LpepPickupDateTime": "2018-01-01 00:57:59", "LpepDropOffDateTime": "2018-01-01 01:12:26", "PULocationID": 97, "DOLocationID": 188}, {"TaxiService": "GreenTaxi", "VendorID": 2, "LpepPickupDateTime": "2018-01-01 00:36:58", "LpepDropOffDateTime": "2018-01-01 00:51:08", "PULocationID": 244, "DOLocationID": 75}, {"TaxiService": "GreenTaxi", "VendorID": 1, "LpepPickupDateTime": "2018-01-01 00:07:40", "LpepDropOffDateTime": "2018-01-01 00:15:20", "PULocationID": 225, "DOLocationID": 37}, {"TaxiService": "GreenTaxi", "VendorID": 1, "LpepPickupDateTime": "2018-01-01 00:25:09", "LpepDropOffDateTime": "2018-01-01 00:42:04", "PULocationID": 36, "DOLocationID": 145}, {"TaxiService": "GreenTaxi", "VendorID": 1, "LpepPickupDateTime": "2018-01-01 00:42:52", "LpepDropOffDateTime": "2018-01-01 01:00:53", "PULocationID": 145, "DOLocationID": 173}, {"TaxiService": "GreenTaxi", "VendorID": 2, "LpepPickupDateTime": "2018-01-01 00:06:22", "LpepDropOffDateTime": "2018-01-01 00:08:17", "PULocationID": 49, "DOLocationID": 49}, {"TaxiService": "GreenTaxi", "VendorID": 2, "LpepPickupDateTime": "2018-01-01 00:34:53", "LpepDropOffDateTime": "2018-01-01 00:52:55", "PULocationID": 40, "DOLocationID": 113}, {"TaxiService": "GreenTaxi", "VendorID": 1, "LpepPickupDateTime": "2018-01-01 00:25:08", "LpepDropOffDateTime": "2018-01-01 00:28:27", "PULocationID": 179, "DOLocationID": 7}, {"TaxiService": "GreenTaxi", "VendorID": 2, "LpepPickupDateTime": "2018-01-01 00:36:26", "LpepDropOffDateTime": "2018-01-01 00:51:07", "PULocationID": 7, "DOLocationID": 193}, {"TaxiService": "GreenTaxi", "VendorID": 2, "LpepPickupDateTime": "2018-01-01 00:53:05", "LpepDropOffDateTime": "2018-01-01 01:26:51", "PULocationID": 97, "DOLocationID": 74}, {"TaxiService": "GreenTaxi", "VendorID": 1, "LpepPickupDateTime": "2018-01-01 00:11:41", "LpepDropOffDateTime": "2018-01-01 00:22:10", "PULocationID": 255, "DOLocationID": 112}, {"TaxiService": "GreenTaxi", "VendorID": 1, "LpepPickupDateTime": "2018-01-01 00:40:32", "LpepDropOffDateTime": "2018-01-01 01:01:20", "PULocationID": 255, "DOLocationID": 28}, ... ]
```
