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
import glob, os


#archivoCsv = csv.writer(open("archivo.csv", "w"))
#archivoCsv.writerow(["Título", "Discurso Íntegro"])
#with open('archivo.csv', 'w') as csvfile:
#	csvwriter = csv.writer(csvfile)
#	csvwriter.writerow(["Título", "Discurso Íntegro"])

#archivos_htm = glob('P_disc/*.htm')
#for line in fileinput.input(archivos_htm):
#	soup = BeautifulSoup(line, "html.parser")
#	titulos = soup.title
#	print(line)

#csvfile = csv.writer(open("archivo.csv", "w"))
#csvfile.writerow(["Título", "Discurso Íntegro"])
#os.chdir("P_disc/")


# 1. Abre archivo csv e inicializa los textos de cabecera
with open('archivo.csv', 'w') as csvfile:
	writer = csv.writer(csvfile, delimiter=",")
	writer.writerow(['Título', 'Discurso Íntegro'])
	
	#fieldnames = ['Título', 'Discurso Íntegro']
	#writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	#writer.writeheader()

	for arch_htm in glob.glob('/home/mustafa/Documentos/Python/P_disc/*.htm'):
		soup = BeautifulSoup(open(arch_htm), "html.parser")
		soup.prettify()
		title_tags = soup.title.string
		discourse_tags = soup.find_all("div", id="disc_integro")
		
		discurso = ""
		bandera = False
		
		for i in range(len(discourse_tags)):
			if discourse_tags[i] == "<":
				bandera = True
			elif discourse_tags[i] == ">":
				bandera = False
				discurso += "\n"
			
			if bandera == False:
				discurso += str(discourse_tags[i])
		#String discurso = "";
		#Boolean bandera = 0;
		#for i=0; i < discourse_tags.lenght; i++ {
			#if (discourse_tags[i] == "<") then
				#bandera = 1;
			#else (discourse_tags[i] == ">") then
				#bandera = 0;
				#discurso += "\n";
			#end if;
			
			#if (bandera == 0) then
				#discurso += discourse_tags[i];
			#end if;
		#end;
#1. quitar parrafo <p>
		writer.writerow([title_tags, discurso]) #discurso / discourse_tags