#!/usr/bin/python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import fileinput
import glob, os, string, unicodedata
import re

#count=0
for arch_htm in glob.glob("/home/mustafa/Documentos/Python/Discurosos_PoliticaHistorica/*.htm"):
	soup = BeautifulSoup(open(arch_htm),"html.parser")
	soup.prettify()

	#disInt_estructText = open("/home/mustafa/Documentos/Python/Discursos_integros/disInt_estruct.txt","w")
	#disInt_cognitvText = open("/home/mustafa/Documentos/Python/Discursos_integros/disInt_cognitv.txt","w")
	
	disInt_tag_id = soup.find_all(id='tab4')
	for tag1 in disInt_tag_id:
		disInt_tag_div = tag1.find_all('div','field-item')
		for tag2 in disInt_tag_div:
			str_tag2 = str(tag2)
			tag2_re = re.sub("\n"," ",str_tag2)
			#~ tag2_re = re.sub('<div class="field-item"><div style="font-family: \'Myriad Pro\'; font-size: 17px; line-height: 25.5px;"><div><span style="font-size: medium;"><img alt="" height="1001" src="Acta%20de%20Independencia%20de%20M%C3%A9xico,%201821%20_%20Adqat%20Archivos/ActaIndependencia.jpg" width="700"/></span></div><div><span style="font-size: medium;">',"",tag2_re)
			#tag2_re = re.sub("</span>","\n",tag2_re)
			#~ tag2_re = re.sub('</div><div><span style="font-size: medium;">',"",tag2_re)
			#~ tag2_re = re.sub('</div></div><div style="font-family: \'Myriad Pro\'; font-size: 17px; line-height: 25.5px;"><span style="font-size: medium;">',"",tag2_re)
			#~ tag2_re = re.sub('</div><div style="font-family: \'Myriad Pro\'; font-size: 17px; line-height: 25.5px;"><span style="font-size: medium;">',"",tag2_re)
			#~ tag2_re = re.sub('</div><div style="font-family: \'Myriad Pro\'; font-size: 17px; line-height: 25.5px;"><span style="font-size: medium;">',"",tag2_re)
			#~ tag2_re = re.sub('</div><div><div>',"",tag2_re)
			#~ tag2_re = re.sub('<span style="font-size: medium;"><span style="font-family: \'Myriad Pro\'; font-size: medium;"><span style="line-height: 25.5px;">',"",tag2_re)
			#~ tag2_re = re.sub('<span style="font-family: \'Myriad Pro\'; font-size: medium;"><span style="line-height: 25.5px;">',"",tag2_re)
			tag2_re = re.sub("<(/p|/span|/div|br)>","\n",tag2_re)
			tag2_re = re.sub("<[^>]+>","",tag2_re)
			tag2_re = re.sub("\n(\s*\n)*","\n\n",tag2_re)
			#tag2_re = re.sub("[^a-zA-Z]","",tag2_re)
			#~ tag2_re = re.sub("</div></div>","",tag2_re)
			print(tag2_re)
			#~ disInt = tag2.text
			#~ print(disInt)
			titulo = soup.title.text
			titulo = ''.join(filter(str.isalpha, titulo))
			titulo = titulo.replace("á", "a")
			titulo = titulo.replace("é", "e")
			titulo = titulo.replace("í", "i")
			titulo = titulo.replace("ó", "o")
			titulo = titulo.replace("ú", "u")
			titulo = titulo.replace("ñ", "n")
			titulo = titulo.replace("Á", "A")
			titulo = titulo.replace("°", "")
			#titulo = ''.join((c for c in unicodedata.normalize('NFD',unicode(titulo)) if unicodedata.category(c) != 'Mn'))
			print(titulo)
				
	#count=count+1
	disInt_estructText = open("/home/mustafa/Documentos/Python/Discurosos_PoliticaHistorica_[Discursos_integros]/"+titulo+"Estructural.ann","w")
	#disInt_estructText.write(tag2_re)
	#disInt_estruct"+str(count)+".txt","w")
	disInt_cognitivText = open("/home/mustafa/Documentos/Python/Discurosos_PoliticaHistorica_[Discursos_integros]/"+titulo+"Cognitivo.ann","w")
	#disInt_cognitivText.write(tag2_re)

	disInt_estructText.close()
	disInt_cognitivText.close()
