from flask_sqlalchemy import SQLAlchemy

#Ini BD
db = SQLAlchemy()

#Definir Usuarios

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key =True)
    nome = db.Column(db.String(80), nullable=False )
    email = db.Column(db.String (80), unique= True, nullable=False)

    def __repr__(self):
        return f'<Usuario {self.nome}>'
    
#Função para inicializar o Bd

def init_db(app):
 #Configurar o bd
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meubanco.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
       db.create_all()
