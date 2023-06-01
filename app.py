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
from forms import UserForm
from auth import verificarToken
# import logging

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
# logging.basicConfig(level=logging.DEBUG, filename="debug.log")
migrate.init_app(app,db)


# End points de login y filtro por admin/user
@app.route('/')
def index():
    uvacios = Usuario.query.first()
    if uvacios is None:
        return render_template('control_admin/control_admin.html')
    return redirect(url_for('login_post'))


@app.route('/login/user',methods=["GET","POST"])
def login_post():
    return render_template("main/login.html")


@app.route('/main/admin')
def main():
    return render_template('main/main_admin.html')


@app.route('/main/user')
def main_user():
    return render_template('main/main_user.html')


@app.route('/signin',methods=["GET","POST"])
def registrar():
    if request.method=="GET":
        return render_template('main/registrar.html')
    else:
        # Condición para el primer usuario administrador
        uvacios = Usuario.query.first()
        admin = False
        if uvacios is None:
            admin = True

        email = request.json["email"]
        password=request.json["password"]
        nombre=request.json["nombre"]
        administrador = admin
        usuario = Usuario(email=email,password=password,nombre=nombre, admin=administrador)
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




# Endpoints de menu de layout
@app.route('/perfil', methods=['GET'])
def perfil():
    return render_template('usuarios/perfil.html')

@app.route('/donar', methods=['GET'])
def donar():
    return render_template('usuarios/donar.html')

@app.route('/misdonaciones', methods=['GET'])
def misdonaciones():
    return render_template('usuarios/misdonaciones.php')


@app.route('/logout')
def logout():
    return render_template("main/logout.html")


# Endpoints del usuario
@app.route('/editar/usuario/<int:ID>', methods=["GET", "POST"])
def editarUsuario(ID):
    user=Usuario.query.get_or_404(ID)
    userForm = UserForm(obj=user)
    if request.method == "POST":
        if userForm.validate_on_submit():
            userForm.populate_obj(user)
            db.session.commit()
            return redirect(url_for('appuser.verUsuarios'))
    return render_template('usuarios/perfil.html', forma=userForm)
