import requests
h = "https://allstartd.fandom.com/wiki/Codes#Working_Codes:
a = requests.get(h)
print(a)
print(a.text)