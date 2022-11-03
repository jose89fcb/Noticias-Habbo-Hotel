import requests
import html
url =  requests.get(f"https://images.habbo.com/habbo-web-news/es/production/front.json")
ActualizacionesHabboHotel =  html.unescape(url.json()[2]['summary']) #Actualizaciones Habbo Hotel
print("Actualizaciones HabboHotel: " + ActualizacionesHabboHotel)