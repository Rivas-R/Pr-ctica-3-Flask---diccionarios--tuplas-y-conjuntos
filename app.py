from flask import Flask, json
import ast

from practica1 import *

app = Flask(__name__)

# Diccionario: {"a": 1, "b": 2} -> %7B%22a%22%3A%201%2C%20%22b%22%3A%202%7D
@app.route("/dict/<path:diccio>")
def show_diccionario(diccio):
    diccionario = json.loads(diccio)
    result = []
    for clave, valor in diccionario.items():
        result.append(f"{clave}: {valor}")

    agregar_clave_valor(diccionario, "c", 3)
    result.append("Se agregó la clave 'c' con el valor 3.")
    eliminar_clave(diccionario, "a")
    result.append("Se eliminó la clave 'a'.")
    modificar_valor(diccionario, "b", 5)
    result.append("Se modificó el valor de la clave 'b' a 5.")
    combinar_diccionarios(diccionario, {"d": 4})
    result.append("Se combinó con otro diccionario {'d': 4}.")
    imprimir_diccionario(diccionario)
    result.append("Se imprimió el diccionario.")

    # Append the final state of the dictionary
    result.append(f"Diccionario final: {diccionario}")

    return "\n".join(result)

# Tupla: (1, 2, 3) -> %281%2C%202%2C%203%29
@app.route("/tuple/<path:tupla>")
def show_tuple(tupla):
    tupla = ast.literal_eval(tupla)
    result = []
    if isinstance(tupla, tuple):
        for item in tupla:
            result.append(f"Elemento de la tupla: {item}")

        tupla = agregar_elemento_tupla(tupla, 4)
        result.append("Se agregó el elemento 4 a la tupla.")
        tupla = eliminar_elemento_tupla(tupla, 2)
        result.append("Se eliminó el elemento 2 de la tupla.")
        tupla = concatenar_tuplas(tupla, (5, 6))
        result.append("Se concatenó con otra tupla (5, 6).")
        tupla = revertir_tupla(tupla)
        result.append("Se revirtió la tupla.")
        imprimir_tupla(tupla)
        result.append("Se imprimió la tupla.")

        # Append the final state of the tuple
        result.append(f"Tupla final: {tupla}")

    return "\n".join(result)

# Conjunto: {1, 2, 3} -> %7B1%2C%202%2C%203%7D
@app.route("/set/<path:conjunto>")
def show_set(conjunto):
    conjunto = ast.literal_eval(conjunto)
    result = []
    if isinstance(conjunto, set):
        for item in conjunto:
            result.append(f"Elemento del conjunto: {item}")

        agregar_elemento_conjunto(conjunto, 4)
        result.append("Se agregó el elemento 4 al conjunto.")
        eliminar_elemento_conjunto(conjunto, 2)
        result.append("Se eliminó el elemento 2 del conjunto.")
        combinar_conjuntos(conjunto, {5, 6})
        result.append("Se combinó con otro conjunto {5, 6}.")
        diferencia_conjuntos(conjunto, {3})
        result.append("Se calculó la diferencia con el conjunto {3}.")
        imprimir_conjunto(conjunto)
        result.append("Se imprimió el conjunto.")

        # Append the final state of the set
        result.append(f"Conjunto final: {conjunto}")

    return "\n".join(result)