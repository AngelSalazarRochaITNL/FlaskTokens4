from flask import Flask, request, render_template, jsonify,redirect, url_for
from database import db
from encriptador import bcrypt
from flask_migrate import Migrate
from config import BasicConfig
from flask_cors import CORS
from routes.user.user import appuser
from routes.images.images import imageUser
from routes.csv.csv import appcsv
from routes.donante.donante import appdonante
from models import Usuario
from auth import verificarToken

app = Flask(__name__)

app.register_blueprint(appuser)
app.register_blueprint(imageUser)
app.register_blueprint(appcsv)
app.register_blueprint(appdonante)
app.config.from_object(BasicConfig)

CORS(app)

bcrypt.init_app(app)
db.init_app(app)

migrate = Migrate()
migrate.init_app(app,db)



@app.route('/')
def index():
    return redirect(url_for('login_post'))


@app.route('/main')
def main():
    return render_template('main/main.html')


@app.route('/signin',methods=["GET","POST"])
def registrar():
    if request.method=="GET":
        return render_template('main/registrar.html')
    else:
        email = request.json["email"]
        password=request.json["password"]
        nombre=request.json["nombre"]
        usuario = Usuario(email=email,password=password,nombre=nombre)
        userExists=Usuario.query.filter_by(email=email).first()
        if not userExists:
            try:   
                db.session.add(usuario)
                db.session.commit()
                responseObject={
                    "status":"Success",
                    "message":"Registro Exitoso"
                }
            except Exception as e:
                responseObject={
                    "status":"Error",
                    "message": e
                }
        else:
            responseObject={
                "status":"Error",
                "message":"Ya existe el usuario"
            }
        return jsonify(responseObject)


@app.route('/login/user',methods=["GET","POST"])
def login_post():
    return render_template("main/login.html")


@app.route('/logout')
def logout():
    return render_template("")

