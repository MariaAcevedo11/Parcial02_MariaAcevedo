from flask import Flask, jsonify #jsonify viene con flask entonces no hay necesidad de instalarla 
import math

app = Flask(__name__)

@app.route('/calcular/<int:num>', methods=['GET'])
def calcular(num):
    factorial = math.factorial(num)
    etiqueta = "par" if num % 2 == 0 else "impar"

    resultado = {
        "numero": num,
        "factorial": factorial,
        "etiqueta": etiqueta
    }
    return jsonify(resultado) #Hace el archivo json 

if __name__ == '__main__':
    app.run(debug=True) #Para que se vea bonito jeje 
