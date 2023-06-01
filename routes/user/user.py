from flask import Blueprint,request,jsonify,render_template, url_for, redirect
from sqlalchemy import exc 
from models import Usuario, Donante
from app import db,bcrypt
from auth import tokenCheck,verificarToken

appuser=Blueprint('appuser',__name__,template_folder='templates')



@appuser.route('/VerUsuarios', methods=["GET"])
def verUsuarios():
    usuarios = Usuario.query.all()
    return render_template('usuarios/usuarios.html', usuarios=usuarios)

@appuser.route('/AdminVeUsuarios', methods=["GET"])
@tokenCheck
def getUsuarios(usuario):
    print(usuario)
    if(usuario['admin']):
        usuarios = Usuario.query.all()
        return render_template('usuarios/usuarios.html', usuarios=usuarios)
    else:
        return jsonify({"message":"Acceso denegado"}) 

@appuser.route('/auth/login', methods=['POST'])
def login():
    user = request.get_json()
    usuario = Usuario(email=user["email"], password=user["password"])
    searchUser = Usuario.query.filter_by(email=usuario.email).first()
    if searchUser:
        validation = bcrypt.check_password_hash(searchUser.password, user["password"])
        if validation:
            auth_token = usuario.encode_auth_token(user_id=searchUser.id)
            responseObject = {
                'status':'success',
                'message':'Loggin exitoso',
                'auth_token':auth_token,
                'id':searchUser.id,
                'admin':searchUser.admin
            }
            return jsonify(responseObject)
    return jsonify({'message':'Datos incorrectos'})


@appuser.route('/donaciones', methods=["GET"])
@tokenCheck
def getDonaciones(dons):
    output=[]
    donaciones = Donante.query.all()
    for dons in donaciones:
        donacionData = {}
        donacionData['usuario_id'] = dons.usuario_id
        donacionData['monto'] = dons.monto
        output.append(donacionData)
    return jsonify({'donaciones':output})


@appuser.route('/auth/registrodonacion', methods=['POST'])
def registrodonacion():
    donacion = request.get_json()
    print(donacion)
    donante = Donante(monto=donacion["monto"], usuario_id=donacion["usuario_id"], tarjeta=donacion["tarjeta"])
    try:
        db.session.add(donante)
        db.session.commit()
        mensaje="Donación exitosa!"
    except exc.SQLAlchemyError as e:
        mensaje="Error"
    return jsonify({'message':mensaje})