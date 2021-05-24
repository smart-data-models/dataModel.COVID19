Entity: VaccinationCertificate  
==============================  
[Open License](https://github.com/smart-data-models//dataModel.COVID19/blob/master/VaccinationCertificate/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Global description: **Description of a COVID-19 Vaccination Certificate.**  

## List of properties  

- `address`: The mailing address  - `alternateName`: An alternative name for this item  - `areaServed`: The geographic area where a service or offered item is provided  - `credentialSubject`: Vaccine, Vaccine Event and recipient object  - `dataProvider`: A sequence of characters identifying the provider of the harmonised data entity.  - `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform.  - `dateModified`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  - `description`: A description of this item  - `expirationDate`: Date and time of expiry  - `id`: Unique identifier of the entity  - `issuanceDate`: Date and time of issuance  - `issuer`: Identity of the issuer  - `location`:   - `name`: The name of this item.  - `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `seeAlso`: list of uri pointing to additional resources about the item  - `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  - `type`: NSGI Entity Type. it has to be VaccinationCertificate    
Required properties  
- `id`  - `type`  ## Data Model description of properties  
Sorted alphabetically (click for details)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
VaccinationCertificate:    
  description: 'Description of a COVID-19 Vaccination Certificate.'    
  properties:    
    address:    
      description: 'The mailing address'    
      properties:    
        addressCountry:    
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/addressCountry'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/addressLocality'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/addressRegion'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, 03578. Model:''https://schema.org/postOfficeBoxNumber'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, 24004. Model:''https://schema.org/https://schema.org/postalCode'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/streetAddress'''    
          type: string    
      type: Property    
      x-ngsi:    
        model: https://schema.org/address    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    credentialSubject:    
      description: 'Vaccine, Vaccine Event and recipient object'    
      properties:    
        administeringCentre:    
          description: 'Property. Model:''https://schema.org/Text''. Name/code of administering centre or a health authority responsible for the vaccination event'    
          type: string    
        batchNumber:    
          description: 'Property. Model:''https://schema.org/Text''. A distinctive combination of numbers and/or letters which specifically identifies a batch'    
          type: string    
        countryOfVaccination:    
          description: 'Property. Model:''https://schema.org/Text''. The country in which the vaccine recipient was vaccinated'    
          type: string    
        healthProfessional:    
          description: 'Property. Model:''https://schema.org/Text''. Name or health professional code responsible for administering the vaccine or prophylaxis'    
          type: string    
        proof:    
          description: 'Property. Proof of Immunization'    
          properties:    
            created:    
              description: 'Property. Model:''https://schema.org/DateTime''. Date and time of proof creation'    
              format: date-time    
              type: string    
            proofValue:    
              description: 'Property. Model:''https://schema.org/Text''. Signature, Hash or JWT value of the proof'    
              type: string    
            verificationMethod:    
              anyOf:    
                - description: 'Property. Identifier format of any NGSI entity'    
                  maxLength: 256    
                  minLength: 1    
                  pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
                  type: string    
                - description: 'Property. Identifier format of any NGSI entity'    
                  format: uri    
                  type: string    
              description: 'Relationship. Model:''http://schema.org/URL''. verificationMethod object'    
          type: object    
        recipient:    
          description: 'Property. Model:''https://schema.org/Patient''. The recipient of the vaccine'    
          properties:    
            birthDate:    
              description: 'Property. Model:''https://schema.org/Date''. this rule applies to. The date on which the vaccine recipient was born'    
              format: date    
              type: string    
            familyName:    
              description: 'Property. Model:''https://schema.org/Text''. The name of the family with which the vaccine recipient identifies'    
              type: string    
            gender:    
              description: 'Property. Model:''https://schema.org/Text''. Enum:''male, female, other''. The gender of the vaccine recipient'    
              enum:    
                - male    
                - female    
                - other    
              type: string    
            givenName:    
              description: 'Property. Model:''https://schema.org/Text''. The non-family name with which the vaccine recipient identifies'    
              type: string    
          type: object    
        vaccine:    
          description: 'Property. Generic description of the vaccine/prophylaxis or its component(s)'    
          properties:    
            atcCode:    
              description: 'Property. Model:''https://schema.org/Text''. Anatomical Therapeutic Chemical Code'    
              type: string    
            disease:    
              description: 'Property. Model:''https://schema.org/Text''. Disease or agent that the vaccination administered to the recipient provides protection against'    
              type: string    
            marketingAuthorizationHolder:    
              description: 'Property. Model:''https://schema.org/Text''. Marketing Authorization Holder'    
              type: string    
            medicinalProductName:    
              description: 'Property. Model:''https://schema.org/Text''. Medicinal product name'    
              type: string    
          type: object    
      type: Property    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    description:    
      description: 'A description of this item'    
      type: Property    
    expirationDate:    
      description: 'Date and time of expiry'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: https://schema.org/DateTime    
    id:    
      anyOf: &vaccinationcertificate_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Unique identifier of the entity'    
      type: Property    
    issuanceDate:    
      description: 'Date and time of issuance'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: https://schema.org/DateTime    
    issuer:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Identity of the issuer'    
      type: Relationship    
      x-ngsi:    
        model: http://schema.org/URL    
    location:    
      $id: https://geojson.org/schema/Geometry.json    
      $schema: "http://json-schema.org/draft-07/schema#"    
      oneOf:    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                type: number    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - Point    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON Point'    
          type: object    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - LineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON LineString'    
          type: object    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 4    
                type: array    
              type: array    
            type:    
              enum:    
                - Polygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON Polygon'    
          type: object    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPoint    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiPoint'    
          type: object    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiLineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiLineString'    
          type: object    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    items:    
                      type: number    
                    minItems: 2    
                    type: array    
                  minItems: 4    
                  type: array    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPolygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiPolygon'    
          type: object    
      title: 'GeoJSON Geometry'    
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *vaccinationcertificate_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    seeAlso:    
      description: 'list of uri pointing to additional resources about the item'    
      oneOf:    
        - items:    
            format: uri    
            type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    type:    
      description: 'NSGI Entity Type. it has to be VaccinationCertificate'    
      enum:    
        - VaccinationCertificate    
      type: Property    
  required:    
    - id    
    - type    
  type: object    
```  
</details>    
## Example payloads    
#### VaccinationCertificate NGSI-v2 key-values Example    
Here is an example of a VaccinationCertificate in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
  "id": "dataModel.id.VINF:36225393",  
  "type": "VaccinationCertificate",  
  "description": "COVID-19 Vaccination Certificate",  
  "issuanceDate": "2017-01-01T01:20:00Z",  
  "expirationDate": "2017-01-01T01:20:00Z",  
  "dateCreated": "2017-01-01T01:20:00Z",  
  "issuer": "dataModel.id.VINF:12233123",  
  "credentialSubject": {  
    "batchNumber": "1183738569",  
    "administeringCentre": "MoH",  
    "healthProfessional": "MoH",  
    "countryOfVaccination": "DE",  
    "recipient": {  
      "givenName": "XYZ",  
      "familyName": "ABC",  
      "gender": "male",  
      "birthDate": "2017-01-01",  
      "vaccine": "COVID-19",  
      "atcCode": "J07BX03",  
      "medicinalProductName": "COVID-19 Vaccine Moderna",  
      "marketingAuthorizationHolder": "Moderna Biotech"  
    }  
  },  
  "proof": {  
    "created": "2017-01-01T01:20:00Z",  
    "proofValue": "eyJhbGciOiJFZERTQSIsImI2NCI6ZmFsc2UsImNyaXQiOlsiYjY0Il19..vD_vXJCWdeGpN-qKHDIlzgGC0auRPcwp3O1sOI-gN8z3UD4pI0HO_77ob5KHhhU1ugLrrwrMsKv71mqHBn-dBg",  
    "verificationMethod": "dataModel.id.VINF.982271182"  
  }  
}  
```  
#### VaccinationCertificate NGSI-v2 normalized Example    
Here is an example of a VaccinationCertificate in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  
```json  
{  
  "id": "urn:ngsi-ld:dataModel:id:VINF:36225393",  
  "type": "VaccinationCertificate",  
  "description": {  
    "type": "Text",  
    "value": "COVID-19 Vaccination Certificate"  
  },  
  "issuanceDate": {  
    "type": "DateTime",  
    "value": "2017-01-01T01:20:00Z"  
  },  
  "expirationDate": {  
    "type": "DateTime",  
    "value": "2017-01-01T01:20:00Z"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2017-01-01T01:20:00Z"  
  },  
  "issuer": {  
    "type": "Relationship",  
    "value": "dataModel.id.VINF.12233123"  
  },  
  "credentialSubject": {  
    "type": "StructuredValue",  
    "value": {  
      "batchNumber": "1183738569",  
      "administeringCentre": "MoH",  
      "healthProfessional": "MoH",  
      "countryOfVaccination": "DE",  
      "recipient": {  
        "givenName": "XYZ",  
        "familyName": "ABC",  
        "gender": "male",  
        "birthDate": "2017-01-01",  
        "vaccine": {  
          "disease": "COVID-19",  
          "atcCode": "J07BX03",  
          "medicinalProductName": "COVID-19 Vaccine Moderna",  
          "marketingAuthorizationHolder": "Moderna Biotech"  
        }  
      },  
      "proof": {  
        "created": "2017-01-01T01:20:00Z",  
        "proofValue": "eyJhbGciOiJFZERTQSIsImI2NCI6ZmFsc2UsImNyaXQiOlsiYjY0Il19..vD_vXJCWdeGpN-qKHDIlzgGC0auRPcwp3O1sOI-gN8z3UD4pI0HO_77ob5KHhhU1ugLrrwrMsKv71mqHBn-dBg",  
        "verificationMethod": "urn:ngsi-ld:dataModel:id:VINF:982271182"  
      }  
    }  
  }  
}  
```  
#### VaccinationCertificate NGSI-LD key-values Example    
Here is an example of a VaccinationCertificate in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
    "id":"urn:ngsi-ld:dataModel:id:VINF:36225393",  
    "type":"VaccinationCertificate",  
    "description":"COVID-19 Vaccination Certificate",  
    "issuanceDate":{  
        "@type":"DateTime",  
        "@value":"2017-01-01T01:20:00Z"  
    },  
    "expirationDate":{  
        "@type":"DateTime",  
        "@value":"2017-01-01T01:20:00Z"  
    },  
    "dateCreated":{  
        "@type":"DateTime",  
        "@value":"2017-01-01T01:20:00Z"  
    },  
    "issuer":"urn:ngsi-ld:dataModel:id:VINF:12233123",  
    "credentialSubject":{  
        "batchNumber":"1183738569",  
        "administeringCentre":"MoH",  
        "healthProfessional":"MoH",  
        "countryOfVaccination":"DE",  
        "recipient":{  
            "givenName":"XYZ",  
            "familyName":"ABC",  
            "gender":"male",  
            "birthDate":{  
                "@type":"Date",  
                "@value":"2017-01-01"  
            },  
            "vaccine":"COVID-19",  
            "atcCode":"J07BX03",  
            "medicinalProductName":"COVID-19 Vaccine Moderna",  
            "marketingAuthorizationHolder":"Moderna Biotech"  
        }  
    },  
    "proof":{  
        "created":{  
            "@type":"DateTime",  
            "@value":"2017-01-01T01:20:00Z"  
        },  
        "proofValue":"eyJhbGciOiJFZERTQSIsImI2NCI6ZmFsc2UsImNyaXQiOlsiYjY0Il19..vD_vXJCWdeGpN-qKHDIlzgGC0auRPcwp3O1sOI-gN8z3UD4pI0HO_77ob5KHhhU1ugLrrwrMsKv71mqHBn-dBg",  
        "verificationMethod":"urn:ngsi-ld:dataModel:id:VINF:982271182"  
    },  
    "@context":[  
        "https://smartdatamodels.org/context.jsonld"  
    ]  
}  
```  
#### VaccinationCertificate NGSI-LD normalized Example    
Here is an example of a VaccinationCertificate in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
```json  
{  
  "id": "urn:ngsi-ld:dataModel:id:VINF:36225393",  
  "type": "VaccinationCertificate",  
  "description": {  
    "type": "Property",  
    "value": "COVID-19 Vaccination Certificate"  
  },  
  "issuanceDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2017-01-01T01:20:00Z"  
    }  
  },  
  "expirationDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2017-01-01T01:20:00Z"  
    }  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2017-01-01T01:20:00Z"  
    }  
  },  
  "issuer": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:dataModel:id:VINF:12233123"  
  },  
  "credentialSubject": {  
    "batchNumber": {  
      "type": "Property",  
      "value": "1183738569"  
    },  
    "administeringCentre": {  
      "type": "Property",  
      "value": "MoH"  
    },  
    "healthProfessional": {  
      "type": "Property",  
      "value": "MoH"  
    },  
    "countryOfVaccination": {  
      "type": "Property",  
      "value": "DE"  
    },  
    "recipient": {  
      "givenName": {  
        "type": "Property",  
        "value": "XYZ"  
      },  
      "familyName": {  
        "type": "Property",  
        "value": "ABC"  
      },  
      "gender": {  
        "type": "Property",  
        "value": "male"  
      },  
      "birthDate": {  
        "type": "Property",  
        "value": {  
          "@type": "Date",  
          "@value": "2017-01-01"  
        }  
      },  
      "vaccine": {  
        "type": "Property",  
        "value": {  
          "disease": {  
            "type": "Property",  
            "value": "COVID-19"  
          },  
          "atcCode": {  
            "type": "Property",  
            "value": "J07BX03"  
          },  
          "medicinalProductName": {  
            "type": "Property",  
            "value": "COVID-19 Vaccine Moderna"  
          },  
          "marketingAuthorizationHolder": {  
            "type": "Property",  
            "value": "Moderna Biotech"  
          }  
        }  
      }  
    },  
    "proof": {  
      "type": "Property",  
      "value": {  
        "created": {  
          "type": "Property",  
          "value": {  
            "@type": "DateTime",  
            "@value": "2017-01-01T01:20:00Z"  
          }  
        },  
        "proofValue": {  
          "type": "Property",  
          "value": "eyJhbGciOiJFZERTQSIsImI2NCI6ZmFsc2UsImNyaXQiOlsiYjY0Il19..vD_vXJCWdeGpN-qKHDIlzgGC0auRPcwp3O1sOI-gN8z3UD4pI0HO_77ob5KHhhU1ugLrrwrMsKv71mqHBn-dBg"  
        },  
        "verificationMethod": {  
          "type": "Relationship",  
          "value": "urn:ngsi-ld:dataModel:id:VINF:982271182"  
        }  
      }  
    }  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
