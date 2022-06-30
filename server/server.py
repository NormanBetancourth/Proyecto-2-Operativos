from flask import Flask
from flask import request
from threading import  Lock
from googletrans import Translator
import logging 

# traducciones = {
#     'carro':'car',
#     'casa':'house',
#     'caballo':'horse',
#     'silla':'chair',
#     'libro':'book',
#     }

translator = Translator()

mutex = Lock()
logging.basicConfig(filename='file.log', format='%(asctime)s - %(message)s', level=logging.INFO)


def saveLog(headers, palabra):  
    logging.info(f"Palabra:{palabra}") 
    


app = Flask(__name__)

@app.route('/traductor')
def get():
    result = 'not found'
    try:
      textoParse = request.args.get('palabra')[1:]
      codigoTrasl = textoParse[0:2]
      text = textoParse[3:]
      textoSalida = translator.translate(text, dest=codigoTrasl); 
      result =textoSalida.text
    except:
      result = 'not foundd'

    mutex.acquire()
    saveLog(request.headers, request.args.get('palabra')[1:])
    mutex.release()
    
    
    return result
    
    
    



app.run(host='localhost', port=5000)
