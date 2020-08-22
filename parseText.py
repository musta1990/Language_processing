#!/usr/bin/python
# -*- coding: utf-8 -*-

#~ 1. Definir la clase htmlParseText
	#~ 2. definir funcion "extracción de texto"
	#~ 3. llamar al objeto(clase) HtmlParseText
from html.parser import HTMLParser

class HtmlParseText(HTMLParser):
	def __init__(self):
		HtmlParser.__init__(self)
		self.bandera = 0
		self.data = []
	
	def handle_starttag(self, tag, attrs):
		"""Manipula los tags iniciales"""
		if tag == '<a>':
			for nombre, valor in attrs:
				if nombre == 'href' and valor == 'http://twitter.com/search?q=':
					self.bandera = 1
					
	def handle_endtag(self, tag):
		"""Manipula los tags finales"""
		if tag = '</a>':
			self.bandera -= 1
			
	def handle_data(self, data):
		"""Manipula la información de los tags
		Extrae información de Trending Topics
		y duración"""
		if self.bandera:
			self.data.append(data)
