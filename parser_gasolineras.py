# coding=utf-8
import requests, bs4
from pygeocoder import Geocoder
from time import sleep
res = requests.get('https://www.elpreciodelagasolina.com/gasolineras/vizcaya:34287')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, "lxml")

def corrector (localizar):
	if localizar == "Avda. Ajarte, S/n (n-625 Km 382), Arrigorriaga":
		localizar = "Avda Aixarte, Arrigorriaga"
	if localizar == "Carretera Bolueta-arrigorriaga Km. 6, Basauri":
		localizar = "48970, Vizcaya"
	if localizar == "Au Ap-68, 6, Arrigorriaga":
		localizar = "Ap-68 6"
	if localizar == "Carretera N634 Km. 106,4, Etxebarri":
		localizar = "Bilbao-Galdakao Errepidea, km 106.4, 48450 Etxebarri, Bizkaia"
	if localizar == "Avenida Alto De Enekuri, 5, Bilbao":
		localizar = "Calle Gasolinera, 48950 Erandio, Vizcaya"
	if localizar == "Cr N-634, 115, Bilbao":
		localizar = "N-634, 115, 48013 Bilbao, Vizcaya"
	if localizar == "Carretera Bi-631 Bilbao-bermeo Km. 11, Bilbao":
		localizar = "Egirleta Errepidea, 20, 48015 Bilbo, Bizkaia"
	if localizar == "Cl Aperribay, 15, Usansolo":
		localizar = "Usansolo"
	if localizar == "Poligono Iru-bide (estacion De Servicio), 1, Arkotxa":
		localizar = "Iru-Bide Kalea, 13A, 48960 Galdakao, Bizkaia"
	if localizar == "Cr Bi-625, 373, Areta":
		localizar = "BI-625, 8a 48498 Arrancudiaga"
	if localizar == "Calle Munoa,, Sn, Barakaldo":
		localizar = "Kalea Munoa, 31002, Barakaldo"
	if localizar == "Carretera Bi-3704 Km. 5,5, Saturraran":
		localizar = "Lugar Barrio los Heros, 11A 48500, Bizkaia"
	if localizar == "Carretera N 637 Km. 4,4, Zamudio":
		localizar = "Txorierri Etorbidea, 19 48170 Zamudio Bizkaia"
	if localizar == "vacio, Erandio":
		localizar = "Lutxana Asua Errepidea, 34, 48950 Erandio, Bizkaia"
	if localizar == "Avenida Zumalacarregui (c.c. Eroski), S/n, Llodio":
		localizar = "Avda Zumalakarregi, S/N, 01400 Laudio, Araba"
	if localizar == "Carretera Bi-3704 Asua-loiu Km. 57, Erandio":
		localizar = "Iparraguirre Hiribidea, 108, 48940 Leioa, Bizkaia"
	if localizar == "Carretera Bi-3704 Km. 57, Erandio":
		localizar = "Iparraguirre Hiribidea, 108, 48940 Leioa, Bizkaia"
	if localizar == "Poligono Zona Comercial Aeropuerto Loiu, 9, Derio":
		localizar = "Barrio San Esteban, 13C 48160 Bizkaia"
	if localizar == "Carretera N-634 Km. 101,8, Usansolo":
		localizar = "N-634, 48960 Galdakao, Vizcaya"
	if localizar == "Cr Bi-2522, 3,8, Zubieta":
		localizar = "48410 Orozko, Vizcaya"
	if localizar == "Carretera Bilbao-santander Km. 120, Barakaldo":
		localizar = "Crta. Kareaga Kalea N-634, Km 120, 48903 Barakaldo, Bizkaia"
	if localizar == "Cr N-634   (barrio Olabarri), 99,9, Usansolo":
		localizar = "Lugar Barrio Olabarri, 4E 48960 Bizkaia"
	if localizar == "Carretera Bi-3745 Km. 9,2, Sestao":
		localizar = "Las Delicias Kalea, 4 48510 Trapagaran Bizkaia"
	if localizar == "vacio, Sestao":
		localizar = "Las Delicias Kalea, 4 48510 Trapagaran Bizkaia"
	if localizar == "Carretera N-634 Km. S/n, Sestao":
		localizar = "Marcos Grijalvo Kalea, 3, 48910 Sestao, Bizkaia"
	if localizar == "Carretera Bi-636 Km. 15,5, Sodupe":
		localizar = "Calle de Iorgi, s/n, 48830 Sodupe, Bizkaia"
	if localizar == "Cl Grupo La Paz, 1 (bi-3739 Km 4,7), Sestao":
		localizar = "La Paz Etxetaldea, 1, 48910 Sestao, Bizkaia"
	if localizar == "Carretera N-634 Km. 96,700, Galdakao":
		localizar = "Iru-Bide Kalea, 13A, 48960 Galdakao, Bizkaia"
	if localizar == "Poligono Granada, S/n, Ortuella":
		localizar = "Etorbidea Bilbao, 22V, 48530 Ortuella, Vizcaya"
	if localizar == "Cl Munguia Bi-3121, 24,2, Urduliz":
		localizar= "Mendiondo Auzoa, 47, 48610 Urduliz, Bizkaia"
	if localizar == "Cr N-240, 16, Lemoa":
		localizar = "N-240, km 16, 48330 Lemoa, Vizcaya"
	if localizar == "Carretera Bi-3102 Km. 18,000, Mungia":
		localizar = "Bermeo K., 56A, 48100 Mungia, Bizkaia"
	if localizar == "Cl Polig.ind. Balparda El Arbol , 2, Santurtzi" or localizar == "Poligono El Arbol, 1, Santurtzi":
		localizar = "El arbol kalea 17, Santurtzi"
	if localizar == "Carretera Bi-3737 Km. S/n, Santa maria de getxo":
		localizar = "Polígono Industrial Errotatxu Ind., 5, 48993 Getxo, Vizcaya"
	if localizar == "Cr N-634, 127,2, Gallarta":
		localizar = "N-634 Km 127.2, 48500 Sanfuentes, Vizcaya"
	if localizar == "Pol.ind. El Campillo, Parc. 1-2 Fase Ii, Triano":
		localizar = "Lugar Barrio, 11B, 48500 El Campillo, Bizkaia"
	if localizar == "Carretera Asua-plentzia Km. 23, Plentzia":
		localizar = "Carretera Urduliz Plencia, s/n, 48620 Isuskiza, Bizkaia"
	if localizar == "Carretera Mungia-plentzia Km. 18, Billela":
		localizar = "Plentzia bidea, 41A, 48100, Bizkaia"
	if localizar == "Carretera Bi-pl Km. 20, Sopelana":
		localizar = "Calle Loiola Ander Deuna, 74, 48600 Sopelana, Vizcaya"
	if localizar == "Crta. N-240 Bilbao - Vitoria (n-240 Km 26), Areatza":
		localizar = "Herriko Plaza, 0, 48142 Gaztelu-Elexabeitia, Bizkaia"
	if localizar == "At A-8, 131, Gallarta":
		localizar = "Herriko Plaza, 0, 48142 Gaztelu-Elexabeitia, Bizkaia"
	if localizar == "Cr A-8  Bilbao Behobia P.k. 99,7, Amorebieta-Etxano" or localizar == "Cr A-8 Bilbao-behobia ,p.k. 100, Amorebieta-Etxano" or localizar == "Cr N-634, 93, Amorebieta-Etxano":
		localizar = "Lugar Barrio Boroa, 5D, 48340, Bizkaia"
	if localizar == "Poligono Sagastikoetxe, S/n, Gorliz":
		localizar = "Artzeta Kalea, 32 48630 Gorliz Bizkaia"
	return localizar

