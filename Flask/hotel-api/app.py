from flask import Flask, jsonify
from flask_restful import Api
from resources.hotel import Hoteis, Hotel
from resources.usuario import User, UserRegister, UserLogin, UserLogout
from resources.site import Site, Sites
from flask_jwt_extended import JWTManager
from blacklist import BLACKLIST

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLACHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'DontTellAnyone'
app.config['JWT_BLACKLIST_ENABLE'] = True

api = Api(app)
jwt = JWTManager(app)

@app.before_first_request
def cria_banco():
    banco.create_all()

@jwt.token_in_blocklist_loader
def verifica_blacklist(self, token):
    return token['jti'] in BLACKLIST

@jwt.revoked_token_loader
def token_de_acesso_invalidado(jwt_header, jwt_payloader):
    return jsonify({'message' : 'You have been logged out'}), 401  # convert a dict to json

api.add_resource(Hoteis, '/hoteis') # will display all the hotels in database
api.add_resource(Hotel, '/hoteis/<string:hotel_id>') # this resource will only get strings id
api.add_resource(User, '/usuarios/<int:user_id>') # this resource will only get integer id
api.add_resource(UserRegister, '/cadastro')
api.add_resource(UserLogin, '/login')
api.add_resource(UserLogout, '/logout')
api.add_resource(Sites, '/sites') #will display all sites in database
api.add_resource(Site, '/sites/<string:url>')

if __name__== '__main__':

    from sql_alchemy import banco
    banco.init_app(app)

    app.run(debug=True)