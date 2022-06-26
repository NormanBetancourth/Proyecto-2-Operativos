import requests

palabra =  input("Seleccione la opcion: ").lower()

url = f"http://localhost:5000/traductor?palabra=${palabra}"
res = requests.get(url)
print(res.content)


#TODO: cuando no se encuentre la respuesta se usa el not fount
#TODO: Nota: esto debe ir en el servidor

car = None
map = {'carro':'res'}
try:
  car = map["a"]
except:
  car = 'not found'

print(car)