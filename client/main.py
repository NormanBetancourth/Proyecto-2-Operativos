import requests

palabra =  input("Seleccione la opcion: ").lower()
print(palabra)

url = f"http://localhost:5000/traductor?palabra=${palabra}"
res = requests.get(url)
print(res)