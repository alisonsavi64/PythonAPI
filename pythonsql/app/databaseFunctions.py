import mysql.connector
import base64
from mysql.connector import Error

def decodeBinaryBlobImage(file):
    binaryData = base64.b64encode(file)
    newdata = binaryData.decode()
    return newdata

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='portfolio',
                                         user='alison',
                                         password='1234')

    if connection.is_connected():
        cursor = connection.cursor()

        def signupUserFunction(recevedUserAuthData):
            
            userAuthData = recevedUserAuthData['signupUserData']
            userAuthDataToBeReturned = {}
            cursor.execute(
                f"""SELECT * FROM users WHERE userEmail='{userAuthData['userEmail']}'""""")
            userRowsAuth = cursor.fetchall()
            if userRowsAuth == []:
                cursor.execute(f"""INSERT INTO users VALUES(
				Null, 
				'{userAuthData['userName']}', 
				'{userAuthData['userEmail']}', 
				'{userAuthData['userPassword']}')""")
                connection.commit()
                cursor.execute(
                    f"""SELECT userId, userName  FROM users WHERE userEmail='{userAuthData['userEmail']}' AND userPassword='{userAuthData['userPassword']}'""")
                userRowsAuth = cursor.fetchall()
                for itemUserAuth in userRowsAuth:
                    userAuthDataToBeReturned["userData"] = {"userId": itemUserAuth[0], "userName": itemUserAuth[1]}
                return(userAuthDataToBeReturned)
            else:
                return {}

        def loginUserFunction(recevedUserAuthData):
            print(recevedUserAuthData)
            userAuthData = recevedUserAuthData['loginUserData']
            print(userAuthData)
            userAuthDataToBeReturned = {}
            cursor.execute(
                f"""SELECT userId, userName  FROM users WHERE userEmail='{userAuthData['userEmail']}' AND userPassword='{userAuthData['userPassword']}'""")
            userRowsAuth = cursor.fetchall()
            if len(userRowsAuth) == 0:
                return({})
            else:
                for itemUserAuth in userRowsAuth:
                    userAuthDataToBeReturned["userData"] = {"userId": itemUserAuth[0], "userName": itemUserAuth[1]}
                return(userAuthDataToBeReturned)

        def addSerieToUserProfileFunction(recevedSerieDataToBeAdd):

            serieDataToBeAddToProfileUser = recevedSerieDataToBeAdd['userAddSerieData']
            cursor.execute(
                f"""SELECT * from series WHERE serieId={serieDataToBeAddToProfileUser['serieId']}""")
            serieRowsData = cursor.fetchall()
            for itemSerieData in serieRowsData:
                if int(itemSerieData[2]) < int(serieDataToBeAddToProfileUser['watchedSerieSeasons']) or int(itemSerieData[3]) < int(serieDataToBeAddToProfileUser['watchedSerieEpisodes']) or int(serieDataToBeAddToProfileUser['watchedSerieSeasons']) < 0 or int(serieDataToBeAddToProfileUser['watchedSerieEpisodes']) < 0:
                    serieDataToBeAddToProfileUser = {}
                    return(serieDataToBeAddToProfileUser)
            cursor.execute(
                f"""SELECT * from watched WHERE watchedUserId={serieDataToBeAddToProfileUser['userId']}""")
            serieRowsData = cursor.fetchall()
            for itemSerieData in serieRowsData:
                if int(itemSerieData[2]) == int(serieDataToBeAddToProfileUser['serieId']):
                    serieDataToBeAddToProfileUser = {}
                    return(serieDataToBeAddToProfileUser)
            cursor.execute(
                f"""INSERT INTO watched VALUES(Null, {serieDataToBeAddToProfileUser['userId']}, {serieDataToBeAddToProfileUser['serieId']}, {serieDataToBeAddToProfileUser['watchedSerieSeasons']}, {serieDataToBeAddToProfileUser['watchedSerieEpisodes']}, {serieDataToBeAddToProfileUser['starsFeedback']})""")
            connection.commit()
            return(serieDataToBeAddToProfileUser)

        def getAllSeriesFunction():

            allSeriesData = {}
            cursor.execute("""SELECT * from series""")
            allSeriesRowsData = cursor.fetchall()
            for itemOfAllSeries in allSeriesRowsData:
                allSeriesData[itemOfAllSeries[0]] = {"serieTitle": itemOfAllSeries[1], "serieSeasons": itemOfAllSeries[2],
                               "serieEpisodes": itemOfAllSeries[3], "serieLogo": f'{decodeBinaryBlobImage(itemOfAllSeries[4])}',"serieFormatImage": itemOfAllSeries[6], "serieGenre": itemOfAllSeries[5], "serieId": itemOfAllSeries[0]}
            return allSeriesData

        def deleteSerieOfUserProfileFunction(watchedIdToDelete):

            cursor.execute(
                f"""DELETE FROM watched WHERE watchedId={watchedIdToDelete}""")
            connection.commit()
            return watchedIdToDelete

        def getSpecificSerieByIdsFunction(userId, serieId):

            specificSerieToBeReturned = {}
            httpMethodToBeUsed = 'post'
            serieProcessUniqueId = ''
            if userId == 'undefined':
                cursor.execute(f"""SELECT * FROM series WHERE serieId={serieId}""")
                specificSerieRowsData = cursor.fetchall()
                for itemSpecificSerieRowsData in specificSerieRowsData:
                    specificSerieToBeReturned["serieData"] = {"serieId": itemSpecificSerieRowsData[0], "serieTitle": itemSpecificSerieRowsData[1], "serieSeasons": itemSpecificSerieRowsData[2], "serieLogo": f'{decodeBinaryBlobImage(itemSpecificSerieRowsData[4])}',
                                      "serieEpisodes": itemSpecificSerieRowsData[3], "serieFormatImage": f'{itemSpecificSerieRowsData[6]}', "serieGenre": itemSpecificSerieRowsData[5], "serieHttpMethod": httpMethodToBeUsed}
                return specificSerieToBeReturned

            else:
                cursor.execute(
                    f"""SELECT * from watched WHERE watchedUserId= {userId} AND watchedSerieId = {serieId}""")
                userSpecificSerieRowsFromProfileData = cursor.fetchall()
                if len(userSpecificSerieRowsFromProfileData) != 0:
                    httpMethodToBeUsed = 'put'
                    for itemSpecificSerie in userSpecificSerieRowsFromProfileData:
                        serieProcessUniqueId = itemSpecificSerie[0]
                cursor.execute(f"""SELECT * FROM series WHERE serieId={serieId}""")
                userSpecificSerieRowsFromProfileData = cursor.fetchall()
                for itemSpecificSerie in userSpecificSerieRowsFromProfileData:
                    specificSerieToBeReturned["serieData"] = {"serieProcessUniqueId": serieProcessUniqueId, "serieId": itemSpecificSerie[0], "serieTitle": itemSpecificSerie[1], "serieSeasons": itemSpecificSerie[2], "serieLogo": f'{decodeBinaryBlobImage(itemSpecificSerie[4])}',
                                      "serieEpisodes": itemSpecificSerie[3], "serieFormatImage": f'{itemSpecificSerie[6]}', "serieGenre": itemSpecificSerie[5], "serieHttpMethod": httpMethodToBeUsed}
                return specificSerieToBeReturned

        def updateSerieOfUserProfileFunction(recevedSerieIdToUpdate, recevedSerieDataToUpdate):

            serieDataUpdatedToBeReturned = {}
            serieDataToBeUpdated = recevedSerieDataToUpdate['newUserSerieDataToUpdate']
            cursor.execute(
                f"""UPDATE watched SET watchedSeasons={serieDataToBeUpdated['watchedSeasons']}, watchedEpisodes={serieDataToBeUpdated['watchedEpisodes']}, watchedGivedStars={serieDataToBeUpdated['watchedGivedStars']} WHERE watchedId={recevedSerieIdToUpdate}""")
            connection.commit()
            cursor.execute(f"""SELECT * FROM watched WHERE watchedId={recevedSerieIdToUpdate}""")
            serieRowsDataUpdated = cursor.fetchall()
            for itemSerieDataUpdated in serieRowsDataUpdated:
                serieDataUpdatedToBeReturned[itemSerieDataUpdated[0]] = {"watchedSeasons": itemSerieDataUpdated[3], "watchedEpisodes": itemSerieDataUpdated[4]}
            return (serieDataUpdatedToBeReturned)

        def getAllSeriesAddedByUserFunction(userUniqueId):

            allUserSeriesDataToBeReturned = {}
            contToDictId = 0
            cursor.execute(
                f"""SELECT * from watched INNER JOIN series ON watched.watchedSerieId = series.serieId WHERE watched.watchedUserId = {userUniqueId};""")
            allUserProfileSeriesData = cursor.fetchall()
            for itemAllUserProfileSeriesData in allUserProfileSeriesData:
                contToDictId += 1
                allUserSeriesDataToBeReturned[contToDictId] = {"serieProcessUniqueId": itemAllUserProfileSeriesData[0], "userId": itemAllUserProfileSeriesData[1], "serieId": itemAllUserProfileSeriesData[2], "watchedSeasons": itemAllUserProfileSeriesData[3], "watchedEpisodes": itemAllUserProfileSeriesData[4], "watchedGivedStars": itemAllUserProfileSeriesData[5],
                              "serieTitle": itemAllUserProfileSeriesData[7], "serieSeasons": itemAllUserProfileSeriesData[8], "serieEpisodes": itemAllUserProfileSeriesData[9], "serieLogo": f'{decodeBinaryBlobImage(itemAllUserProfileSeriesData[10])}',"serieFormatImage": f'{itemAllUserProfileSeriesData[12]}', "serieGenre": itemAllUserProfileSeriesData[11]}
            for itemSerieSpecificId in allUserSeriesDataToBeReturned:
                cursor.execute(f"""SELECT AVG(CAST(watchedGivedStars as FLOAT)) FROM watched WHERE watchedSerieId={allUserSeriesDataToBeReturned[itemSerieSpecificId]['serieId']}""")
                userRowsGivedStars = cursor.fetchall()
                for itemUserGivedStarsAVG in userRowsGivedStars:
    
                    allUserSeriesDataToBeReturned[itemSerieSpecificId]["serieStarsAVG"] = itemUserGivedStarsAVG[0]
                    
            return (allUserSeriesDataToBeReturned)

except Error as e:
    print('error', e)
