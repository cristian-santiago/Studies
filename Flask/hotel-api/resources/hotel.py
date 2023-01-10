from flask_restful import Resource, reqparse
from models.hotel import HotelModel
from flask_jwt_extended import jwt_required
import sqlite3


def normalize_path_params(
    cidade=None,
    estrelas_min = 0,
    estrelas_max = 5,
    diaria_min = 0,
    diaria_max = 10000,
    limit = 50,
    offset = 0, **dados):

    if cidade:
        return {
            'estrelas_min': estrelas_min,
            'estrelas_max': estrelas_max,
            'diaria_min' : diaria_min,
            'diaria_max' : diaria_max,
            'cidade': cidade,
            'limit' : limit,
            'offset' : offset
        }
    
    
    return {
        'estrelas_min': estrelas_min,
        'estrelas_max': estrelas_max,
        'diaria_min' : diaria_min,
        'diaria_max' : diaria_max,        
        'limit' : limit,
        'offset' : offset
    }



path_params = reqparse.RequestParser()
path_params.add_argument('cidade', type=str)
path_params.add_argument('estrelas_min', type=float)
path_params.add_argument('estrelas_max', type=float)
path_params.add_argument('diaria_min', type=float)
path_params.add_argument('diaria_max0', type=float )
path_params.add_argument('limit',type=float)
path_params.add_argument('offset', type=float)


class Hoteis(Resource):
    def get(self):

        connection = sqlite3.connect('hotel.db')
        cursor = connection.cursor()      


        dados = path_params.parse_args()
        dados_validos = {chave:dados[chave] for chave in dados if dados[chave] is not None} #received only the valida data from path_params
        parametros = normalize_path_params(**dados_validos)

        if not parametros.get('cidade'):
            consulta = """
            SELECT * FROM hoteis
            WHERE (estrelas > ? and estrelas < ?)
            AND (diaria > ? and diaria < ?)
            LIMIT ? OFFSET ?            
            """
            tupla = tupla([parametros[chave] for chave in parametros])
            resultado = cursor.execute(consulta, tupla)
        else:
            consulta = """
            SELECT * FROM hoteis
            WHERE (estrelas > ? and estrelas < ?)
            AND (diaria > ? and diaria < ?)
            AND cidade = ? LIMIT ? OFFSET ?            
            """
            tupla = tupla([parametros[chave] for chave in parametros])
            resultado = cursor.execute(consulta, tupla)
        hoteis = []
        for i in resultado:
            hoteis.append()
           
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
        #hoteis = [hotel for hotel in hoteis if hotel['hotel_id'] != hotel_id]        
        