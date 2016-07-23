#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# HOJA DE FUNCIONES PARA EL PROYECTO ZIPF
#

#
# Rubén Martín Moreno
#

import os.path


def validar_entrada():
	while True:
		archivo = raw_input("Escribe el archivo que quieres analizar: ")
		archivo = str(archivo)
		if os.path.isfile(archivo):
			return archivo
		else:
			print "ATENCIÓN: Ese archivo no existe."


def validar_salida():
	'''Valida el valor de salida'''

	while True:
		archivo = raw_input("Escribe el nombre de archivo en el que quieras guardar los datos(con extensión): ")
		try:
			archivo = str(archivo)
			return archivo
		except ValueError:
			print "ATENCIÓN: Debe ingresar un archivo."


def limpia_texto(text):
	'''Esta ón pone todo el texto en minúscula y elimina los caracteres extraños: ',', ')' ...'''

	texto = text
	texto = texto.lower()	# Convierte todo el texto a minúscula
	
	lista_caracteres = [',', '(', ')', '¡', '!', '¿', '?', '\'', '#', '$', '\%', '&', '*', '+', '-', '\\', '_', ':', ';', '<', '>', '=', '@', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '/', '[', ']', '^', '{', '}', '|', '~', '\n', '“', '”', '―', '…', '─']	# Lista de los caracteres que queremos eliminar

	for caracter in lista_caracteres:
		texto = texto.replace(caracter, "")
	return texto


def por_frases(text):
	'''Divide un texto en cada una de sus frases usando como punto de separación el '.' '''

	texto = text
	frases = texto.split(".")
	return frases


def por_palabras(lista_frases):
	'''Esta ón limpia los espacios inicial y final de una lista de frases y después separa las palabras'''

	frases = lista_frases

	i = 0
	for frase in frases:
		frases[i] = frases[i].strip()		# Limpia los espacios iniciales y finales de cada frase
		frases[i] = frases[i].split(' ')	# Separa las palabras según los espacios
		i += 1

	return frases


def crea_dict(lista_palabras):
	'''Genera un diccionario con palabras como claves y la cantidad de veces que se repiten como valores'''

	lista = lista_palabras

	diccionario = dict()

	for frase in lista:
		for palabra in frase:
			if diccionario.has_key(palabra) == True:
				valor = diccionario[palabra]
				valor += 1
				diccionario[palabra] = valor
			else:
				diccionario.setdefault(palabra, 1)
	diccionario.pop('',None)	# Eliminamos los espacios del diccionario
	return diccionario


def muestra_valores(diccionario):
	'''Muesta las palabras y cuantas veces se repiten'''

	for palabra,veces in diccionario.items():
		print ' \'%s\' se encuentra %s veces' %(palabra,veces)


def escribe_lista(diccionario, archivo):
	'''Escribe los resultados en un archivo de texto, ordenándolos previamente de mayor a menor'''

	lista = diccionario.items()
	lista.sort(key=lambda x: x[1], reverse = True)

	input_filename = open(archivo, "w")
	for par in lista:
		linea = '%s;%s\n' %(par[0], par[1])
		input_filename.write(linea)
	input_filename.close()
	return lista


def full_program():
	'''Ejecuta el programa completo'''

	archivo_entrada = validar_entrada()

	para_analizar = open(archivo_entrada, 'r')
	texto_sin_limpiar = para_analizar.read()
	
	texto_limpio = limpia_texto(texto_sin_limpiar)	# Limpio el texto de caracteres especiales y lo dejo todo en minúscula

	frases = por_frases(texto_limpio)	# Separa el texto en sus frases

	palabras = por_palabras(frases)	# Separa las frases en palabras

	diccionario = crea_dict(palabras)	# Crea como claves las palabras y como valores las veces que están repetidas en el texto
	
	archivo_salida = validar_salida()	# Graba los valores en un archivo introducido por el usuario'

	lista_ordenada = escribe_lista(diccionario, archivo_salida)

	para_analizar.close()	# Cierra el archivo abierto

	print '\nArchivo guardado con éxito'	# Imprime un mensaje de éxito
