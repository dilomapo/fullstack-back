"""
App
"""
from flask import Flask, request, redirect
from persistencia import guardar_pedido

app = Flask (__name__)

@app.route("/pizza",methods=['POST'])
def pizza():
    """
    Pizza
    """
    nombre = request.form.get("nm")
    apellido = request.form.get("ap")
    print("Nombre: "+nombre)
    print("Apellido: "+apellido)

    with open("pedidos.txt", "a", encoding="utf-8") as file:
        file.write("")
        file.close()
        guardar_pedido(nombre, apellido)
    return redirect("http://localhost/EJERCICIOS/Final/solicita_pedido.html", code=302)
