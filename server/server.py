from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/traductor')
def get():
    print(request.args.get('palabra'))
    print(request)
    headers = request.headers
    print(headers)

    return request.args.get('palabra')

    #TODO: aqui es donde se debe crear el hilo y orquestar lo de los logs
app.run(host='localhost', port=5000)
