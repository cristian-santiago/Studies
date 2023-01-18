from flask_restful import Resource, reqparse
from models.hotel import HotelModel
from flask_jwt_extended import jwt_required
from resources.filttros import normalize_path_params, consulta_sem_ciade, consulta_com_cidade

import sqlite3





# Recebendo parâmetros de consulta

path_params = reqparse.RequestParser()
path_params.add_argument("cidade", type=str,location="values")
path_params.add_argument("estrelas_min", type=float,location="values")
path_params.add_argument("estrelas_max", type=float,location="values")
path_params.add_argument("diaria_min", type=float,location="values")
path_params.add_argument("diaria_max", type=float ,location="values")
path_params.add_argument("limit",type=float,location="values")
path_params.add_argument("offset", type=float,location="values")


class Hoteis(Resource):
    def get(self):


# Aplicando filtros avançados com parâmetros de consulta

        connection = sqlite3.connect('/home/cdasilva/Área de Trabalho/Studies/Flask/hotel-api/instance/banco.db')
        cursor = connection.cursor()      

        # Parâmetros de consulta via Path
        dados = path_params.parse_args()
        dados_validos = {chave:dados[chave] for chave in dados if dados[chave] is not None} #received only the valida data from path_params
        parametros = normalize_path_params(**dados_validos)

        if not parametros.get("cidade"):
            
            tupla = tuple([parametros[chave] for chave in parametros])
            resultado = cursor.execute(consulta_sem_ciade, tupla)
        else:
            
            tupla = tuple([parametros[chave] for chave in parametros])
            resultado = cursor.execute(consulta_com_cidade, tupla)
        hoteis = []

        for i in resultado:
            hoteis.append({
            "hotel_id": i[0],
            "nome": i[1],
            "estrelas" : i[2],
            "diária" : i[3],
            "cidade" : i[4]

            })
        
        return {"hoteis" : hoteis} 
        
           
        #return {'hoteis': [hotel.json() for hotel in HotelModel.query.all()]} #List comprehension

class Hotel(Resource):

    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome', type=str, required=True, help="The field 'nome' must be filled.")
    argumentos.add_argument('estrelas', type=float, required=True, help="The field 'estrlas' must be filled.")
    argumentos.add_argument('diária')
    argumentos.add_argument('cidade')

 
    #GET
    def get(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel:
            return hotel.json()
        return {'Message': 'Hotel not found'}, 404


    #POST
    @jwt_required()
    def post(self, hotel_id):      

        if HotelModel.find_hotel(hotel_id):
            return {"Message":f"Hotel id '{hotel_id}' already exists. "}, 400 #bad request

        dados = Hotel.argumentos.parse_args()
        hotel = HotelModel(hotel_id, **dados)
        try:
            hotel.save_hotel()
        except:
            return {'message': 'An error occured while trying to save.'}, 500 #internal server error

        return hotel.json()   


    #PUT
    @jwt_required()
    def put(self, hotel_id):

        dados = Hotel.argumentos.parse_args()
        hotel_encontrado = HotelModel.find_hotel(hotel_id)
        if hotel_encontrado:
            hotel_encontrado.update_hotel(**dados)
            hotel_encontrado.save_hotel()
            return hotel_encontrado.json(), 200
        hotel = HotelModel(hotel_id, **dados)
        try:
            hotel.save_hotel()
        except:
            return {'message': 'An error occured while trying to save.'}, 500 #internal server error        
        return hotel.json(), 201

    #DELETE
    @jwt_required()
    def delete(self, hotel_id):

        hotel = HotelModel.find_hotel(hotel_id)
        if hotel:
            try:
                hotel.delete_hotel()
            except:
                return {'message': 'An error occured while trying to delete.'}, 500 # internal server error
            return {'message': 'Hotel deleted.'}
        return {"message":f"Hotel '{hotel_id}' not found."}
        

        # Method to delete/remove an item from a json list
        #hoteis = [hotel for hotel in hoteis if hotel['hotel_id'] != hotel_id]    # list comprehension    
        