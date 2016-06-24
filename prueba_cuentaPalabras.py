#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# Prueba de código para contar palabras usando un diccionario
#

#
# Rubén Martín Moreno
#


def crea_dict(lista_palabras):
	'''Esta función genera un diccionario con palabras como claves y la cantidad de veces que se repiten como valores'''
	lista = lista_palabras

	diccionario = dict()

	for palabra in lista:
		if diccionario.has_key(palabra) == True:
			valor = diccionario[palabra]
			valor += 1
			diccionario[palabra] = valor
		else:
			diccionario.setdefault(palabra, 1)

	return diccionario

# Iniciamos un diccionario

lista = ['en', 'en', 'en', 'en', 'en', 'en', 'de', 'de', 'de', 'por']

prueba = crea_dict(lista)


# Recorrer el diccionario, imprimiendo su clave-valor
print 'En esta prueba:'
for k,v in prueba.items():
	print ' \'%s\' se encuentra %s veces' %(k,v)


#valor = diccionario['en']
#valor += 1
#diccionario['en'] = valor

#print diccionario['en']

#print diccionario.has_key('por')
#diccionario.setdefault('por', 1)
#print diccionario.has_key('por')