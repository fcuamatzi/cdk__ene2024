#!/bin/python

from flask import Flask, request

app = Flask(__name__)

#metodos de apirest

@app.route('/')
def saludo():
    return 'hola desde mi servicio'

@app.route('/saludo/<persona>')
def saludoPersona(persona):
    return 'hola %s desde mi servicio' % persona

@app.route('/cuadrado/<float:num>')
def calculaCuadrado(num):
    resp = num*num
    return 'Respuesta %f desde mi servicio' %resp


@app.route('/test', methods=['POST', 'GET'])
def recibeParam():
    textReturn = "Método no aceptado"
    if request.method == "POST":
        data = request.get_json()
        try:
            mascota = data['mascota']
            numero = data['num'] * 2
            textReturn = 'Se recibio: %s,' % mascota
            textReturn = textReturn + ' por 2: %i' % numero
        except:
            textReturn = "Ocurrio un error"
    return textReturn

#lanzamiento de servidor
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)


