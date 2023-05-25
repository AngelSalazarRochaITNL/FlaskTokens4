from flask import Blueprint,request,jsonify,render_template
from sqlalchemy import exc 
from models import Usuario
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
                'admin':searchUser.admin
            }
            return jsonify(responseObject)
    return jsonify({'message':'Datos incorrectos'})


# @appuser.route('/registro',methods=["POST"])
# def registro():
#     user = request.get_json()
#     userExists =Usuario.query.filter_by(email=user['email']).first()
#     if not userExists:
#         usuario = Usuario(email=user['email'],password=user['password'])
#         try:
#             db.session.add(usuario)
#             db.session.commit()
#             mensaje="Usuario creado"
#         except exc.SQLAlchemyError as e:
#             mensaje  = e
#     else:
#         mensaje = "Usuario existente"  
#     return jsonify({"message":mensaje})

# @appuser.route('/login',methods=["POST"])
# def login():
#     user = request.get_json()
#     usuario = Usuario(email=user["email"],password=user["password"])
#     searchUser = Usuario.query.filter_by(email=usuario.email).first()
#     if searchUser:
#         validation = bcrypt.check_password_hash(searchUser.password,user["password"])
#         if validation:
#             auth = usuario.encode_auth_token(user_id=searchUser.id)
#             print(auth)
#             response = {
#                 "status":"success",
#                 "message":"Login exitoso",
#                 "auth_token":auth
#             }
#             return jsonify(response)
#     return jsonify({"message":"Datos incorrectos"})


# @appuser.route('/usuarios',methods=["GET"])
# @tokenCheck
# def getUsers(usuario):
#     print(usuario)
#     if(usuario['admin']):
#         response=[]
#         usuarios = Usuario.query.all()
#         for usuario in usuarios:
#             usuarioData={
#                 'id':usuario.id,
#                 'email':usuario.email,
#                 'password':usuario.password,
#                 'registrado':usuario.registrado,
#                 'admin':usuario.admin
#             }
#             response.append(usuarioData)
#         return jsonify({'usuarios':response})  
#     else: 
#         return jsonify({"message":"Acceso denegado"}) 