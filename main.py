import requests
import telegram
import os

BOT_TOKEN = os.environ['']
CHAT_ID = os.environ['']

URL = "https://www.flylevel.com/nwe/flights/api/calendar/?triptype=RT&origin=EZE&destination=BCN&month=02&year=2026&currencyCode=USD"  # Reemplazá por la URL real

def revisar_precios():
    response = requests.get(URL)
    data = response.json()
    vuelos = data["data"]["dayPrices"]
    vuelos_baratos = [v for v in vuelos if v["price"] < 200]
    if vuelos_baratos:
        bot = telegram.Bot(token=BOT_TOKEN)
        for vuelo in vuelos_baratos:
            fecha = vuelo["date"]
            precio = vuelo["price"]
            mensaje = f"✈️ ¡Pasaje barato! Fecha: {fecha}, Precio: USD {precio}"
            bot.send_message(chat_id=CHAT_ID, text=mensaje)

if __name__ == "__main__":
    revisar_precios()
