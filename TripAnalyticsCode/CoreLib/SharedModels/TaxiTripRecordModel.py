import json
from datetime import datetime

'''
This is the unified class to contain records from Green, Yellow, and FHV
'''
class TaxiTripRecordModel:
    TaxiService = ""
    VendorID = 0
    LpepPickupDateTime = 0
    LpepDropOffDateTime = 0
    PULocationID = 0
    DOLocationID = 0

    DATE_TIME_FORMAT = "%Y-%m-%d %H:%M:%S"


    '''
    Constructor to initialize all properties
    '''    
    def __init__(self, TaxiService: str, VendorID: int, LpepPickupDateTime: datetime, LpepDropOffDateTime: datetime, PULocationID: int, DOLocationID:int ):
        self.TaxiService = TaxiService
        self.VendorID = VendorID
        self.LpepPickupDateTime = LpepPickupDateTime
        self.LpepDropOffDateTime = LpepDropOffDateTime
        self.PULocationID = PULocationID
        self.DOLocationID = DOLocationID

    '''
    This function formats the object data as a tuple, used for database insert
    returns tuple
    '''
    def ToTuple(self):
        return (self.TaxiService, 
            self.VendorID,  
            self.LpepPickupDateTime.strftime(TaxiTripRecordModel.DATE_TIME_FORMAT), 
            self.LpepDropOffDateTime.strftime(TaxiTripRecordModel.DATE_TIME_FORMAT), 
            self.PULocationID, 
            self.DOLocationID)

    '''
    This function takes tuple tup, and creates an object. This is used for database retreival
    returns TaxiTripRecordModel
    '''
    def FromTuple(tup: tuple):
        (TaxiService, VendorID, LpepPickupDateTime, LpepDropOffDateTime, PULocationID, DOLocationID) = tup
        if type(LpepDropOffDateTime) is str:
            LpepPickupDateTime = datetime.strptime(LpepPickupDateTime, TaxiTripRecordModel.DATE_TIME_FORMAT)
            LpepDropOffDateTime = datetime.strptime(LpepDropOffDateTime, TaxiTripRecordModel.DATE_TIME_FORMAT)

        return TaxiTripRecordModel(TaxiService,VendorID,LpepPickupDateTime,LpepDropOffDateTime,PULocationID,DOLocationID)

    '''
    Serialize the object for JSON REST response
    returns dictionary
    '''
    def ToDict(self):
        dictRep = { 'TaxiService': self.TaxiService,
                    'VendorID': self.VendorID,
                    'LpepPickupDateTime' : self.LpepPickupDateTime.strftime(self.DATE_TIME_FORMAT),
                    'LpepDropOffDateTime' : self.LpepDropOffDateTime.strftime(self.DATE_TIME_FORMAT),
                    'PULocationID' : self.PULocationID,
                    'DOLocationID' : self.DOLocationID
        }   
        return dictRep

