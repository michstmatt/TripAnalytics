import json
from CoreLib.SharedModels.TaxiTripRecordModel import TaxiTripRecordModel

'''
This class provides results to the /predict endpoint
'''
class TimePredictionModel:
    PickupDateTime = 0
    TravelTime = 0
    PULocationID = 0
    DOLocationID = 0

    def __init__(self, model: TaxiTripRecordModel, time: float):
        self.PickupDateTime= str(model.LpepPickupDateTime)
        self.TravelTime = time
        self.PULocationID = model.PULocationID
        self.DOLocationID = model.DOLocationID

    '''
    Serialize the object for JSON REST response
    returns json string
    '''
    def ToJson(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)