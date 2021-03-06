import requests
import xmltodict
username = 'gokmen.simsek@student.hu.nl'
password = 'TQxDmfd3Ghmj9HiN5MFtnfAapCWj7bcx-0Yx3SJbtgS8r0bDGcpWcw'
invoer = input('voer station in')
auth_details = (username, password)
api_url = 'http://webservices.ns.nl/ns-api-avt?station={}'.format(invoer)
response = requests.get(api_url, auth=auth_details)

with open('vertrektijden.xml', 'w') as myXMLFile:
 myXMLFile.write(response.text)


vertrekXML = xmltodict.parse(response.text)
print('Dit zijn de vertrekkende treinen:')
for vertrek in vertrekXML['ActueleVertrekTijden']['VertrekkendeTrein']:
 eindbestemming = vertrek['EindBestemming']
 vertrektijd = vertrek['VertrekTijd'] # 2016-09-27T18:36:00+0200
 vertrektijd = vertrektijd[11:16] # 18:36
 print('Om '+vertrektijd+' vertrekt een trein naar '+ eindbestemming)
