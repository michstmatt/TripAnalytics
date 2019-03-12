'''
This class defines the field names and their corresponding order for the CSV, ideally this class should also store the data as a true service model
This class is for the Yellow taxi CSV
'''
class YellowTaxiServiceModel:

    VENDOR_ID_KEY = "VendorID"
    LPEP_PICKUP_DATETIME_KEY = "lpep_pickup_datetime"
    LPEP_DROPOFF_DATETIME_KEY = "lpep_dropoff_datetime"
    WAS_STORED_AND_FORWARDED_KEY = "store_and_fwd_flag"
    RATECODE_ID_KEY = "RatecodeID"
    PU_LOCATION_ID_KEY = "PULocationID"
    DO_LOCATION_ID_KEY = "DOLocationID"
    PASSENGER_COUNT_KEY = "passenger_count"
    TRIP_DISTANCE_KEY = "trip_distance"
    FARE_AMOUNT_KEY = "fare_amount"
    EXTRA_KEY = "extra"
    MTA_TAX_KEY = "mta_tax"
    TIP_AMOUNT_KEY = "tip_amount"
    TOLLS_AMOUNT_KEY = "tolls_amount"
    EHAIL_FEE_KEY = "ehail_fee"
    IMPROVEMENT_SURCHARGE_KEY = "improvement_surcharge"
    TOTAL_AMOUNT_KEY = "total_amount"
    PAYMENT_TYPE_KEY = "payment_type"
    TRIP_TYPE_KEY = "trip_type"

    DATE_TIME_FORMAT = "%Y-%m-%d %H:%M:%S"

    FieldNames = [VENDOR_ID_KEY, LPEP_PICKUP_DATETIME_KEY, LPEP_DROPOFF_DATETIME_KEY, PASSENGER_COUNT_KEY, TRIP_DISTANCE_KEY,RATECODE_ID_KEY,WAS_STORED_AND_FORWARDED_KEY,PU_LOCATION_ID_KEY,DO_LOCATION_ID_KEY,PAYMENT_TYPE_KEY,FARE_AMOUNT_KEY,EXTRA_KEY,MTA_TAX_KEY,TIP_AMOUNT_KEY,TOLLS_AMOUNT_KEY,IMPROVEMENT_SURCHARGE_KEY,TOTAL_AMOUNT_KEY]
