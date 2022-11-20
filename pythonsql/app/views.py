from app import app
from flask import request
import json
from app import database


@app.route("/api/user/signup", methods=['POST', 'GET'])
def sign():
    if request.method == 'POST':
        jinfos = json.loads(request.data.decode('utf-8'))
        ninfos = database.signup(jinfos)
    return (ninfos)


@app.route("/api/user/login", methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        jinfos = json.loads(request.data.decode('utf-8'))
        res_login = database.login(jinfos)
    return (res_login)


@app.route("/api/series/addseries", methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        jinfos = json.loads(request.data.decode('utf-8'))
        data = database.addseries(jinfos)
    return(data)


@app.route("/api/series/delseries/<id>", methods=['DELETE'])
def delete(id):
    print(database.delseries(id))
    return({"id": id})


@app.route("/api/series/updateseries/<id>", methods=['PUT'])
def updateseries(id):
    jinfos = json.loads(request.data.decode('utf-8'))
    infos = database.updateserie(id, jinfos)
    return (infos)


@app.route("/api/series/all", methods=['POST', 'GET'])
def all():
    infos = database.all()
    return(infos)

@app.route("/api/series/write", methods=['GET'])
def writeIMG():
    infos = database.writeimages()
    return (infos)


@app.route("/api/series/seriebyid/<userid>/<serieid>", methods=['GET'])
def getseriebyid(userid, serieid):
    infos = database.getsid(userid, serieid)
    return (infos)


@app.route("/api/series/seriesuser/<id>", methods=['GET'])
def getseriesuser(id):
    infos = database.getsu(id)
    return (infos)
