from flask_restful import Resource, reqparse
from models.hotel import HotelModel

hoteis = [

    { 
        'hotel_id': 'first',
        'nome': "Primeiro Hotel",
        'estrelas': 4.2,
        'diária':150.5,
        'cidade': 'Nova Iguaçu'

    },
    {
        'hotel_id': 'second',
        'nome': "Segundo Hotel",
        'estrelas': 4.7,
        'diária':395.9,
        'cidade': 'Caxias'
    },
    {
        'hotel_id': 'third',
        'nome': "Terceiro Hotel",
        'estrelas': 3.9,
        'diária':130.7,
        'cidade': 'Niterói'
    }


]

class Hoteis(Resource):
    def get(self):
        return {'hoteis': hoteis}

class Hotel(Resource):

    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('estrelas')
    argumentos.add_argument('diária')
    argumentos.add_argument('cidade')

    def find_hotel(hotel_id):

        for hotel in hoteis:
            if hotel['hotel_id']== hotel_id:
                return hotel
        return None

    # Implementando o GET
    def get(self, hotel_id):

        hotel = Hotel.find_hotel(hotel_id)
        if hotel:
            return hotel
        return {'Message': 'Hotel not found'}, 404


    # Implementando o POST
    def post(self, hotel_id):      

        dados = Hotel.argumentos.parse_args()
        hotel_objeto = HotelModel(hotel_id, **dados)
        novo_hotel = hotel_objeto.json()
        hoteis.append(novo_hotel)
        return novo_hotel, 201


    # Implementando o PUT
    def put(self, hotel_id):

        dados = Hotel.argumentos.parse_args()        
        hotel_objeto = HotelModel(hotel_id, **dados)
        novo_hotel = hotel_objeto.json()
        hotel = Hotel.find_hotel(hotel_id)
        if hotel:
            hotel.update(novo_hotel)
            return novo_hotel, 200

        hoteis.append(novo_hotel)
        return novo_hotel, 201

    # Implementando o DELETE
    def delete(self, hotel_id):

        global hoteis
        # Method to delete/remove an item from a json list
        hoteis = [hotel for hotel in hoteis if hotel['hotel_id'] != hotel_id]        
        return {'message': 'Hotel deleted.'}