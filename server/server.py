from unittest import result
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

mutex = Lock()

def thread_fuc(headers, palabra, rs):
    
    mutex.acquire()
    print('entra al th')
    print(palabra)
    print(headers)
    result = traducciones[palabra]
    mutex.release()


app = Flask(__name__)

@app.route('/traductor')
def get():
    global result
    result = 'aa'
    #Tenemos un problema, no se retornan las traducciones


    print(request)
    x = threading.Thread(target=thread_fuc, args=(request.headers, request.args.get('palabra')[1:],result,))

    print('antes de iniciar el th')
    
    
    x.start()
    x.join()
    
    print('cuando acaba el th')
    return traducciones[request.args.get('palabra')[1:]]
    

    # return result
    
    



app.run(host='localhost', port=5000)
