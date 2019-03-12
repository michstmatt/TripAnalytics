from flask import Flask, request
from datetime import datetime
import json


from CoreLib.GreenTaxi.GreenTaxiTripService import GreenTaxiTripService
from CoreLib.YellowTaxi.YellowTaxiTripService import YellowTaxiTripService
from CoreLib.FHV.FHVTripService import FHVTripService
from CoreLib.SharedModels.TaxiTripRecordModel import TaxiTripRecordModel
from CoreLib.SharedModels.TaxiTripDBA import TaxiTripDBA
from ML.TimePredictorModel import TimePredictorModel
from ML.TimePredictionModel import TimePredictionModel

#time format expected in URL
URL_TIME_FORMAT = "%H:%M"
URL_DATE_TIME_FORMAT = "%Y-%m-%d %H:%M:%S"

def getDB():
    #init datase connection
    dba = TaxiTripDBA()
    dbExists = dba.InitializeDB()


    # if the database didnt exist, then import data from csvs
    if not dbExists:

        greenTaxiData = GreenTaxiTripService.GetRecordsFromService(
            '../tripData/green_tripdata_2018-01.csv')
        dba.InsertTaxiRecords(greenTaxiData)
        del greenTaxiData

        yellowTaxiData = YellowTaxiTripService.GetRecordsFromService(
            '../tripData/yellow_tripdata_2018-01.csv')
        dba.InsertTaxiRecords(yellowTaxiData)
        del yellowTaxiData

        fhvTaxiData = FHVTripService.GetRecordsFromService(
            '../tripData/fhv_tripdata_2018-01.csv')
        dba.InsertTaxiRecords(fhvTaxiData)
        del fhvTaxiData
    return dba

dba = getDB()
# grab the top 100,000 records to train our model
trainRecords = dba.GetTaxiRecords(100000, 0)
dba.Close()

# create the time prediciton model
model = TimePredictorModel()

# format records for training
xTrain, yTrain = model.FormatRecordsForTraining(trainRecords)

# train the model
model.Train(xTrain, yTrain)



# API region
# create the API
app = Flask(__name__)

'''
This handles request to http://my-uri/predict
expects http://my-uri/predict?pickupID=<INT>&dropoffID=<INT>&timeString=HH:MM
'''
@app.route("/predict")
def predictEndpoint():
    # TODO better error handling
    try:
        # parse  URL args
        pickupID = request.args.get('pickupID', type=int)
        dropoffID = request.args.get('dropoffID', type=int)
        timeString = request.args.get('timeString', type=str)
        dateParse = datetime.strptime(timeString, URL_TIME_FORMAT)

        # create a dummy model object
        rideModel = TaxiTripRecordModel(TaxiService="",
                                        VendorID=0,
                                        LpepPickupDateTime = dateParse,
                                        LpepDropOffDateTime = None,
                                        PULocationID = pickupID,
                                        DOLocationID = dropoffID)

        # format object for training, NB must be an array to make SKLearn happy
        dataForPred = model.FormatRecordsForPrediction([rideModel])

        # predict the travel time
        time = model.Predict(dataForPred).tolist()[0]

        # format data for json response
        predictionModel = TimePredictionModel(rideModel,time)

        # return the response as json
        return predictionModel.ToJson()

    except:
        return "Error in formatting"


'''
This handles request to http://my-uri/getRecords
expects http://my-uri/getRecods?count=<INT>&offset=<INT>
'''
@app.route("/getRecords")
def recordsEndpoint():
    # TODO better error handling
    try:
        # parse  URL args
        count = request.args.get('count', type=int)
        offset = request.args.get('offset', type=int)

        dba = getDB()
        records = dba.GetTaxiRecords(count,offset)
        dba.Close()
        recordsDict = [r.ToDict() for r in records]

        # return the response as json
        return json.dumps(recordsDict)

    except:
        return "Error in formatting"

'''
This handles request to http://my-uri/getRecordsForTime
expects http://my-uri/getRecordsForTime?pickupTimeString=YYYY-mm-dd HH:MM:SS&dropoffTimeString=YYYY-mm-dd HH:MM:SS
'''
@app.route("/getRecordsForTime")
def recordsForTimeEndpoint():
    # TODO better error handling
    try:
        # parse  URL args
        pickupTimeString = request.args.get('pickupTimeString', type=str)
        pickupTimeString = pickupTimeString.replace('%20', ' ')
        puDateParse = datetime.strptime(pickupTimeString, URL_DATE_TIME_FORMAT)

        dropoffTimeString = request.args.get('dropoffTimeString', type=str)
        dropoffTimeString = dropoffTimeString.replace('%20', ' ')
        doDateParse = datetime.strptime(dropoffTimeString, URL_DATE_TIME_FORMAT)

        dba = getDB()
        records = dba.GetTaxiRecordsForTime(puDateParse,doDateParse)
        dba.Close()
        recordsDict = [r.ToDict() for r in records]

        # return the response as json
        return json.dumps(recordsDict)

        

    except:
        return "Error in formatting"

'''
This handles request to http://my-uri/getRecordsForTaxiType
expects http://my-uri/getRecordsForTaxiType?taxiType=<STRING>
'''
@app.route("/getRecordsForTaxiType")
def recordsForTaxiTypeEndpoint():
    # TODO better error handling
    try:
        # parse  URL args
        taxiType = request.args.get('type', type=str)
        dba = getDB()
        records = dba.GetTaxiRecordsForTaxiType(taxiType)
        dba.Close()
        recordsDict = [r.ToDict() for r in records]

        # return the response as json
        return json.dumps(recordsDict)

    except:
        return "Error in formatting"



app.run(port='5002')

