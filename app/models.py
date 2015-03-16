from werkzeug.security import generate_password_hash, check_password_hash
from . import db, lm
from flask.ext.login import UserMixin

# Classe Usuari
class User(UserMixin, db.Model):
    # Taula SQL
    __tablename__ = 'users'
    #id unica de cada element
    id = db.Column(db.Integer, primary_key=True)
    #Nom de usuari
    username = db.Column(db.String(16), index=True, unique=True)
    #Contrasenya (encriptada)
    password_hash = db.Column(db.String(64))

    #Creem la contrasenya encriptada a partir del text pla rebut
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    #Comprovem la contrasenya amb el hash
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    #Metode per a registrar nous usuaris.
    @staticmethod
    def register(username, password):
        user = User(username=username)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()

    def __repr__(self):
        return '<User {0}'.format(self.username)

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))
