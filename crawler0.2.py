#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib.request

def spider(maximoDePaginas):
	pagina = 1
	while pagina < maximoDePaginas:
		# 1 marzo al 9 junio
		# 160301 hasta 160609
		mi_url = "http://www.trendinalia.com/twitter-trending-topics/mexico/mexico-160301.html"
		codigo_fuente = urllib.request.urlopen(mi_url)
		hipertexto = codigo_fuente.text
