from flask import Flask, request
import jsonpickle
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

from app import views
