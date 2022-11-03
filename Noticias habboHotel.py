import requests
import html
url =  requests.get(f"https://images.habbo.com/habbo-web-news/es/production/front.json")

NoticiasHabboHotel =  html.unescape(url.json()[0]['summary']) #Noticias Habbo Hotel












print("Noticias HabboHotel: " + NoticiasHabboHotel)
