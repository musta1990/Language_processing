#python2 HandleDIR_parseSimpleText.py /home/mustafa/Documentos/Python/Crawler0.1/Mexico/

import sys, os
#import parseSimpleText

PatronTT="http://twitter.com/search?q="
PatronTime="align=\"right\">"
ExtencionSalida=".TT.csv"
ExtencionEntrada=".html"

def escribir_TT(VOC,namefile):
  namefile=namefile.replace(ExtencionEntrada,ExtencionSalida)
  file_voc=open(namefile,"w")
  file_voc.write("SIZE:,"+str(len(VOC))+"\n")
  file_voc.write("TrendingTopic\tTime\tCategory"+"\n")
  for par in VOC:
	#file_voc.write(vocablo+"\t"+str(VOC[vocablo])+"\n")
	file_voc.write(par[0]+"\t"+par[1]+"\n")
#	print par[0]+"\t"+par[1]+"\n"
  file_voc.close()    

def extraer_TT(namearchivoorigen):
	print "\n<process funcion= \"Se extrae los trending topics y su duracion del html de  http://www.trendinalia.com/\"/>\n"
	lista_TT=list()

	  
	archivoorigen=open(namearchivoorigen,"r")
	#archivosalida=open(sys.argv[2],"w")

	text=archivoorigen.read()
	archivoorigen.close()

	puntero=0
	punteroTTfin=0
	punteroTimepoinicio=0
	punteroTimepofin=0

	while puntero >= 0:
		puntero = text.find(PatronTT, puntero)
		punteroTTfin = text.find("\"", puntero)
		punteroTimepoinicio = text.find(PatronTime, puntero)
		punteroTimepofin = text.find("<", punteroTimepoinicio+len(PatronTime))
		
		
		if puntero >= 0:
			#print text[puntero+len(PatronTT):punteroTTfin],"time",text[punteroTimepoinicio+len(PatronTime):punteroTimepofin]
			TTtext=text[puntero+len(PatronTT):punteroTTfin].replace("%23","#")
			TTtime=text[punteroTimepoinicio+len(PatronTime):punteroTimepofin]
			TT=[TTtext,TTtime]
			#print "##", TT
			lista_TT.append(TT)
			puntero+=len(PatronTT)
		

	escribir_TT(lista_TT,namearchivoorigen)

	print "</process general estodo=\"correcto\" Numero de trendingTopics extraidos = ",len(lista_TT)," >"  





#inicio de funcion main
print "\n<process funcion= \"Dado un directorio se extrean todos lo trending topics de todos los archivos html \"/>"

if(len(sys.argv) < 2):
  print "\nError: No se declaro archivo de entrada.\n" 
  print "</process estodo=\"Error\">"
  exit()
else:
  print "Directorio con los Html de Trendalia: ",sys.argv[1],"\n"
#  print "File de matriz del Word2Vec: ",sys.argv[3],
#print "escritura de documentos subcorpus",sys.argv[3]


dir = sys.argv[1]
separador=""
if dir[0:5].find("/")>0:
	separador="/"


files = os.listdir(dir)
for file in files:
	if file.find(ExtencionEntrada)>0:
		print "#> Generando:",file
		dir+separador+file
		extraer_TT(dir+separador+file)


		
