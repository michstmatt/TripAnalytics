import sqlite3
import os.path
from datetime import datetime
from .TaxiTripRecordModel import TaxiTripRecordModel

'''
This class provides a wrapper for a SQLite DBO
'''

class TaxiTripDBA:

    '''
    File constants
    '''
    DB_DIRECTORY = "./"
    DB_NAME = "tripAnalytics.db"
    DB_PATH = os.path.join(DB_DIRECTORY,DB_NAME)

    '''
    Objects to handle database interaction
    '''
    conn = None
    cursor = None

    '''
    This function initialize the database
    returns True if database already existed, else False 
    '''
    def InitializeDB(self):
        dbExists =  os.path.exists(self.DB_PATH)
        # Note this connection will automatically create the file
        self.conn = sqlite3.connect(self.DB_PATH)
        self.cursor = self.conn.cursor()

        if not dbExists:
            self.CreateTaxiTable()
        
        return dbExists

    '''
    Close up connections, should be performed upon destruction
    '''
    def Close(self):
        self.conn.close()


    '''
    Create the database table for travel records
    TODO move string literals
    '''
    def CreateTaxiTable(self):
        print("[*] Creating DB")
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS TaxiRecords 
                                (
                                    TaxiService text,
                                    VendorID integer,
                                    LpepPickupDateTime text,
                                    LpepDropOffDateTime text,
                                    PULocationID integer,
                                    DOLocationID integer
                                )''')

    '''
    This function bulk inserts TaxiTripRecords
    records: list(TaxiTripRecord)
    '''
    def InsertTaxiRecords(self, records:list):
        print("[*] Adding records to Database")
        #transform data to tuple for inserting
        recordsTuple = [r.ToTuple() for r in records]
        self.cursor.executemany('''insert into TaxiRecords(TaxiService, VendorID, LpepPickupDateTime, LpepDropOffDateTime, PULocationID, DOLocationID)
            values(?, ?, ?, ?, ?, ?)''', recordsTuple)
        self.conn.commit()
        print("[*] %d records added" % len(records))

    '''
    This function retrieves all records in the database
    returns list(TaxiTripRecord)
    '''
    def GetAllTaxiRecords(self):
        self.cursor.execute("SELECT * FROM TaxiRecords")

        records = []
        for row in self.cursor.fetchall():
            model = TaxiTripRecordModel.FromTuple(row)
            records.append(model)
        return records
    
    '''
    This function retrieves count number of records in the database staring at offset
    returns list(TaxiTripRecord)
    '''
    def GetTaxiRecords(self, count: int, offset: int):
        self.cursor.execute("SELECT * FROM TaxiRecords LIMIT %d OFFSET %d" % (count, offset))

        records = []
        for row in self.cursor.fetchall():
            model = TaxiTripRecordModel.FromTuple(row)
            records.append(model)
        return records

    '''
    This function retrieves all records for a given pickup and dropoff locations
    input:
        pickupID: id of pickup location
        dropoffID: id of dropoff location
    '''
    def GetTaxiRecordsForPUDOIDs(self, pickupID: int, dropoffID:int):
        self.cursor.execute("SELECT * FROM TaxiRecords WHERE PULocationID = :puID AND DOLocationID = :doID", {"puID": pickupID, "doID": dropoffID})

        records = []
        for row in self.cursor.fetchall():
            model = TaxiTripRecordModel.FromTuple(row)
            records.append(model)
        return records

    '''
    This function retrieves all records for a given taxi service
    input:
        taxiType: string of taxi service
    '''
    def GetTaxiRecordsForTaxiType(self, taxiType: str):

        # prevent SQL injection
        fmtTaxiType = ""
        if taxiType.lower() == "greentaxi":
            fmtTaxiType = "GreenTaxi"
        elif taxiType.lower() == "yellowtaxi":
            fmtTaxiType = "YellowTaxi"
        elif taxiType.lower() == "fhv":
            fmtTaxiType = "FHV"


        self.cursor.execute("SELECT * FROM TaxiRecords WHERE TaxiService = :taxiType", {"taxiType": fmtTaxiType})

        records = []
        for row in self.cursor.fetchall():
            model = TaxiTripRecordModel.FromTuple(row)
            records.append(model)
        return records

    
    '''
    This function retrieves all records for a given time filter
    input:
        puDateTime: datetime of pickup,
        doDateTime: datetime of dropoff
    '''
    def GetTaxiRecordsForTime(self, puDateTime: datetime, doDateTime: datetime):
        self.cursor.execute("SELECT * FROM TaxiRecords WHERE strftime('%s',LpepPickupDateTime) >= strftime('%s', :puDate) AND strftime('%s',LpepDropOffDateTime) <= strftime('%s', :doDate)", 
            {"puDate": puDateTime.strftime(TaxiTripRecordModel.DATE_TIME_FORMAT),
             "doDate": doDateTime.strftime(TaxiTripRecordModel.DATE_TIME_FORMAT) 
            })

        records = []
        for row in self.cursor.fetchall():
            model = TaxiTripRecordModel.FromTuple(row)
            records.append(model)
        return records
