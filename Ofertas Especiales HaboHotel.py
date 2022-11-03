import requests
import html
url =  requests.get(f"https://images.habbo.com/habbo-web-news/es/production/front.json")
OfertasEspecialesHaboHotel = html.unescape(url.json()[3]['summary']) #Ofertas  especiales habbo hotel
print("Ofertas Especiales Habbo Hotel: " + OfertasEspecialesHaboHotel)
