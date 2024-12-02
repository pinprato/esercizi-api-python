import requests

# Imposta la tua chiave API
api_key = "xxxx"

# URL dell'endpoint di WeatherAPI
url = "http://api.weatherapi.com/v1/current.json"

# Parametri della richiesta
params = {
    "key": api_key,
    "q": "Prato",
    "aqi": "no"  # Se non ti interessa la qualità dell'aria, puoi impostarla su "no"
}

# Effettua la richiesta POST
response = requests.post(url, data=params)

# Controlla se la richiesta è stata effettuata con successo
if response.status_code == 200:
    # Parsec l'output JSON
    data = response.json()
    print("Meteo attuale a Prato:")
    print(f"Temperatura: {data['current']['temp_c']} °C")
    print(f"Condizioni: {data['current']['condition']['text']}")
else:
    print("Errore nella richiesta:", response.status_code)
