from sql_alchemy import banco

class HotelModel(banco.Model):

    __tablename__ = 'hoteis'

    hotel_id = banco.Column(banco.String, primary_key = True)
    nome = banco.Column(banco.String(80))
    estrelas = banco.Column(banco.Float(precision=1))
    diária = banco.Column(banco.Float(precision=2))
    cidate = banco.Column(banco.String(40))




    def __init__(self, hotel_id, nome, estrelas, diária, cidade):

        self.hotel_id = hotel_id
        self.nome = nome
        self.estrelas = estrelas
        self.diária = diária
        self.cidade = cidade


    def json(self):
        return {
            'hotel_id': self.hotel_id,
            'nome': self.nome,
            'estrelas' : self.estrelas,
            'diárias' : self.diária,
            'cidade' :self.cidade
        }