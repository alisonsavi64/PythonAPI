from app import app
from flask import request
import json
from app import databaseFunctions

def convertDataFromRequetToJson(data):

    return json.loads(data.decode('utf-8'))

@app.route("/api/series", methods=['GET'])
def getAllSeries():

    returnedDataOfAllSeries = databaseFunctions.getAllSeriesFunction()
    return(returnedDataOfAllSeries)

@app.route("/api/series/<userUniqueId>/<serieUniqueId>", methods=['GET'])
def getSpecificSerieByIds(userUniqueId, serieUniqueId):

    returnedSpecificSerieGotByIdData = databaseFunctions.getSpecificSerieByIdsFunction(userUniqueId, serieUniqueId)
    return (returnedSpecificSerieGotByIdData)

@app.route("/api/series/user/<userUniqueId>", methods=['GET'])
def getAllSeriesAddedByUser(userUniqueId):

    returnedAllUserAddedSeriesData = databaseFunctions.getAllSeriesAddedByUserFunction(userUniqueId)
    return (returnedAllUserAddedSeriesData)
    

@app.route("/api/series", methods=['POST'])
def addSerieToUserProfile():
     
    returnedUserAddedSerieData = databaseFunctions.addSerieToUserProfileFunction(convertDataFromRequetToJson(request.data))
    return(returnedUserAddedSerieData)


@app.route("/api/series/<watchedUserSerieUniqueId>", methods=['DELETE'])
def deleteSerieOfUserProfile(watchedUserSerieUniqueId):

    databaseFunctions.deleteSerieOfUserProfileFunction(watchedUserSerieUniqueId)
    return({"deletedSerieOfUserProfileId": watchedUserSerieUniqueId})


@app.route("/api/series/<watchedUserSerieUniqueId>", methods=['PUT'])
def updateSerieDataOfUser(watchedUserSerieUniqueId):
    
    returnedUserUpdatedSerieData = databaseFunctions.updateSerieOfUserProfileFunction(watchedUserSerieUniqueId, convertDataFromRequetToJson(request.data))
    return (returnedUserUpdatedSerieData)

@app.route("/api/user/signup", methods=['POST'])
def signupUser():

    returnedUserSignupData = databaseFunctions.signupUserFunction(convertDataFromRequetToJson(request.data))
    return (returnedUserSignupData)


@app.route("/api/user/login", methods=['POST'])
def loginUser():
   
    returnedUserLoginData = databaseFunctions.loginUserFunction(convertDataFromRequetToJson(request.data))
    return (returnedUserLoginData)


