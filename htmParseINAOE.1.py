#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
1. Abrir archivos htm
2. Buscar los tags relevantes (parsing)
3. Enviarlos a un archivo csv
"""
from bs4 import BeautifulSoup
import csv
import fileinput
import glob, os, string

# 1. Abre archivo csv e inicializa los textos de cabecera
with open('archivo.csv', 'w') as csvfile:
	writer = csv.writer(csvfile, delimiter=",")
	writer.writerow([
		'Título',
		'Promedio',
		'Introducción',
		'Argumento principal',
		'Valor',
		'Lógica de argumentación',
		'Valor',
		'Tono emocional',
		'Valor',
		'Soportes de la argumentación',
		'Valor',
		'Cierre',
		'Valor',
		'Discurso íntegro'])
		
	# 2. Abre todos los archivos htm
	for arch_htm in glob.glob('/home/mustafa/Documentos/Python/P_disc/*.htm'):
		soup = BeautifulSoup(open(arch_htm), "html.parser")
		soup.prettify()
		# 3. Análisis sintáctico
		title_tags = soup.title.string # Título
		promedio_tags = soup.find_all("div", id="promedio") # Promedio
		intro_tags = soup.find_all("div", id="introd") # Introducción
		argprin_tags = soup.find_all("div", id="argprin_tag") # Argumento Principal
		argprin_val_tags = soup.find_all("div", id="argprin_tag_val") # Valor de Argumento Principal
		
		# Acceder al arbol
		logarg_tags = soup.find_all("div", "logicaa-d") # Lógica de Argumentación
		for tags in logarg_tags:
			logarg_val = tags.find_all("div", "field-item")
			
#		tonoemo_tags = soup.find()
#		soparg_tags = soup.find()
#		cierre_tags = soup.find()
		discourse_tags = soup.find_all("div", id="disc_integro")
		
		# Promedio
		promedio = ""
		bandera0 = 0
		prom_str = str(promedio_tags)
		
		for i in range(len(prom_str)):
			if prom_str[i] == "<":
				bandera0 = 1
			
			if bandera0 == 0:
				promedio += prom_str[i]
			
			if prom_str[i] == ">":
				bandera0 = 0
				promedio += "\n"
		
		# Intro
		intro = ""
		bandera1 = 0
		intro_str = str(intro_tags)
		
		for i in range(len(intro_str)):
			if intro_str[i] == "<":
				bandera1 = 1
			
			if bandera1 == 0:
				intro += intro_str[i]
			
			if intro_str[i] == ">":
				bandera1 = 0
				intro += "\n"
		
		# Argumento principal
		arg_prin = ""
		bandera2 = 0
		argprin_str = str(argprin_tags)
		
		for i in range(len(argprin_str)):
			if argprin_str[i] == "<":
				bandera2 = 1
			
			if bandera2 == 0:
				arg_prin += argprin_str[i]
			
			if argprin_str[i] == ">":
				bandera2 = 0
				arg_prin += "\n"
		
		# Argumento principal, valor
		argprin_val = ""
		bandera3 = 0
		argprin_val_str = str(argprin_val_tags)
		
		for i in range(len(argprin_val_str)):
			if argprin_val_str[i] == "<":
				bandera3 = 1
			
			if bandera3 == 0:
				argprin_val += argprin_val_str[i]
			
			if argprin_val_str[i] == ">":
				bandera3 = 0
				argprin_val += "\n"
		
		# Discurso íntegro
		discurso = ""
		bandera = 0
		discurso_str = str(discourse_tags)
		
		for i in range(len(discurso_str)):
			if discurso_str[i] == "<":
				bandera = 1
			
			if bandera == 0:
				discurso += discurso_str[i]
			
			if discurso_str[i] == ">":
				bandera = 0
				discurso += "\n"
		
		writer.writerow([
			title_tags,
			promedio,
			intro,
			arg_prin,
			argprin_val,
			discurso])
