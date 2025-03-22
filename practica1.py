# Práctica 1: Funciones en python
# Rivas Alfaro Raul Heriberto

def agregar_clave_valor(diccionario, clave, valor):
    """Agregar una clave-valor a un diccionario y retornarlo modificado."""
    print(f"Diccionario original: {diccionario} (se agregará la clave '{clave}' con el valor '{valor}')")
    diccionario[clave] = valor  # Se agrega la clave-valor
    print("Diccionario modificado:", diccionario)
    return diccionario


def eliminar_clave(diccionario, clave):
    """Eliminar una clave de un diccionario y retornarlo modificado."""
    if clave in diccionario:
        print(f"Diccionario original: {diccionario} (se eliminará la clave '{clave}')")
        del diccionario[clave]  # Se elimina la clave si existe
    else:
        print(f"Diccionario original: {diccionario} (la clave '{clave}' no se encontró, no se realizará ningún cambio)")
    print("Diccionario modificado:", diccionario)
    return diccionario


def modificar_valor(diccionario, clave, nuevo_valor):
    """Modificar el valor de una clave en un diccionario, retornar True si se pudo modificar y False si no."""
    if clave in diccionario:
        print(f"Diccionario original: {diccionario} (se modificará la clave '{clave}' con el nuevo valor '{nuevo_valor}')")
        diccionario[clave] = nuevo_valor  # Modifica el valor si la clave existe
        print("Diccionario modificado:", diccionario)
        return True
    print(f"Diccionario original: {diccionario} (la clave '{clave}' no se encontró, no se realizará ningún cambio)")
    return False


def combinar_diccionarios(dic1, dic2):
    """Combinar dos diccionarios y regresar el diccionario resultante."""
    print("Diccionarios originales:", dic1, dic2)
    combinado = {**dic1, **dic2}  # Se combinan los diccionarios
    print("Diccionario combinado:", combinado)
    return combinado


def agregar_elemento_conjunto(conjunto, elemento):
    """Agregar un elemento a un conjunto, retornar True si se agregó y False si ya estaba."""
    print("Conjunto original:", conjunto)
    if elemento not in conjunto:
        conjunto.add(elemento)
        print(f"Conjunto modificado: {conjunto} (se agregó el elemento {elemento})")
        return True
    print("Elemento ya estaba en el conjunto.")
    return False


def eliminar_elemento_conjunto(conjunto, elemento):
    """Eliminar un elemento de un conjunto, retornar True si se eliminó y False si no estaba."""
    print("Conjunto original:", conjunto)
    if elemento in conjunto:
        conjunto.remove(elemento)
        print(f"Conjunto modificado: {conjunto} (se eliminó el elemento {elemento})")
        return True
    print("Elemento no estaba en el conjunto.")
    return False


def combinar_conjuntos(conj1, conj2):
    """Combinar dos conjuntos y regresar el conjunto resultante."""
    print("Conjuntos originales:", conj1, conj2)
    combinado = conj1 | conj2  # Se unen los conjuntos
    print(f"Conjunto combinado: {combinado} (resultado de unir {conj1} y {conj2})")
    return combinado


def diferencia_conjuntos(conj1, conj2):
    """Regresar la diferencia de dos conjuntos."""
    print("Conjuntos originales:", conj1, conj2)
    diferencia = conj1 - conj2  # Se obtiene la diferencia
    print(f"Diferencia de conjuntos: {diferencia} (elementos en {conj1} que no están en {conj2})")
    return diferencia


def agregar_elemento_tupla(tupla, elemento):
    """Agregar un elemento a una tupla y regresar una nueva tupla con los cambios."""
    nueva_tupla = tupla + (elemento,)  # Se crea una nueva tupla con el elemento agregado
    print(f"Tupla original: {tupla} (se agregará el elemento '{elemento}')")
    print("Tupla modificada:", nueva_tupla)
    return nueva_tupla


def eliminar_elemento_tupla(tupla, elemento):
    """Eliminar un elemento de una tupla y regresar una nueva tupla sin ese elemento."""
    nueva_tupla = tuple(x for x in tupla if x != elemento)  # Se crea una nueva tupla sin el elemento
    print(f"Tupla original: {tupla} (se eliminará el elemento '{elemento}')")
    print("Tupla modificada:", nueva_tupla)
    return nueva_tupla


def concatenar_tuplas(tupla1, tupla2):
    """Concatenar dos tuplas en una nueva y regresarla."""
    nueva_tupla = tupla1 + tupla2  # Se concatenan las tuplas
    print(f"Tuplas originales: {tupla1}, {tupla2} (se concatenarán)")
    print("Tupla concatenada:", nueva_tupla)
    return nueva_tupla


def revertir_tupla(tupla):
    """Revertir el orden de una tupla y regresar la nueva tupla."""
    nueva_tupla = tupla[::-1]  # Se invierte la tupla
    print(f"Tupla original: {tupla} (se invertirá el orden)")
    print("Tupla revertida:", nueva_tupla)
    return nueva_tupla


def imprimir_diccionario(diccionario):
    """Imprimir un diccionario."""
    print("Diccionario:", diccionario)


def imprimir_tupla(tupla):
    """Imprimir una tupla."""
    print("Tupla:", tupla)


def imprimir_conjunto(conjunto):
    """Imprimir un conjunto."""
    print("Conjunto:", conjunto)


if __name__ == "__main__":
    # Ejemplo de uso de las funciones
    dic = {"a": 1, "b": 2}
    agregar_clave_valor(dic, "c", 3)
    eliminar_clave(dic, "a")
    modificar_valor(dic, "b", 5)
    combinar_diccionarios(dic, {"d": 4})
    
    conj = {1, 2, 3}
    agregar_elemento_conjunto(conj, 4)
    eliminar_elemento_conjunto(conj, 2)
    combinar_conjuntos(conj, {5, 6})
    diferencia_conjuntos(conj, {3})
    
    tup = (1, 2, 3)
    agregar_elemento_tupla(tup, 4)
    eliminar_elemento_tupla(tup, 2)
    concatenar_tuplas(tup, (5, 6))
    revertir_tupla(tup)
    
    imprimir_diccionario(dic)
    imprimir_tupla(tup)
    imprimir_conjunto(conj)
