import requests
import html
url =  requests.get(f"https://images.habbo.com/habbo-web-news/es/production/front.json")
SeguridadHabbo = html.unescape(url.json()[10]['summary']) #Seguridad Habbo Hotel
print("Seguridad Habbo: " +SeguridadHabbo)
