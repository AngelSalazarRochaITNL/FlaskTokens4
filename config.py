class BasicConfig:
    # Configuracion de la base de datos
    USER_DB = 'postgres'
    PASS_DB = 'Yon1thek1'
    URL_DB = 'localhost'
    NAME_DB = 'flask_tokens4'
    FULL_URL_DB = f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'
    SQLALCHEMY_DATABASE_URI = FULL_URL_DB
    DEBUG=True
    SECRET_KEY="secretKey1212"
    BCRYPT_LOG_ROUNDS=13
    SQLALCHEMY_TRACK_MODIFICATIONS=False