#!/usr/bin/python
# -*- coding: utf-8 -*-

# Librería para análisis gramatical
# y conversión a archivo separado por coma (csv)
from HTMLParser import HTMLParser
import csv

# Objeto analizador
class MyHTMLParser(HTMLParser):
	def handle_starttag(self, tag, attrs):
		""" Reconoce todos los tags de inicio,
		e.g. <head> <title>, <h1>, etc. """
	