import requests

#print(requests.__version__)

#print(requests.get("http://www.google.com/"))

var = requests.get("https://raw.githubusercontent.com/colinchoix/404Labs/master/Lab1/script.py")

print(var.text)
