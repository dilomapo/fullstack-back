"""
App
"""
from flask import Flask, request, redirect, Response
from persistencia import guardar_pedido

app = Flask (__name__)

@app.route("/checksize",methods=['POST'])
def checksize():
    """
    Pizza
    """
    tamano = request.form.get("tam")
    mensaje = ""

    if (tamano=="S"):
        mensaje = "No disponible"
    else:    
        mensaje = "Disponible"
    
    print("Tamano: "+tamano)
    return Response(mensaje, 200, {'Access-Control-Allow-Origin': '*'})
