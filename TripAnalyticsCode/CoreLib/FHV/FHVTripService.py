from csv import DictReader
from datetime import datetime
from CoreLib.SharedModels.TaxiTripRecordModel import TaxiTripRecordModel
from .FHVTripRecordModel import FHVTripServiceModel as FHVSM

'''
This class provides methods for parsing data from CSV and creating the shared parent data structure, TaxiTripRecordModel
'''
class FHVTripService:

    '''
    This function maps the dictionary of each row of CSV information into a object of TaxiTripRecord Model
    Returns TaxiTripRecordModel
    '''
    def ServiceModelDictToModel(modelDict: dict):
        FHVModel = TaxiTripRecordModel(
            TaxiService = "FHV",
            VendorID = 0,
            LpepPickupDateTime = datetime.strptime(modelDict[FHVSM.PICKUP_DATETIME_KEY], FHVSM.DATE_TIME_FORMAT),
            LpepDropOffDateTime = datetime.strptime(modelDict[FHVSM.DROPOFF_DATETIME_KEY], FHVSM.DATE_TIME_FORMAT),
            PULocationID = (int)(modelDict[FHVSM.PU_LOCATION_ID_KEY]),
            DOLocationID = (int)(modelDict[FHVSM.DO_LOCATION_ID_KEY])
            )

        return FHVModel

    '''
    This function loads and parses the CSV
    Returns List(TaxiTripRecordModel)
    '''
    def GetRecordsFromService(fileName: str):

        records = []
        print("[*] Loading ", fileName)
        # open file, implement FNF handler
        with open(fileName) as file:
            # create a reader to make each row a dictionary with row values corresponding to FieldName keys
            reader = DictReader(file, FHVSM.FieldNames)

            # iterate over rows
            for rowDictionary in reader:
                try:
                    # transform dictioanry into TaxiTripRecord Model
                    model = FHVTripService.ServiceModelDictToModel(rowDictionary)
                    records.append(model)
                except:
                    # format error
                    pass
                print("[*] Records loaded", len(records),end="\r")
        
            print("")
        print("[*] Done")

        return records
