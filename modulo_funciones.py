#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# Hoja de funciones creadas para este proyecto
#

#
# Rubén Martín Moreno
#

def limpia_texto(text):
	'''Esta función pone todo el texto en minúscula y elimina los caracteres extraños: ',', ')' ...'''

	texto = text
	texto = texto.lower()	# Convierte todo el texto a minúscula
	
	lista_caracteres = [',', '(', ')', '¡', '!', '¿', '?', '\'', '#', '$', '\%', '&', '*', '+', '-', '\\', '_', ':', ';', '<', '>', '=', '@', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '/', '[', ']', '^', '{', '}', '|', '~', '\n', '“', '”', '―']	# Lista de los caracteres que queremos eliminar

	for caracter in lista_caracteres:
		texto = texto.replace(caracter, "")
	return texto

def por_frases(text):
	'''Divide un texto en cada una de sus frases usando como punto de separación el '.' '''

	texto = text
	frases = texto.split(".")
	return frases


def por_palabras(lista_frases):
	'''Esta función limpia los espacios inicial y final de una lista de frases y después separa las palabras'''

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