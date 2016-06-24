#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# Prueba de código para contar las palabras de un texto de prueba sacado de la novela "El Beso de Julia", por Pablo Manuel Pérez Moreno
#

#
# Rubén Martín Moreno
#


# Importo las funciones que he creado
import modulo_funciones as func

# Cargo el texto y lo leo en la variable texto_sin_limpiar
capitulo1 = open('texto-prueba3.txt', 'r')
texto_sin_limpiar = capitulo1.read()

# Limpio el texto de caracteres especiales y lo dejo todo en minúscula
texto_limpio = func.limpia_texto(texto_sin_limpiar)

# Separa el texto en sus frases
frases = func.por_frases(texto_limpio)

# Separa las frases en palabras
frases = func.por_palabras(frases)

# Crea como claves las palabras y como valores las veces que están repetidas en el texto
diccionario = func.crea_dict(frases)

# Graba los valores en un archivo llamado 'resultado_completo'
lista_ordenada = func.escribe_lista(diccionario, 'resultado_completo.txt')

# Cierra el archivo abierto
capitulo1.close()


