from csv import DictReader
from datetime import datetime
from CoreLib.SharedModels.TaxiTripRecordModel import TaxiTripRecordModel
from .GreenTaxiTripRecordModel import GreenTaxiServiceModel as GTSM


'''
This class provides methods for parsing data from CSV and creating the shared parent data structure, TaxiTripRecordModel
'''
class GreenTaxiTripService:

    '''
    This function maps the dictionary of each row of CSV information into a object of TaxiTripRecord Model
    Returns TaxiTripRecordModel
    '''
    def ServiceModelDictToModel(modelDict):
        greenTaxiModel = TaxiTripRecordModel(
            TaxiService="GreenTaxi",
            VendorID = (int)(modelDict[GTSM.VENDOR_ID_KEY]),
            LpepPickupDateTime = datetime.strptime( modelDict[GTSM.LPEP_PICKUP_DATETIME_KEY], GTSM.DATE_TIME_FORMAT),
            LpepDropOffDateTime = datetime.strptime( modelDict[GTSM.LPEP_DROPOFF_DATETIME_KEY], GTSM.DATE_TIME_FORMAT),
            PULocationID = (int)(modelDict[GTSM.PU_LOCATION_ID_KEY]),
            DOLocationID = (int)(modelDict[GTSM.DO_LOCATION_ID_KEY]))
        return greenTaxiModel

    '''
    This function loads and parses the CSV
    Returns List(TaxiTripRecordModel)
    '''
    def GetRecordsFromService(fileName):
        records = []
        print("[*] Loading ", fileName)
        # open file, implement FNF handler
        with open(fileName) as file:
            # create a reader to make each row a dictionary with row values corresponding to FieldName keys
            reader = DictReader(file,GTSM.FieldNames)

            # iterate over rows
            for rowDictionary in reader:
                try:
                    # transform dictioanry into TaxiTripRecord Model
                    model = GreenTaxiTripService.ServiceModelDictToModel(rowDictionary)
                    records.append(model)
                except:
                    # invalid data format
                    pass
                print("[*] Records loaded", len(records),end="\r")
        
            print("")
        print("[*] Done")


        return records


