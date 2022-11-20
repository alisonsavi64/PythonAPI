import mysql.connector
import base64
from mysql.connector import Error

def convert(file):
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

        def signup(data):

            compare = data['data']
            ninfos = {}
            cursor.execute(
                f"""SELECT * FROM users WHERE email='{compare['email']}'""""")
            rows = cursor.fetchall()
            if rows == []:
                cursor.execute(f"""INSERT INTO users VALUES(
				Null, 
				'{compare['name']}', 
				'{compare['email']}', 
				'{compare['password']}')""")
                connection.commit()
                cursor.execute(
                    f"""SELECT id, name  FROM users WHERE email='{compare['email']}' AND password='{compare['password']}'""")
                rows = cursor.fetchall()
                for i in rows:
                    ninfos["user"] = {"id": i[0], "name": i[1]}
                return(ninfos)
            else:
                return {}

        def login(data):

            compare = data['data']
            infos = {}
            #Função junto com o signup
            cursor.execute(
                f"""SELECT id, name  FROM users WHERE email='{compare['email']}' AND password='{compare['password']}'""")
            rows = cursor.fetchall()
            if len(rows) == 0:
                return({})
            else:
                for i in rows:
                    infos["user"] = {"id": i[0], "name": i[1]}
                return(infos)

        def addseries(data):

            infos = data['data']
            cursor.execute(
                f"""SELECT * from series WHERE id={infos['serieid']}""")
            rows = cursor.fetchall()
            for i in rows:
                if int(i[2]) < int(infos['temps']) or int(i[3]) < int(infos['eps']) or int(infos['temps']) < 0 or int(infos['eps']) < 0:
                    infos = {}
                    return(infos)
            cursor.execute(
                f"""SELECT * from watched WHERE id_user={infos['userid']}""")
            rows = cursor.fetchall()
            print(rows)
            for i in rows:
                print(i)
                if int(i[2]) == int(infos['serieid']):
                    infos = {}
                    return(infos)
            cursor.execute(
                f"""INSERT INTO watched VALUES(Null, {infos['userid']}, {infos['serieid']}, {infos['temps']}, {infos['eps']}, {infos['stars']})""")
            connection.commit()
            return(infos)

        def all():

            infos = {}
            cursor.execute("""SELECT * from series""")
            rows = cursor.fetchall()
            for i in rows:
                infos[i[0]] = {"title": i[1], "temps": i[2],
                               "eps": i[3], "img": f'{convert(i[4])}',"format": i[6], "genre": i[5], "id": i[0]}
            return infos

        def delseries(data):

            cursor.execute(
                f"""DELETE FROM watched WHERE id={data}""")
            connection.commit()
            return data

        def getsid(uid, sid):

            serie = {}
            method = 'post'
            processid = ''
            if uid == 'undefined':
                cursor.execute(f"""SELECT * FROM series WHERE id={sid}""")
                rows = cursor.fetchall()
                for i in rows:
                    serie["serie"] = {"id": i[0], "title": i[1], "temps": i[2], "img": f'{convert(i[4])}',
                                      "eps": i[3], "format": f'{i[6]}', "genre": i[5], "met": method}
                return serie

            else:
                cursor.execute(
                    f"""SELECT * from watched WHERE id_user = {uid} AND id_serie = {sid}""")
                rows = cursor.fetchall()
                if len(rows) != 0:
                    method = 'put'
                    for i in rows:
                        processid = i[0]
                cursor.execute(f"""SELECT * FROM series WHERE id={sid}""")
                rows = cursor.fetchall()
                for i in rows:
                    serie["serie"] = {"processid": processid, "id": i[0], "title": i[1], "temps": i[2], "img": f'{convert(i[4])}',
                                      "eps": i[3], "format": f'{i[6]}', "genre": i[5], "met": method}
                return serie

        def updateserie(id, data):

            serie = {}
            infos = data['data']
            print(infos)
            cursor.execute(
                f"""UPDATE watched SET tempsa={infos['tempsa']}, epsa={infos['epsa']}, stars= {infos['stars']} WHERE id={id}""")
            connection.commit()
            cursor.execute(f"""SELECT * FROM watched WHERE id={id}""")
            rows = cursor.fetchall()
            for i in rows:
                serie[i[0]] = {"tempsa": i[3], "epsa": i[4]}
            return (serie)

        def getsu(id):

            data = {}
            cont = 0
            cursor.execute(
                f"""SELECT * from watched INNER JOIN series ON watched.id_serie = series.id WHERE watched.id_user = {id};""")
            rows = cursor.fetchall()

            for i in rows:
                cont += 1
                data[cont] = {"processid": i[0], "iduser": i[1], "idserie": i[2], "tempsa": i[3], "epsa": i[4], "stars": i[5],
                              "title": i[7], "temps": i[8], "eps": i[9], "img": f'{convert(i[10])}',"format": f'{i[12]}', "genre": i[11]}
            for i in data:
                cursor.execute(f"""SELECT AVG(CAST(stars as FLOAT)) FROM watched WHERE id_serie={data[i]['idserie']}""")
                stars_data = cursor.fetchall()
                for p in stars_data:
                    data[i]["starsAVG"] = p[0]

            return (data)

except Error as e:
    print('error', e)
