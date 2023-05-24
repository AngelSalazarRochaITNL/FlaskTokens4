from flask import Blueprint,request,jsonify,render_template
from models import Donante
from auth import tokenCheck
from sqlalchemy import exc
from app import db
import base64

appdonante = Blueprint('appdonante',__name__,template_folder="templates")

