from sklearn.neighbors import KNeighborsRegressor
from datetime import datetime, timedelta
from CoreLib.SharedModels.TaxiTripRecordModel import TaxiTripRecordModel

'''
This Class provides methods for formatting, training, and predicting travel time
'''
class TimePredictorModel:

	'''
	A linear/logistic approach wont work well in this instance due to model fitting and time
	Looking at similar records will provide the best model 
	'''
	model = KNeighborsRegressor(n_neighbors=6)


	'''
	Format a record for training, this data has know travel time
	'''
	def FormatRecordForTraining(self, record: TaxiTripRecordModel):
		travelTime = timedelta(hours=record.LpepDropOffDateTime.hour, minutes=record.LpepDropOffDateTime.minute) - \
                    timedelta(hours=record.LpepPickupDateTime.hour,
                              minutes=record.LpepPickupDateTime.minute)
		x = self.FormatRecordForPrediction(record)
		y = travelTime.seconds

		return (x,y)
	
	'''
	Bulk format records for training, this is necessary for the X and Y arrays for SciKit Learn input
	returns a tuple of (list,float)
	'''
	def FormatRecordsForTraining(self, records: list):
		X = []
		Y = []

		for r in records:
			x,y = self.FormatRecordForTraining(r)
			X.append(x)
			Y.append(y)

		return (X, Y)
	
	'''
	Format data for prediciting, this is data coming from the API. We do not know the travel time
	returns a feature vector (list)
	'''
	def FormatRecordForPrediction(self, record: TaxiTripRecordModel):

		puID = self.OneHotEncode(record.PULocationID, 265)
		doID = self.OneHotEncode(record.DOLocationID, 265)
		x = puID + doID + [record.LpepPickupDateTime.hour]
		return x

	'''
	Bulk format records for predicition, this is necessary for the X and Y arrays for SciKit Learn input, even for a single record
	returns X an array of feature vectors list(list)
	'''
	def FormatRecordsForPrediction(self, records: list):
		X = []

		for r in records:
			x = self.FormatRecordForPrediction(r)
			X.append(x)

		return X

	'''
	We must encode certain values, such as pickup ID, as pickup IDs have no mathematical correlation
		(e.g.,) OneHotEncode(2,4) = [0,0,1,0,0]
		returns a sparse vector
	'''
	def OneHotEncode(self, id, total):
		array = [0 for i in range(total+1)]
		array[(int)(id)] = 1
		return array

	'''
	This function trains the model with given X feature and Y label data
	'''
	def Train(self, X, Y):
		print("[*] Training Model")
		self.model.fit(X, Y)
		print("[*] Done")

	'''
	This function predicts label data for a given X array
	returns an array of predictions
	'''
	def Predict(self, X):
		return self.model.predict(X)
