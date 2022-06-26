from flask import Flask
from flask import request

import threading
from threading import Thread, Lock

traducciones = {
    'carro':'car',
    'casa':'house',
    'caballo':'horse',
    'silla':'chair',
    'libro':'book',
    }


def thread_fuc(headers, palabra):
    mutex.acquire()
    try:
        print(palabra)
        print(headers)
        respuesta = traducciones[palabra]
        print('respuesta: '+respuesta)
    finally:
        mutex.release()

    return respuesta
    

mutex = Lock()

app = Flask(__name__)

@app.route('/traductor')
def get():
    
    print(request)
    x = threading.Thread(target=thread_fuc, args=(request.headers, request.args.get('palabra')[1:],))
    x.start()
    
    #TODO: arbir el hilo, una vez creado agregamos al log y retornamos la respuesta
    # return request.args.get('palabra')
    return traducciones[request.args.get('palabra')[1:]]



app.run(host='localhost', port=5000)
