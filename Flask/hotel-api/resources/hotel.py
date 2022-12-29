from flask_restful import Resource, reqparse
from models.hotel import HotelModel


class Hoteis(Resource):
    def get(self):
        return {'hoteis': [hotel.json() for hotel in HotelModel.query.all()]} #List comprehension

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
        