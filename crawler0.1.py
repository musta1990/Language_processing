#!/usr/bin/python
# -*- coding: utf-8 -*-

#~ 1. Crear el archivo csv vacío
#~ 2. Entrar en la página 
#~ http://www.trendinalia.com/twitter-trending-topics/globales/globales-16...
#~ y buscar las fechas
#~ 3. Por cada fecha extraer el Trending Topic y su duración
#~ 4. Escribir en el archivo csv y cerrarlo

#~ import csv
import urllib.request
import time
#~ from parseText import HtmlParseText
from datetime import date

#~ with open('trending_topics.csv', 'w') as arch_csv:
	#~ escribir = csv.writer(arch_csv, delimiter=",")
	#~ escribir.writerow(['Trending Topic','Duración'])
	
def obtener_sitio_html(mi_url):
	"""Descarga los sitios html"""
	sitio_fuente = urllib.request.urlopen(mi_url)
	html = sitio_fuente.read()
	return html

#~ def extraccion_alternativa():
	#~ """Descarga los sitios html que se quedaron atrás. 
	#~ Esta función debería estar comentada. Solo usarla 
	#~ en caso de archivos html atrasados"""
	#~ i=1
	#~ for i in range(14, 31):
		#~ mi_url = "http://www.trendinalia.com/twitter-trending-topics/mexico/puebla-1606"+str(i)+".html"
		#~ archivo_html = open('trendinalia_1606'+str(i)+'.html','w')
		#~ archivo_html.write(str(obtener_sitio_html(mi_url)))
		#~ time.sleep(0.8)
	
def main():
	for mes in range(4,7):
		if (mes==1) or (mes==3) or (mes==5) or (mes==7) or (mes==8) or (mes==10) or (mes==12):
			for dia in range(1,32):
				fecha = date(2016, mes , dia)
				mi_url = "http://www.trendinalia.com/twitter-trending-topics/mexico/tijuana-"+str(fecha.strftime("%y%m%d"))+".html"
				time.sleep(0.8)
				archivo_html = open('trendinalia_'+str(fecha.strftime("%y%m%d"))+'.html','w')
				archivo_html.write(str(obtener_sitio_html(mi_url)))
				print(mi_url)
		elif mes == 2:
			for dia in range(1,30):
				fecha = date(2016, mes , dia)
				mi_url = "http://www.trendinalia.com/twitter-trending-topics/mexico/tijuana-"+str(fecha.strftime("%y%m%d"))+".html"
				time.sleep(0.8)
				archivo_html = open('trendinalia_'+str(fecha.strftime("%y%m%d"))+'.html','w')
				archivo_html.write(str(obtener_sitio_html(mi_url)))
				print(mi_url)
		elif (mes==4) or (mes==6) or (mes==9) or (mes==11):
			for dia in range(1,31):
				fecha = date(2016, mes , dia)
				mi_url = "http://www.trendinalia.com/twitter-trending-topics/mexico/tijuana-"+str(fecha.strftime("%y%m%d"))+".html"
				time.sleep(0.8)
				archivo_html = open('trendinalia_'+str(fecha.strftime("%y%m%d"))+'.html','w')
				archivo_html.write(str(obtener_sitio_html(mi_url)))
				print(mi_url)

main()
#~ extraccion_alternativa()
	#~ i = 0
	#~ for i in range(1,10):
		#~ fecha = date(2016, 1, 1)
		#~ mi_url = "http://www.trendinalia.com/twitter-trending-topics/mexico/mexico-16030"+str(i)+".html" # d.strftime("%y%m%d")
		#~ archivo_html = open('trendinalia_16030'+str(i)+'.html','w')
		#~ archivo_html.write(str(obtener_sitio_html(mi_url)))
		#~ time.sleep(5)

# 1 marzo al 9 junio
# 160301 hasta 160609
