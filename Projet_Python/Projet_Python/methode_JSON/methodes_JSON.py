#Mettre ici les méthodes de lecture/écriture JSON
# Python program to update 
# JSON 

from datetime import datetime
import json 
from datetime import date


# function to add to JSON 
def write_json(data, filename):
	with open(filename,'w') as f:
		json.dump(data, f, indent=4)
	return


def EnregistrerClient(data):
	with open('./JSON/infos_client.json') as json_file:
		fichier = json.load(json_file)
		temp = fichier['foyers']
		data['Personnes']=[]
		today = date.today()
		data['Date']=today.strftime("%Y-%m-%d")
		temp.append(data)
	write_json(fichier,'./JSON/infos_client.json')
	return


def EnregistrerPersonnes(data):
	with open('./JSON/infos_client.json') as json_file:
		fichier = json.load(json_file)
		temp = fichier['foyers']
		temp[len(temp)-1]['Personnes'].append(data)
	write_json(fichier,'./JSON/infos_client.json')
	return


### Méthode ajoutant la commande passée par un client à la BDD des commandes effectuées ###
def EnregistrerCommande(data, id):
	#récupération CP de la personne ayant commandé (utile pour la partie admin)
	CP=""
	with open('./JSON/infos_client.json') as json_file:
		fichier = json.load(json_file)
		temp = fichier['foyers']
		for element in temp:
			if (element["id_box"]==id): CP = element["codeP"]
  
	with open('./JSON/commandes_faites.json') as json_file:
		fichier = json.load(json_file)
		temp = fichier['commandes']
		datacleaned={}
		for k,v in data.items():
			if (v != '0'):
				datacleaned[k]=v
		datacleaned['id']=id
		datacleaned['CP']=CP
		datacleaned['Date'] = (datetime.now()).strftime("%Y-%m-%d") #Ajout de la date au format YYYY-mm-dd 
		
		temp.append(datacleaned)
	write_json(fichier,'./JSON/commandes_faites.json')
	return


### Méthode vérifiant si l'Id et le password entrés par le client sont dans la base de données clients ###
def VerifClient(id,pwd):
	with open('./JSON/infos_client.json') as json_file:
		fichier = json.load(json_file)
		temp=fichier['foyers']
		check = False
		for element in temp:
			if(element['id_box']==id and element['pwd']==pwd): 
				check=True
				break
	return check


### Méthode vérifiant si l'Id et le password entrés par l'admin sont dans la base de données admin ###
def VerifAdmin(id,pwd):
	with open('./JSON/admin_login.json') as json_file:
		fichier = json.load(json_file)
		temp=fichier['admin']
		check = False
		for element in temp:
			if(element['id']==id and element['pwd']==pwd): check=True
	return check