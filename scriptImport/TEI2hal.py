import requests

url = 'https://api-preprod.archives-ouvertes.fr/sword/hal'
# or manually, service is https://api-preprod.archives-ouvertes.fr/sword/upload 
	
head = {
	'Packaging': 'http://purl.org/net/sword-types/AOfr',
  'Content-Type': 'text/xml',
  'X-Allow-Completion' :None #est ce nécessaire ? 
	}
# si depot avec fichier : Content-Type : application/zip to upload pdf file  

xmlfh = open('./TEI/ART.xml') #chemin vers votre fichier
xmlcontent = xmlfh.read() 
print('TEI chargée')

response = requests.post(url, headers=head, data=xmlcontent, auth=('user', 'pass'))
print(response.text) #donne la 

print("done")
xmlfh.close()
