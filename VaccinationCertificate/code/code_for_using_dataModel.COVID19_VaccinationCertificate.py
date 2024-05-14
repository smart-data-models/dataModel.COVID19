
#         # This code allows you to install a orion-ld broker in a linux system
#         # The manuals are here https://github.com/FIWARE/context.Orion-LD/tree/develop/doc/manuals-ld
#         
#         # INSTALL NGSI LD broker (OrionLD)
#         sudo docker pull mongo:3.6
#         sudo docker pull fiware/orion-ld
#         sudo docker network create fiware_default
#         sudo docker run -d --name=mongo-db --network=fiware_default --expose=27017 mongo:3.6 --bind_ip_all --smallfiles
#         sudo docker run -d --name fiware-orionld -h orion --network=fiware_default -p 1026:1026  fiware/orion-ld -dbhost mongo-db
#         
#         # TO RELAUNCH (only if you have already installed a broker in the same machine)
#         sudo docker stop fiware-orionld
#         sudo docker rm fiware-orionld
#         sudo docker stop mongo-db
#         sudo docker rm mongo-db
#         sudo docker network rm fiware_default
#         
#         # CHECK INSTANCES
#         # Check the broker is running
#         curl -X GET 'http://localhost:1026/version'
#         
#         # Check what entities are in the broker
#         curl -X GET http://localhost:1026/ngsi-ld/v1/entities?local=true&limit=1000
#         
#         # now the python code you can use to insert some value in the context broker according to the data model
#         
from pysmartdatamodels import pysmartdatamodels as sdm
import subprocess
serverUrl = "http://localhost:1026" # supposed that your broker is installed in localhost. Edit to match your configuration
dataModel = "VaccinationCertificate"
subject = "dataModel.COVID19"
credentialSubject = {'batchNumber': {'type': 'Property', 'value': '1183738569'}, 'administeringCentre': {'type': 'Property', 'value': 'MoH'}, 'healthProfessional': {'type': 'Property', 'value': 'MoH'}, 'countryOfVaccination': {'type': 'Property', 'value': 'DE'}, 'recipient': {'givenName': {'type': 'Property', 'value': 'XYZ'}, 'familyName': {'type': 'Property', 'value': 'ABC'}, 'gender': {'type': 'Property', 'value': 'male'}, 'birthDate': {'type': 'Property', 'value': {'@type': 'Date', '@value': '2017-01-01'}}, 'vaccine': {'type': 'Property', 'value': {'disease': {'type': 'Property', 'value': 'COVID-19'}, 'atcCode': {'type': 'Property', 'value': 'J07BX03'}, 'medicinalProductName': {'type': 'Property', 'value': 'COVID-19 Vaccine Moderna'}, 'marketingAuthorizationHolder': {'type': 'Property', 'value': 'Moderna Biotech'}}}}, 'proof': {'type': 'Property', 'value': {'created': {'type': 'Property', 'value': {'@type': 'DateTime', '@value': '2017-01-01T01:20:00Z'}}, 'proofValue': {'type': 'Property', 'value': 'eyJhbGciOiJFZERTQSIsImI2NCI6ZmFsc2UsImNyaXQiOlsiYjY0Il19..vD_vXJCWdeGpN-qKHDIlzgGC0auRPcwp3O1sOI-gN8z3UD4pI0HO_77ob5KHhhU1ugLrrwrMsKv71mqHBn-dBg'}, 'verificationMethod': {'type': 'Relationship', 'value': 'urn:ngsi-ld:dataModel:id:VINF:982271182'}}}}
attribute = "credentialSubject"
value = credentialSubject
# The next line creates the query for inserting this attribute in a NGSI-LD context broker if the attribute does not exist it creates it
print(sdm.update_broker(dataModel, subject, attribute, value, serverUrl=serverUrl, updateThenCreate=True))

expirationDate = "{'type': 'Property', 'value': {'@type': 'DateTime', '@value': '2017-01-01T01:20:00Z'}}"
attribute = "expirationDate"
value = expirationDate
# The next line creates the query for inserting this attribute in a NGSI-LD context broker if the attribute does not exist it creates it
print(sdm.update_broker(dataModel, subject, attribute, value, serverUrl=serverUrl, updateThenCreate=True))

issuanceDate = "{'type': 'Property', 'value': {'@type': 'DateTime', '@value': '2017-01-01T01:20:00Z'}}"
attribute = "issuanceDate"
value = issuanceDate
# The next line creates the query for inserting this attribute in a NGSI-LD context broker if the attribute does not exist it creates it
print(sdm.update_broker(dataModel, subject, attribute, value, serverUrl=serverUrl, updateThenCreate=True))

issuer = "{'type': 'Relationship', 'object': 'urn:ngsi-ld:dataModel:id:VINF:12233123'}"
attribute = "issuer"
value = issuer
# The next line creates the query for inserting this attribute in a NGSI-LD context broker if the attribute does not exist it creates it
print(sdm.update_broker(dataModel, subject, attribute, value, serverUrl=serverUrl, updateThenCreate=True))

print(" In case you have installed the orion-ld broker (see comments on the header of this program)")
print(" Execute this instruction to check that the entities has been inserted")
command = ['curl', '-X', 'GET', 'http://localhost:1026/ngsi-ld/v1/entities?local=true&limit=1000']
result = subprocess.run(command, capture_output=True, text=True)
print(result.stdout)
