import requests

palabra =  input("Seleccione la opcion: ").lower()

url = f"http://localhost:5000/traductor?palabra=${palabra}"
res = requests.get(url)
print(f'La traducción a {palabra} es : {res.content}')