distancia = []
compania = []
direccion = []
localidad = []
gasolina95 = []
gasolina98 = []
gasoleo = []
glp = []

f = open('a.json', 'w')

table = soup.find(class_='sortable')
for row in table.find_all('tr')[1:]:
	col = row.find_all('td')
	json = "{ \"Distancia\": \""
	column_1 = col[0].string.strip()
	distancia.append(column_1)
	json+=str(column_1)
	json+= "\",\n \"Compania\": \""
	column_2 = col[1].string.strip()
	compania.append(column_2)
	json+=str(column_2)
	json+= "\",\n \"Direccion\": \""
	if col[2].find('a').string != None:
		column_3 = col[2].find('a').string.strip()
	if col[2].find('a').string == None:
		column_3 = "vacio"
	direccion.append(column_3)
	json+=str(column_3)
	json+= "\",\n \"Localidad\": \""
	column_4 = col[3].find('a').string.strip()
	localidad.append(column_4)
	json+=str(column_4)
	json+= "\",\n \"Gasolina95\": \""
	column_5 = col[4].string.strip()
	gasolina95.append(column_5)
	json+=str(column_5.encode('utf-8')[0:5])
	json+= "\",\n \"Gasolina98\": \""
	column_6 = col[6].string.strip()
	gasolina98.append(column_6)
	json+=str(column_6.encode('utf-8')[0:5])
	json+= "\",\n \"Gasoleo\": \""
	column_7 = col[7].string.strip()
	gasoleo.append(column_7)
	json+=str(column_7.encode('utf-8')[0:5])
	json+= "\",\n \"GLP\": \""
	column_8 = col[8].string.strip()
	glp.append(column_8)
	json+=str(column_8.encode('utf-8')[0:5])
	localizar = column_3 + ", " + column_4
	localizar = corrector(localizar)
	json+= "\",\n \"Coordenadas\": \"["
	coordenadas= str(Geocoder.geocode(localizar).coordinates)[1:-1]
	json+= coordenadas
	#print column_3
	#print column_4 para añadir la localizacion
	json+= "]\"\n}\n"
	f.write(json)
	sleep(0.101)
f.close()
