import requests
import html
url =  requests.get(f"https://images.habbo.com/habbo-web-news/es/production/front.json")

NoticiasFansites =  html.unescape(url.json()[1]['summary']) #Noticias Fansites

print("Noticias Fansites: " + NoticiasFansites)