import requests
import html
url =  requests.get(f"https://images.habbo.com/habbo-web-news/es/production/front.json")
BuildersAtWork = html.unescape(url.json()[4]['summary']) #Constructores
print("Builders At Work: " + BuildersAtWork)
