from flask import Flask
from flask import request
from threading import  Lock
import logging 

traducciones = {
    'carro':'car',
    'casa':'house',
    'caballo':'horse',
    'silla':'chair',
    'libro':'book',
    }

mutex = Lock()
logging.basicConfig(filename='file.log', format='%(asctime)s - %(message)s', level=logging.INFO)

def saveLog(headers, palabra):  
    mutex.acquire()
    logging.info(f"{headers}\n Palabra:{palabra}") 
    mutex.release()


app = Flask(__name__)

@app.route('/traductor')
def get():
    result = 'not found'
    try:
      result = traducciones[request.args.get('palabra')[1:]]
    except:
      result = 'not found'

    saveLog(request.headers, request.args.get('palabra')[1:])
    
    return result
    
    
    



app.run(host='localhost', port=5000)
