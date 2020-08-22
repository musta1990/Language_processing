#!/usr/bin/python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import csv
import fileinput
import glob, os, string
import re

with open('Discursos_pol_Otro.csv', 'w') as csvfile:
	writer = csv.writer(csvfile, delimiter=",")
	writer.writerow([
		'Título',
		'Promedio',
		'Argumento principal', # Conclusiones Estructurales
		'Argumento principal [Valor]',
		'Lógica de argumentación',
		'Lógica de argumentación [Valor]',
		'Tono emocional',
		'Tono emocional [Valor]',
		'Soportes de la argumentación',
		'Soportes de la argumentación [Valor]',
		'Cierre',
		'Cierre [Valor]',
		'Hechos y datos',
		'Hechos y datos [Valor]', # Caracterización del Patrón Cognitivo del Pensamiento
		'Con fuente',
		'Sin fuente',
		'Cita a terceros',
		'Percepciones',
		'Percepciones [Valor]',
		'Opinión',
		'Referencia a terceros',
		'Provocación',
		'Comparación',
		'Duda/pregunta',
		'Juicio de valor positivo',
		'Juicio de valor negativo',
		'Autorevelación',
		'Idea épica',
		'Declaración de principios',
		'Escenarios negativos',
		'Escenarios negativos [Valor]',
		'Amenazas',
		'Debilidades',
		'Escenarios positivos',
		'Escenarios positivos [Valor]',
		'Ventajas',
		'Oportunidades',
		'Fortalezas',
		'Propuestas',
		'Propuestas [Valor]',
		'Propuesta completa',
		'Sólo estrategia',
		'Sólo objetivos',
		'Idea genérica',
		'Sólo acción',
		'Sólo responsables',
		'Cápsula y opinión',
		'Discurso íntegro'])
	
	for arch_htm in glob.glob('/home/mustafa/Documentos/Python/Discursos_pol_Otro/*.htm'):
		soup = BeautifulSoup(open(arch_htm), "html.parser")
		soup.prettify()
		# Título
		titulo_tag = soup.find_all('h1','title')
		for t in titulo_tag:
			titulo = t.text.replace('\n',' ')
			#print(titulo)
		# Promedio
		promedio_tag = soup.find_all('div','promedio')
		for p in promedio_tag:
			promedio = p.text.replace('\n',' ')
			#print(promedio)
		# Argumento principal / valor
		arg_prin_tag = soup.find_all('div','argumentop-d')
		for a in arg_prin_tag:
			arg_prin_tag2 = a.find_all('div','txt-d')
			for a2 in arg_prin_tag2:
				arg_prin = a2.text.replace('\n',' ')
				#print(arg_prin)
		for a_v in arg_prin_tag:
			arg_prin_val_tag = a_v.find_all('div','field-item')
			for a_v2 in arg_prin_val_tag:
				arg_prin_val = a_v2.text.replace('\n',' ')
				#print(arg_prin_val)
		# Logica argumentativa / valor
		log_arg_tag = soup.find_all('div','logicaa-d')
		for lo in log_arg_tag:
			log_arg_tag2 = lo.find_all('div','txt-d')
			for lo2 in log_arg_tag2:
				log_arg = lo2.text.replace('\n',' ')
				#print(log_arg)
		for lo_v in log_arg_tag:
			log_arg_val_tag = lo_v.find_all('div','field-item')
			for lo_v2 in log_arg_val_tag:
				log_arg_val = lo_v2.text.replace('\n',' ')
				#print(log_arg_val)
		# Tono emocional / valor
		tono_emo_tag = soup.find_all('div','tonoe-d')
		for to in tono_emo_tag:
			tono_emo_tag2 = to.find_all('div','txt-d')
			for to2 in tono_emo_tag2:
				tono_emo = to2.text.replace('\n',' ')
				#print(tono_emo)
		for to_v in tono_emo_tag:
			tono_emo_val_tag = to_v.find_all('div','field-item')
			for to_v2 in tono_emo_val_tag:
				tono_emo_val = to_v2.text.replace('\n',' ')
				#print(tono_emo_val)
		# Soportes de la argumentación / valor
		contenido_tag = soup.find_all('div','contetodo')
		for con in contenido_tag:
			sopo_arg_tag = con.find_all('div','soportesa-d')
			for so in sopo_arg_tag:
				sopo_arg_tag2 = so.find_all('div','txt-d')
				for so2 in sopo_arg_tag2:
					sopo_arg = so2.text.replace('\n',' ')
					#print(sopo_arg)
			for so_v in sopo_arg_tag:
				sopo_arg_val_tag = so_v.find_all('div','field-item')
				for so_v2 in sopo_arg_val_tag:
					sopo_arg_val = so_v2.text.replace('\n',' ')
					#print(tono_emo_val)
		# Cierre / valor
		cierre_tag = soup.find_all('div','cierre-d')
		for ci in cierre_tag:
			cierre_tag2 = ci.find_all('div','txt-d')
			for ci2 in cierre_tag2:
				cierre = ci2.text.replace('\n',' ')
				#print(sopo_arg)
			for ci_v in cierre_tag:
				cierre_val_tag = ci_v.find_all('div','field-item')
				for ci_v2 in cierre_val_tag:
					cierre_val = ci_v2.text.replace('\n',' ')
					#print(tono_emo_val)
		# Hechos y datos / valor
		contenido2_tag = soup.find_all(id='comprb1')
		for con2 in contenido2_tag:
			hech_dat_tag = con2.find_all('div','txt-d')
			for he in hech_dat_tag:
				hech_dat = he.text.replace('\n',' ')
			hech_dat_val_tag = con2.find_all('div','field-item')
			for he2 in hech_dat_val_tag:
				hech_dat_val = he2.text.replace('\n',' ')
			# Con fuente / Sin fuente / Cita a terceros
			sub_contenido_tag = soup.find_all('div','lngrp2')
			for sub in sub_contenido_tag:
				sub2_contenido_tag = sub.find_all('div','g2titulo')
				for sub2 in sub2_contenido_tag:
					if 'Con fuente' in sub2.get_text():
						con_fuente_temp = sub2.find_next('div','valorg2')
						con_fuente = con_fuente_temp.text.replace('\n',' ')
						#print(con_fuente)
					elif 'Sin fuente' in sub2.get_text():
						sin_fuente_temp = sub2.find_next('div','valorg2')
						sin_fuente = sin_fuente_temp.text.replace('\n',' ')
						#print(sin_fuente)
					elif 'Cita a terceros' in sub2.get_text():
						cita_ter_temp = sub2.find_next('div','valorg2')
						cita_ter = cita_ter_temp.text.replace('\n',' ')
						#print(cita_ter)
		# Percepciones / valor
		contenido3_tag = soup.find_all(id='represb1')
		for con3 in contenido3_tag:
			percep_tag = con3.find_all('div','txt-d')
			for per in percep_tag:
				percep = per.text.replace('\n',' ')
			percep_val_tag = con3.find_all('div','field-item')
			for per2 in percep_val_tag:
				percep_val = per2.text.replace('\n',' ')
			# Sub datos
			sub3_contenido_tag = soup.find_all('div','lngrp2')
			for sub3 in sub3_contenido_tag:
				sub2_3_contenido_tag = sub3.find_all('div','g3titulo')
				for sub2_3 in sub2_3_contenido_tag:
					if 'Opinión' in sub2_3.get_text():
						opi_temp = sub2_3.find_next('div','valorg3')
						opi = opi_temp.text.replace('\n',' ')
						#print(opi)
					elif 'Referencia a terceros' in sub2_3.get_text():
						ref_ter_temp = sub2_3.find_next('div','valorg3')
						ref_ter = ref_ter_temp.text.replace('\n',' ')
						#print(ref_ter)
					elif 'Provocación' in sub2_3.get_text():
						provo_temp = sub2_3.find_next('div','valorg3')
						provo = provo_temp.text.replace('\n',' ')
						#print(provo)
					elif 'Comparación' in sub2_3.get_text():
						compa_temp = sub2_3.find_next('div','valorg3')
						compa = compa_temp.text.replace('\n',' ')
						#print(compa)
					elif 'Duda/pregunta' in sub2_3.get_text():
						duda_preg_temp = sub2_3.find_next('div','valorg3')
						duda_preg = duda_preg_temp.text.replace('\n',' ')
						#print(duda_preg)
					elif 'Juicio de valor positivo' in sub2_3.get_text():
						jui_val_positivo_temp = sub2_3.find_next('div','valorg3')
						jui_val_positivo = jui_val_positivo_temp.text.replace('\n',' ')
						#print(jui_val_positivo)
					elif 'Juicio de valor negativo' in sub2_3.get_text():
						jui_val_negativo_temp = sub2_3.find_next('div','valorg3')
						jui_val_negativo = jui_val_negativo_temp.text.replace('\n',' ')
						#print(jui_val_negativo)
					elif 'Autorevelación' in sub2_3.get_text():
						autore_temp = sub2_3.find_next('div','valorg3')
						autore = autore_temp.text.replace('\n',' ')
						#print(autore)
					elif 'Idea épica' in sub2_3.get_text():
						idea_ep_temp = sub2_3.find_next('div','valorg3')
						idea_ep = idea_ep_temp.text.replace('\n',' ')
						#print(idea_ep)
					elif 'Declaración de principios' in sub2_3.get_text():
						dec_prin_temp = sub2_3.find_next('div','valorg3')
						dec_prin = dec_prin_temp.text.replace('\n',' ')
						#print(dec_prin)
		# Escenarios negativos
		contenido4_tag = soup.find_all(id='enfoqb1')
		for con4 in contenido4_tag:
			esc_nega_tag = con4.find_all('div','txt-d')
			for esc in esc_nega_tag:
				esc_nega = esc.text.replace('\n',' ')
			esc_nega_val_tag = con4.find_all('div','field-item')
			for esc2 in esc_nega_val_tag:
				esc_nega_val = esc2.text.replace('\n',' ')
			# Amenazas /  debilidades
			sub4_contenido_tag = soup.find_all('div','lngrp2')
			for sub4 in sub4_contenido_tag:
				sub2_4_contenido_tag = sub4.find_all('div','g4titulo')
				for sub2_4 in sub2_4_contenido_tag:
					if 'Amenazas' in sub2_4.get_text():
						amena_temp = sub2_4.find_next('div','valorg4')
						amena = amena_temp.text.replace('\n',' ')
						#print(amena)
					elif 'Debilidades' in sub2_4.get_text():
						debi_temp = sub2_4.find_next('div','valorg4')
						debi = debi_temp.text.replace('\n',' ')
						#print(debi)
		# Escenarios positivos
		contenido5_tag = soup.find_all(id='soporb1')
		for con5 in contenido5_tag:
			esc_posi_tag = con5.find_all('div','txt-d')
			for posi in esc_posi_tag:
				esc_posi = posi.text.replace('\n',' ')
			esc_posi_val_tag = con5.find_all('div','field-item')
			for posi_val in esc_posi_val_tag:
				esc_posi_val = posi_val.text.replace('\n',' ')
			# Ventajas / oportunidades / fortalezas
			sub5_contenido_tag = soup.find_all('div','lngrp2')
			for sub5 in sub5_contenido_tag:
				sub2_5_contenido_tag = sub5.find_all('div','g5titulo')
				for sub2_5 in sub2_5_contenido_tag:
					if 'Ventajas' in sub2_5.get_text():
						venta_temp = sub2_5.find_next('div','valorg5')
						venta = venta_temp.text.replace('\n',' ')
						#print(venta)
					elif 'Oportunidades' in sub2_5.get_text():
						opor_temp = sub2_5.find_next('div','valorg5')
						opor = opor_temp.text.replace('\n',' ')
						#print(opor)
					elif 'Fortalezas' in  sub2_5.get_text():
						forta_temp = sub2_5.find_next('div','valorg5')
						forta = forta_temp.text.replace('\n',' ')
						#print(forta)
		# Propuesta / valor
		contenido6_tag = soup.find_all(id='propusb1')
		for con6 in contenido6_tag:
			propu_tag = con6.find_all('div','txt-d')
			for pro in propu_tag:
				propu = pro.text.replace('\n',' ')
			propu_val_tag = con6.find_all('div','field-item')
			for pro_val in propu_val_tag:
				propu_val = pro_val.text.replace('\n',' ')
			# Propuesta completa / Sólo estrategia / Sólo objetivos ...
			sub6_contenido_tag = soup.find_all('div','lngrp2')
			for sub6 in sub6_contenido_tag:
				sub2_6_contenido_tag = sub6.find_all('div','g6titulo')
				for sub2_6 in sub2_6_contenido_tag:
					if 'Propuesta completa' in sub2_6.get_text():
						propu_comp_temp = sub2_6.find_next('div','valorg6')
						propu_comp = propu_comp_temp.text.replace('\n',' ')
						#print(propu_comp)
					elif 'Sólo estrategia' in sub2_6.get_text():
						solo_estra_temp = sub2_6.find_next('div','valorg6')
						solo_estra = solo_estra_temp.text.replace('\n',' ')
						#print(solo_estra)
					elif 'Sólo objetivos' in  sub2_6.get_text():
						solo_obj_temp = sub2_6.find_next('div','valorg6')
						solo_obj = solo_obj_temp.text.replace('\n',' ')
						#print(solo_obj)
					elif 'Idea genérica' in sub2_6.get_text():
						idea_gene_temp = sub2_6.find_next('div','valorg6')
						idea_gene = idea_ep_temp.text.replace('\n',' ')
						#print(idea_gene)
					elif 'Sólo acción' in sub2_6.get_text():
						solo_acc_temp = sub2_6.find_next('div','valorg6')
						solo_acc = solo_acc_temp.text.replace('\n',' ')
						#print(solo_acc)
					elif 'Sólo responsables' in sub2_6.get_text():
						solo_repo_temp = sub2_6.find_next('div','valorg6')
						solo_repo = solo_repo_temp.text.replace('\n',' ')
						#print(solo_repo)
		# Cápsula y opinión
		contenido7_tag = soup.find_all(id='tab3')
		for con7 in contenido7_tag:
			capsu_op_tags = con7.find_all('div','field-item')
			capsu_op = capsu_op_tags[0]
			capsu_op = capsu_op.text.replace("\n"," ")
			#print("1"+str(capsu_op_tags)+"1")
			#for cap in capsu_op_tag:
			#	capsu_op = cap.text.replace('\n',' ')
			#	print(capsu_op)
		# Discurso íntegro
		contenido8_tag = soup.find_all(id='tab4')
		for con8 in contenido8_tag:
			disc_inte_tag = con8.find_all('div','field-item')
			for disc in disc_inte_tag:
				str_disc = str(disc)
				#~ print(str_disc)
				#~ str_disc = disc.text.replace("\n"," ")
				line = re.sub("\n", " ", str_disc)
				line = re.sub("<(/p|/span|/div|br)>","\n",line)
				line = re.sub("<[^>]+>","",line)
				line = re.sub("\n(\s*\n)*","\n\n",line)
				#~ line = re.sub("<div*>", "", line)
				#~ line = re.sub("</div>", "\n", line)
				#~ line = re.sub("</p>", "\n\n", line)
				#~ line = re.sub("<p>&nbsp;", "", line)
				#~ line = re.sub("<br>", "", line)
				#~ line = re.sub("<div>", "", line)
				#~ line = re.sub('<div style="text-align: justify;">', "", line)
				#~ line = re.sub("<span>", "", line)
				#~ line = re.sub("<\span>", "", line)
				#~ line = re.sub("<p>", "", line)
				#~ line = re.sub("<a>", "", line)
				#~ line = re.sub("<.*>" , "" , line)
				print(line)
				#~ line = re.sub("</.*>" , "\n" , str_disc)
				#~ line = re.sub("<.*>" , "\n" , line)
				#~ line = re.sub("(\n)+" , "\n" , line)
				#~ line = re.sub("<br>", "\n", line)
				#~ line = "temp"
				#~ print(line)
				
		#~ print("AQUI DEBE IR LA INFO:")
		#~ print("|" + capsu_op + "|")
		writer.writerow([
			titulo,
			promedio,
			arg_prin,
			arg_prin_val,
			log_arg,
			log_arg_val,
			tono_emo,
			tono_emo_val,
			sopo_arg,
			sopo_arg_val,
			cierre,
			cierre_val,
			hech_dat,
			hech_dat_val,
			con_fuente,
			sin_fuente,
			cita_ter,
			percep,
			percep_val,
			opi,
			ref_ter,
			provo,
			compa,
			duda_preg,
			jui_val_positivo,
			jui_val_negativo,
			autore,
			idea_ep,
			dec_prin,
			esc_nega,
			esc_nega_val,
			amena,
			debi,
			esc_posi,
			esc_posi_val,
			venta,
			opor,
			forta,
			propu,
			propu_val,
			propu_comp,
			solo_estra,
			solo_obj,
			idea_gene,
			solo_acc,
			solo_repo,
			capsu_op,
			line
			])
