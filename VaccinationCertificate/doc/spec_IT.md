<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entità: Certificato di vaccinazione    
===================================<!-- /10-Header -->    
<!-- 15-License -->    
[Licenza aperta](https://github.com/smart-data-models//dataModel.COVID19/blob/master/VaccinationCertificate/LICENSE.md)    
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Descrizione globale: **Descrizione di un certificato di vaccinazione COVID-19.**    
versione: 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Elenco delle proprietà    
<sup><sub>[*] Se non c'è un tipo in un attributo è perché potrebbe avere diversi tipi o diversi formati/modelli</sub></sup>.    
- `address[object]`: L'indirizzo postale  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Il paese. Ad esempio, la Spagna  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: La località in cui si trova l'indirizzo civico e che si trova nella regione  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: La regione in cui si trova la località, e che si trova nel paese  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: Un distretto è un tipo di divisione amministrativa che, in alcuni paesi, è gestita dal governo locale.      
	- `postOfficeBoxNumber[string]`: Il numero di casella postale per gli indirizzi di casella postale. Ad esempio, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: Il codice postale. Ad esempio, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: L'indirizzo stradale  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
- `alternateName[string]`: Un nome alternativo per questa voce  - `areaServed[string]`: L'area geografica in cui viene fornito il servizio o l'articolo offerto.  . Model: [https://schema.org/Text](https://schema.org/Text)- `credentialSubject[object]`: Vaccino, evento vaccinale e oggetto destinatario  	- `administeringCentre[string]`: Nome/codice del centro di somministrazione o di un'autorità sanitaria responsabile dell'evento vaccinale  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `batchNumber[string]`: Una combinazione distintiva di numeri e/o lettere che identifica specificamente un lotto.  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `countryOfVaccination[string]`: Il Paese in cui è stato vaccinato il destinatario del vaccino  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `healthProfessional[string]`: Nome o codice professionale sanitario responsabile della somministrazione del vaccino o della profilassi  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `proof[object]`: Prova di immunizzazione      
	- `recipient[object]`: Il destinatario del vaccino  . Model: [https://schema.org/Patient](https://schema.org/Patient)    
- `dataProvider[string]`: una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata  - `dateCreated[date-time]`: Timestamp di creazione dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `dateModified[date-time]`: Timestamp dell'ultima modifica dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `description[string]`: Descrizione dell'articolo  - `expirationDate[date-time]`: Data e ora di scadenza  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `id[*]`: Identificatore univoco dell'entità  - `issuanceDate[date-time]`: Data e ora di emissione  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `issuer[*]`: Identità dell'emittente  . Model: [http://schema.org/URL](http://schema.org/URL)- `location[*]`: Riferimento geojson all'elemento. Può essere un punto, una stringa di linea, un poligono, un multi-punto, una stringa di linea o un poligono multiplo.  - `name[string]`: Il nome di questo elemento  - `owner[array]`: Un elenco contenente una sequenza di caratteri codificata JSON che fa riferimento agli ID univoci dei proprietari.  - `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source[string]`: Una sequenza di caratteri che indica la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del provider di origine o l'URL dell'oggetto di origine.  - `type[string]`: Tipo di entità NSGI. deve essere VaccinationCertificate.  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Proprietà richieste    
- `id`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Modello di dati descrizione delle proprietà    
Ordinati in ordine alfabetico (clicca per i dettagli)    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
VaccinationCertificate:      
  description: Description of a COVID-19 Vaccination Certificate.      
  properties:      
    address:      
      description: The mailing address      
      properties:      
        addressCountry:      
          description: 'The country. For example, Spain'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressCountry      
            type: Property      
        addressLocality:      
          description: 'The locality in which the street address is, and which is in the region'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressLocality      
            type: Property      
        addressRegion:      
          description: 'The region in which the locality is, and which is in the country'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressRegion      
            type: Property      
        district:      
          description: 'A district is a type of administrative division that, in some countries, is managed by the local government'      
          type: string      
          x-ngsi:      
            type: Property      
        postOfficeBoxNumber:      
          description: 'The post office box number for PO box addresses. For example, 03578'      
          type: string      
          x-ngsi:      
            model: https://schema.org/postOfficeBoxNumber      
            type: Property      
        postalCode:      
          description: 'The postal code. For example, 24004'      
          type: string      
          x-ngsi:      
            model: https://schema.org/https://schema.org/postalCode      
            type: Property      
        streetAddress:      
          description: The street address      
          type: string      
          x-ngsi:      
            model: https://schema.org/streetAddress      
            type: Property      
        streetNr:      
          description: Number identifying a specific property on a public street      
          type: string      
          x-ngsi:      
            type: Property      
      type: object      
      x-ngsi:      
        model: https://schema.org/address      
        type: Property      
    alternateName:      
      description: An alternative name for this item      
      type: string      
      x-ngsi:      
        type: Property      
    areaServed:      
      description: The geographic area where a service or offered item is provided      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    credentialSubject:      
      description: 'Vaccine, Vaccine Event and recipient object'      
      properties:      
        administeringCentre:      
          description: Name/code of administering centre or a health authority responsible for the vaccination event      
          type: string      
          x-ngsi:      
            model: https://schema.org/Text      
            type: Property      
        batchNumber:      
          description: A distinctive combination of numbers and/or letters which specifically identifies a batch      
          type: string      
          x-ngsi:      
            model: https://schema.org/Text      
            type: Property      
        countryOfVaccination:      
          description: The country in which the vaccine recipient was vaccinated      
          type: string      
          x-ngsi:      
            model: https://schema.org/Text      
            type: Property      
        healthProfessional:      
          description: Name or health professional code responsible for administering the vaccine or prophylaxis      
          type: string      
          x-ngsi:      
            model: https://schema.org/Text      
            type: Property      
        proof:      
          description: Proof of Immunization      
          properties:      
            created:      
              description: Date and time of proof creation      
              format: date-time      
              type: string      
              x-ngsi:      
                model: https://schema.org/DateTime      
                type: Property      
            proofValue:      
              description: 'Signature, Hash or JWT value of the proof'      
              type: string      
              x-ngsi:      
                model: https://schema.org/Text      
                type: Property      
            verificationMethod:      
              anyOf:      
                - description: Identifier format of any NGSI entity      
                  maxLength: 256      
                  minLength: 1      
                  pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
                  type: string      
                  x-ngsi:      
                    type: Property      
                - description: Identifier format of any NGSI entity      
                  format: uri      
                  type: string      
                  x-ngsi:      
                    type: Property      
              description: verificationMethod object      
              x-ngsi:      
                model: http://schema.org/URL      
                type: Relationship      
          type: object      
          x-ngsi:      
            type: Property      
        recipient:      
          description: The recipient of the vaccine      
          properties:      
            birthDate:      
              description: this rule applies to. The date on which the vaccine recipient was born      
              format: date      
              type: string      
              x-ngsi:      
                model: https://schema.org/Date      
                type: Property      
            familyName:      
              description: The name of the family with which the vaccine recipient identifies      
              type: string      
              x-ngsi:      
                model: https://schema.org/Text      
                type: Property      
            gender:      
              description: 'Enum:''male, female, other''. The gender of the vaccine recipient'      
              enum:      
                - male      
                - female      
                - other      
              type: string      
              x-ngsi:      
                model: https://schema.org/Text      
                type: Property      
            givenName:      
              description: The non-family name with which the vaccine recipient identifies      
              type: string      
              x-ngsi:      
                model: https://schema.org/Text      
                type: Property      
          type: object      
          x-ngsi:      
            model: https://schema.org/Patient      
            type: Property      
        vaccine:      
          description: Generic description of the vaccine/prophylaxis or its component(s)      
          properties:      
            atcCode:      
              description: Anatomical Therapeutic Chemical Code      
              type: string      
              x-ngsi:      
                model: https://schema.org/Text      
                type: Property      
            disease:      
              description: Disease or agent that the vaccination administered to the recipient provides protection against      
              type: string      
              x-ngsi:      
                model: https://schema.org/Text      
                type: Property      
            marketingAuthorizationHolder:      
              description: Marketing Authorization Holder      
              type: string      
              x-ngsi:      
                model: https://schema.org/Text      
                type: Property      
            medicinalProductName:      
              description: Medicinal product name      
              type: string      
              x-ngsi:      
                model: https://schema.org/Text      
                type: Property      
          type: object      
          x-ngsi:      
            type: Property      
      type: object      
      x-ngsi:      
        type: Property      
    dataProvider:      
      description: A sequence of characters identifying the provider of the harmonised data entity      
      type: string      
      x-ngsi:      
        type: Property      
    dateCreated:      
      description: Entity creation timestamp. This will usually be allocated by the storage platform      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    dateModified:      
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    description:      
      description: A description of this item      
      type: string      
      x-ngsi:      
        type: Property      
    expirationDate:      
      description: Date and time of expiry      
      format: date-time      
      type: string      
      x-ngsi:      
        model: https://schema.org/DateTime      
        type: Property      
    id:      
      anyOf:      
        - description: Identifier format of any NGSI entity      
          maxLength: 256      
          minLength: 1      
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
          type: string      
          x-ngsi:      
            type: Property      
        - description: Identifier format of any NGSI entity      
          format: uri      
          type: string      
          x-ngsi:      
            type: Property      
      description: Unique identifier of the entity      
      x-ngsi:      
        type: Property      
    issuanceDate:      
      description: Date and time of issuance      
      format: date-time      
      type: string      
      x-ngsi:      
        model: https://schema.org/DateTime      
        type: Property      
    issuer:      
      anyOf:      
        - description: Identifier format of any NGSI entity      
          maxLength: 256      
          minLength: 1      
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
          type: string      
          x-ngsi:      
            type: Property      
        - description: Identifier format of any NGSI entity      
          format: uri      
          type: string      
          x-ngsi:      
            type: Property      
      description: Identity of the issuer      
      x-ngsi:      
        model: http://schema.org/URL      
        type: Relationship      
    location:      
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'      
      oneOf:      
        - description: Geojson reference to the item. Point      
          properties:      
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
          title: GeoJSON Point      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. LineString      
          properties:      
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
          title: GeoJSON LineString      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. Polygon      
          properties:      
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
          title: GeoJSON Polygon      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. MultiPoint      
          properties:      
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
          title: GeoJSON MultiPoint      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. MultiLineString      
          properties:      
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
          title: GeoJSON MultiLineString      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. MultiLineString      
          properties:      
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
          title: GeoJSON MultiPolygon      
          type: object      
          x-ngsi:      
            type: GeoProperty      
      x-ngsi:      
        type: GeoProperty      
    name:      
      description: The name of this item      
      type: string      
      x-ngsi:      
        type: Property      
    owner:      
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)      
      items:      
        anyOf:      
          - description: Identifier format of any NGSI entity      
            maxLength: 256      
            minLength: 1      
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
            type: string      
            x-ngsi:      
              type: Property      
          - description: Identifier format of any NGSI entity      
            format: uri      
            type: string      
            x-ngsi:      
              type: Property      
        description: Unique identifier of the entity      
        x-ngsi:      
          type: Property      
      type: array      
      x-ngsi:      
        type: Property      
    seeAlso:      
      description: list of uri pointing to additional resources about the item      
      oneOf:      
        - items:      
            format: uri      
            type: string      
          minItems: 1      
          type: array      
        - format: uri      
          type: string      
      x-ngsi:      
        type: Property      
    source:      
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'      
      type: string      
      x-ngsi:      
        type: Property      
    type:      
      description: NSGI Entity Type. it has to be VaccinationCertificate      
      enum:      
        - VaccinationCertificate      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: ""      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.COVID19/blob/master/VaccinationCertificate/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/datamodel.COVID19/VaccinationCertificate/schema.json      
  x-model-tags: ""      
  x-version: 0.0.1      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## Esempi di payload    
#### VaccinationCertificate NGSI-v2 valori-chiave Esempio    
Ecco un esempio di certificato di vaccinazione in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.    
<details><summary><strong>show/hide example</strong></summary>      
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
      "vaccine": {  
        "disease": "COVID-19",  
        "atcCode": "J07BX03",  
        "medicinalProductName": "COVID-19 Vaccine Moderna",  
        "marketingAuthorizationHolder": "Moderna Biotech"  
      },  
      "proof": {  
        "created": "2017-01-01T01:20:00Z",  
        "proofValue": "eyJhbGciOiJFZERTQSIsImI2NCI6ZmFsc2UsImNyaXQiOlsiYjY0Il19..vD_vXJCWdeGpN-qKHDIlzgGC0auRPcwp3O1sOI-gN8z3UD4pI0HO_77ob5KHhhU1ugLrrwrMsKv71mqHBn-dBg",  
        "verificationMethod": "dataModel.id.VINF.982271182"  
      }  
    }  
  }  
}  
```  
</details>    
#### Certificato di vaccinazione NGSI-v2 normalizzato Esempio    
Ecco un esempio di certificato di vaccinazione in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si utilizzano le opzioni e restituisce i dati di contesto di una singola entità.    
<details><summary><strong>show/hide example</strong></summary>      
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
    "type": "Text",  
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
</details>    
#### Certificato di vaccinazione Valori chiave NGSI-LD Esempio    
Ecco un esempio di certificato di vaccinazione in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.    
<details><summary><strong>show/hide example</strong></summary>      
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
      "vaccine": {  
        "disease": "COVID-19",  
        "atcCode": "J07BX03",  
        "medicinalProductName": "COVID-19 Vaccine Moderna",  
        "marketingAuthorizationHolder": "Moderna Biotech"  
      },  
      "proof": {  
        "created": "2017-01-01T01:20:00Z",  
        "proofValue": "eyJhbGciOiJFZERTQSIsImI2NCI6ZmFsc2UsImNyaXQiOlsiYjY0Il19..vD_vXJCWdeGpN-qKHDIlzgGC0auRPcwp3O1sOI-gN8z3UD4pI0HO_77ob5KHhhU1ugLrrwrMsKv71mqHBn-dBg",  
        "verificationMethod": "dataModel.id.VINF.982271182"  
      }  
    }  
  },  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.COVID19/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### Certificato di vaccinazione NGSI-LD normalizzato Esempio    
Ecco un esempio di certificato di vaccinazione in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si utilizzano le opzioni e restituisce i dati di contesto di una singola entità.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
    "id": "urn:ngsi-ld:dataModel:id:VINF:36225393",  
    "type": "VaccinationCertificate",  
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
    "dateCreated": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2017-01-01T01:20:00Z"  
        }  
    },  
    "description": {  
        "type": "Property",  
        "value": "COVID-19 Vaccination Certificate"  
    },  
    "expirationDate": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2017-01-01T01:20:00Z"  
        }  
    },  
    "issuanceDate": {  
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
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.COVID19/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->    
<!-- 90-FooterNotes -->    
<!-- /90-FooterNotes -->    
<!-- 95-Units -->    
Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per ottenere una risposta su come gestire le unità di grandezza.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
