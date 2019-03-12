'''
This class defines the field names and their corresponding order for the CSV, ideally this class should also store the data as a true service model
This class is for the FHV CSV
'''

class FHVTripServiceModel:

    BASE_NUM_KEY = "pickup_datetime"
    PICKUP_DATETIME_KEY = "pickup_datetime"
    DROPOFF_DATETIME_KEY = "dropoff_datetime"
    PU_LOCATION_ID_KEY = "PULocationID"
    DO_LOCATION_ID_KEY = "DOLocationID"
    SR_FLAG_KEY = "SR_Flag"

    DATE_TIME_FORMAT = "%Y-%m-%d %H:%M:%S"

    FieldNames = [BASE_NUM_KEY, PICKUP_DATETIME_KEY, DROPOFF_DATETIME_KEY, PU_LOCATION_ID_KEY, DO_LOCATION_ID_KEY, SR_FLAG_KEY]
