import sqlite3

connection = sqlite3.connect('hotel.db')

cursor = connection.cursor()

criar_tabela = "CREATE TABLE IF NOT EXISTS hoteis (hoteis_id text PRIMARY KEY, nome text, estrelas real, diária real, cidade text)"

criar_hotel = "INSERT INTO hoteis VALUES ('second', 'Segundo Hotel', 4.3, 350.30, 'Itaguaí') "

cursor.execute(criar_tabela)
cursor.execute(criar_hotel)

connection.commit()
connection.close()