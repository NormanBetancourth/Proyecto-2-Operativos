import requests

palabra =  input("Escriba la frase que se va a tarducir posterior al codigo del idioma: ").lower()

url = f"http://localhost:5000/traductor?palabra=${palabra}"
res = requests.get(url)
print(f'La traducción de "{palabra[3:]}" en el idioma "{palabra[0:2]}" es : {res.content}')