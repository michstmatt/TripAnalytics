from csv import DictReader
from datetime import datetime
from CoreLib.SharedModels.TaxiTripRecordModel import TaxiTripRecordModel
from .YellowTaxiTripRecordModel import YellowTaxiServiceModel as YTSM

'''
This class provides methods for parsing data from CSV and creating the shared parent data structure, TaxiTripRecordModel
'''
class YellowTaxiTripService:


    '''
    This function maps the dictionary of each row of CSV information into a object of TaxiTripRecord Model
    Returns TaxiTripRecordModel
    '''
    def ServiceModelDictToModel(modelDict: dict):
        yellowTaxiModel = TaxiTripRecordModel(
            TaxiService="YellowTaxi",
            VendorID = (int)(modelDict[YTSM.VENDOR_ID_KEY]),
            LpepPickupDateTime = datetime.strptime( modelDict[YTSM.LPEP_PICKUP_DATETIME_KEY], YTSM.DATE_TIME_FORMAT),
            LpepDropOffDateTime = datetime.strptime( modelDict[YTSM.LPEP_DROPOFF_DATETIME_KEY], YTSM.DATE_TIME_FORMAT),
            PULocationID = (int)(modelDict[YTSM.PU_LOCATION_ID_KEY]),
            DOLocationID = (int)(modelDict[YTSM.DO_LOCATION_ID_KEY]))
        return yellowTaxiModel

    '''
    This function loads and parses the CSV
    Returns List(TaxiTripRecordModel)
    '''
    def GetRecordsFromService(fileName:str):

        records = []
        print("[*] Loading ", fileName)
        # open file, implement FNF handler
        with open(fileName) as file:
            # create a reader to make each row a dictionary with row values corresponding to FieldName keys
            reader = DictReader(file, YTSM.FieldNames)

            # iterate over rows
            for rowDictionary in reader:
                try:
                    # transform dictioanry into TaxiTripRecord Model
                    model = YellowTaxiTripService.ServiceModelDictToModel(rowDictionary)
                    records.append(model)
                except:
                    # Error with data format 
                    pass
                print("[*] Records loaded", len(records),end="\r")
        
            print("")
        print("[*] Done")

        return records


