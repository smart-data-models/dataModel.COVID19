Entità: EUProofOfVaccination  
============================  
[Licenza aperta](https://github.com/smart-data-models//dataModel.COVID19/blob/master/EUProofOfVaccination/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descrizione globale: **Certificato digitale Covid versione 1.3.0 adattato per funzionare con lo standard NGSI dal programma Smart Data Models**  

## Elenco delle proprietà  

- `dob`: Data di nascita. Data di nascita della persona indirizzata nel DCC. Formato data ISO 8601 limitato all'intervallo 1900-2099 o vuoto  - `id`: Identificatore unico dell'entità  - `nam`: Cognome(i), nome(i) - in questo ordine  - `r`: Gruppo di recupero  - `t`: Gruppo di test  - `type`: Tipo di entità NGSI. Deve essere EUProofOfVaccination  - `v`: Gruppo di vaccinazione  - `ver`: Versione dello schema. Versione dello schema, secondo il Semantic versioning (ISO, https://semver.org/ versione 2.0.0 o più recente)    
Proprietà richieste  
- `id`  - `type`    
Questo modello di dati è un adattamento della prova di vaccinazione UE versione 1.3.0. Maggiori informazioni su [https://ec.europa.eu/health/sites/default/files/ehealth/docs/vaccination-proof_interoperability-guidelines_en.pdf](https://ec.europa.eu/health/sites/default/files/ehealth/docs/vaccination-proof_interoperability-guidelines_en.pdf). L'adattamento aggiunge due attributi obbligatori per essere compatibile con lo standard NGSI, id e type.  
## Descrizione del modello di dati delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
EUProofOfVaccination:    
  description: 'EU Digital Covid Certificate version 1.3.0 adapted to work with NGSI standard by Smart Data Models Program'    
  properties:    
    dob:    
      description: 'Date of birth. Date of Birth of the person addressed in the DCC. ISO 8601 date format restricted to range 1900-2099 or empty'    
      pattern: ^((19|20)\d\d(-\d\d){0,2}){0,1}$    
      type: string    
      x-ngsi:    
        type: Property    
    id:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Unique identifier of the entity'    
      x-ngsi:    
        type: Property    
    nam:    
      description: 'Surname(s), forename(s) - in that order'    
      properties:    
        fn:    
          description: 'Property. Surname. The surname or primary name(s) of the person addressed in the certificate'    
          maxLength: 80    
          type: string    
        fnt:    
          description: 'Property. Standardised surname. The surname(s) of the person, transliterated ICAO 9303'    
          maxLength: 80    
          pattern: ^[A-Z<]*$    
          type: string    
        gn:    
          description: 'Property. Forename. The forename(s) of the person addressed in the certificate'    
          maxLength: 80    
          type: string    
        gnt:    
          description: 'Property. Standardised forename. The forename(s) of the person, transliterated ICAO 9303'    
          maxLength: 80    
          pattern: ^[A-Z<]*$    
          type: string    
      type: object    
      x-ngsi:    
        type: Property    
    r:    
      description: 'Recovery Group'    
      items:    
        description: 'Recovery Entry'    
        properties:    
          ci:    
            description: 'Property. Unique Certificate Identifier: UVCI. Certificate Identifier, format as per UVCI: Annex 2 in  https://ec.europa.eu/health/sites/health/files/ehealth/docs/vaccination-proof_interoperability-guidelines_en.pdf'    
            maxLength: 80    
            type: string    
          co:    
            description: 'Property. Country of Vaccination / Test, ISO 3166 alpha-2 where possible'    
            pattern: "[A-Z]{1,10}"    
            type: string    
          df:    
            description: 'ISO 8601 complete date: Certificate Valid From'    
            format: date    
            type: string    
          du:    
            description: 'ISO 8601 complete date: Certificate Valid Until'    
            format: date    
            type: string    
          fr:    
            description: 'ISO 8601 complete date of first positive NAA test result'    
            format: date    
            type: string    
          is:    
            description: 'Certificate Issuer'    
            maxLength: 80    
            type: string    
          tg:    
            description: 'Property. Disease or agent targeted. EU eHealthNetwork: Value Sets for Digital Covid Certificates. version 1.0, 2021-04-16, section 2.1. For COVID19 the value has to be 840539006. More info in https://github.com/ehn-dcc-development/ehn-dcc-schema/blob/release/1.3.0/valuesets/disease-agent-targeted.json For other values check https://www.snomed.org/snomed-ct/five-step-briefing'    
            type: string    
        required:    
          - tg    
          - fr    
          - co    
          - is    
          - df    
          - du    
          - ci    
        type: object    
      maxItems: 1    
      minItems: 1    
      type: array    
    t:    
      description: 'Test Group'    
      items:    
        description: 'Test Entry'    
        properties:    
          ci:    
            description: 'Property. Unique Certificate Identifier: UVCI. Certificate Identifier, format as per UVCI: Annex 2 in  https://ec.europa.eu/health/sites/health/files/ehealth/docs/vaccination-proof_interoperability-guidelines_en.pdf'    
            maxLength: 80    
            type: string    
          co:    
            description: 'Property. Country of Test, ISO 3166 alpha-2 where possible'    
            pattern: "[A-Z]{1,10}"    
            type: string    
          is:    
            description: 'Certificate Issuer'    
            maxLength: 80    
            type: string    
          ma:    
            description: 'Property. RAT Test name and manufacturer. EU eHealthNetwork: Value Sets for Digital Covid Certificates. version 1.0, 2021-04-16, section 2.4. The values are ORG-100001699 for AstraZeneca AB, ORG-100030215 for Biontech Manufacturing GmbH, ORG-100001417 for Janssen-Cilag International, ORG-100031184 for Moderna Biotech Spain S.L., ORG-100006270 for Curevac AG, ORG-100013793 for CanSino Biologics, ORG-100020693 for China Sinopharm International Corp. - Beijing location, ORG-100010771 for Sinopharm Weiqida Europe Pharmaceutical s.r.o. - Prague location, ORG-100024420 for Sinopharm Zhijun (Shenzhen) Pharmaceutical Co. Ltd. - Shenzhen location, ORG-100032020 for Novavax CZ AS, Gamaleya-Research-Institute for Gamaleya Research Institute, Vector-Institute for Vector Institute, Sinovac-Biotech for Sinovac Biotech, Bharat-Biotech for Bharat Biotech. More info at https://github.com/ehn-dcc-development/ehn-dcc-schema/blob/release/1.3.0/valuesets/vaccine-mah-manf.json'    
            type: string    
          nm:    
            description: 'NAA Test Name'    
            maxLength: 80    
            type: string    
          sc:    
            description: 'Date/Time of Sample Collection'    
            format: date-time    
            type: string    
          tc:    
            description: 'Testing Centre'    
            maxLength: 80    
            type: string    
          tg:    
            description: 'Property. Disease or agent targeted. EU eHealthNetwork: Value Sets for Digital Covid Certificates. version 1.0, 2021-04-16, section 2.1. For COVID19 the value has to be 840539006. More info in https://github.com/ehn-dcc-development/ehn-dcc-schema/blob/release/1.3.0/valuesets/disease-agent-targeted.json For other values check https://www.snomed.org/snomed-ct/five-step-briefing'    
            type: string    
          tr:    
            description: 'Property. EU eHealthNetwork: Value Sets for Digital Covid Certificates. version 1.0, 2021-04-16, section 2.9. Test Result. the values for COVID19 are 260415000 for Not detected and 260373001 for Detected. More info at https://github.com/ehn-dcc-development/ehn-dcc-schema/blob/release/1.3.0/valuesets/test-result.json'    
            type: string    
          tt:    
            description: 'Property. Type of Test. EU eHealthNetwork: Value Sets for Digital Covid Certificates version 1.0, 2021-04-16, section 2.7. The values for COVID19 are LP6464-4 for Nucleic acid amplification with probe detection, LP217198-3 for Rapid immunoassay. '    
            type: string    
        required:    
          - tg    
          - tt    
          - sc    
          - tr    
          - co    
          - is    
          - ci    
        type: object    
      maxItems: 1    
      minItems: 1    
      type: array    
      x-ngsi:    
        type: Property    
    type:    
      description: 'NGSI entity type. It has to be EUProofOfVaccination'    
      enum:    
        - EUProofOfVaccination    
      type: string    
      x-ngsi:    
        type: Property    
    v:    
      description: 'Vaccination Group'    
      items:    
        properties:    
          ci:    
            description: 'Property. Unique Certificate Identifier: UVCI. Certificate Identifier, format as per UVCI: Annex 2 in  https://ec.europa.eu/health/sites/health/files/ehealth/docs/vaccination-proof_interoperability-guidelines_en.pdf'    
            maxLength: 80    
            type: string    
          co:    
            description: 'Country of Vaccination / Test, ISO 3166 alpha-2 where possible'    
            pattern: "[A-Z]{1,10}"    
            type: string    
          dn:    
            description: 'Property. Dose Number. Dose Number / Total doses in Series: positive integer'    
            minimum: 1    
            type: integer    
          dt:    
            description: 'ISO8601 complete date: Date of Vaccination'    
            format: date    
            type: string    
          is:    
            description: 'Certificate Issuer'    
            maxLength: 80    
            type: string    
          ma:    
            description: 'Property. Marketing Authorization Holder - if no MAH present, then manufacturer. EU eHealthNetwork: Value Sets for Digital Covid Certificates. version 1.0, 2021-04-16, section 2.4. The values are ORG-100001699 for AstraZeneca AB, ORG-100030215 for Biontech Manufacturing GmbH, ORG-100001417 for Janssen-Cilag International, ORG-100031184 for Moderna Biotech Spain S.L., ORG-100006270 for Curevac AG, ORG-100013793 for CanSino Biologics, ORG-100020693 for China Sinopharm International Corp. - Beijing location, ORG-100010771 for Sinopharm Weiqida Europe Pharmaceutical s.r.o. - Prague location, ORG-100024420 for Sinopharm Zhijun (Shenzhen) Pharmaceutical Co. Ltd. - Shenzhen location, ORG-100032020 for Novavax CZ AS, Gamaleya-Research-Institute for Gamaleya Research Institute, Vector-Institute for Vector Institute, Sinovac-Biotech for Sinovac Biotech, Bharat-Biotech for Bharat Biotech. More info at https://github.com/ehn-dcc-development/ehn-dcc-schema/blob/release/1.3.0/valuesets/vaccine-mah-manf.json'    
            type: string    
          mp:    
            description: 'Property. Vaccine medicinal product. EU eHealthNetwork: Value Sets for Digital Covid Certificates. version 1.0, 2021-04-16, section 2.3. The values are EU/1/20/1528 for Comirnaty, EU/1/20/1507 for COVID-19 Vaccine Moderna, EU/1/21/1529 for Vaxzevria, EU/1/20/1525 for COVID-19 Vaccine Janssen, CVnCoV for CVnCoV, Sputnik-V for Sputnik-V, Convidecia for Convidecia, EpiVacCorona for EpiVacCorona, BBIBP-CorV for BBIBP-CorV, Inactivated-SARS-CoV-2-Vero-Cell for Inactivated SARS-CoV-2 (Vero Cell), CoronaVac for CoronaVac, Covaxin for Covaxin (also known as BBV152 A, B, C). More info at https://github.com/ehn-dcc-development/ehn-dcc-schema/blob/release/1.3.0/valuesets/vaccine-medicinal-product.json'    
            type: string    
          sd:    
            description: 'Property. Total Series of Doses: positive integer'    
            minimum: 1    
            type: integer    
          tg:    
            description: 'Property. Disease or agent targeted. EU eHealthNetwork: Value Sets for Digital Covid Certificates. version 1.0, 2021-04-16, section 2.1. For COVID19 the value has to be 840539006. More info in https://github.com/ehn-dcc-development/ehn-dcc-schema/blob/release/1.3.0/valuesets/disease-agent-targeted.json For other values check https://www.snomed.org/snomed-ct/five-step-briefing'    
            type: string    
          vp:    
            description: 'Property. Vaccine or prophylaxis. EU eHealthNetwork: Value Sets for Digital Covid Certificates. version 1.0, 2021-04-16, section 2.2. For COVID19 the values have to be 1119349007 for SARS-CoV-2 mRNA vaccine,1119305005 for SARS-CoV-2 antigen vaccine,J07BX03 for covid-19 vaccines. More info at https://github.com/ehn-dcc-development/ehn-dcc-schema/blob/release/1.3.0/valuesets/vaccine-prophylaxis.json and other values at https://www.snomed.org/snomed-ct'    
            type: string    
        type: object    
      maxItems: 1    
      minItems: 1    
      type: array    
    ver:    
      description: 'Schema version. Version of the schema, according to Semantic versioning (ISO, https://semver.org/ version 2.0.0 or newer)'    
      pattern: ^\d+.\d+.\d+$    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: https://github.com/ehn-dcc-development/ehn-dcc-schema/blob/release/1.3.0/DCC.combined-schema.json    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.COVID19/blob/master/EUProofOfVaccination/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.COVID19/EUProofOfVaccination/schema.json    
  x-model-tags: 'EU, COVID19'    
  x-version: ""    
```  
</details>    
## Esempio di payloads  
#### EUProofOfVaccination NGSI-v2 valori chiave Esempio  
Ecco un esempio di EUProofOfVaccination in formato JSON-LD come valori chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
```json  
{  
"id": "urn:ngsi-ld:1234:ABCD",  
  "type": "EUProofOfVaccination",  
  "ver": "1.3.0",  
  "nam": {  
    "fn": "Smith-Jones",  
    "fnt": "SMITH<JONES",  
    "gn": "Charles Edward",  
    "gnt": "CHARLES<EDWARD"  
  },  
  "dob": "1964-01-01",  
  "v": [  
    {  
      "tg": "840539006",  
      "vp": "1119349007",  
      "mp": "EU/1/20/1507",  
      "ma": "ORG-100031184",  
      "dn": 1,  
      "sd": 2,  
      "dt": "2021-06-11",  
      "co": "NL",  
      "is": "Ministry of Health Welfare and Sport",  
      "ci": "URN:UVCI:01:NL:DADFCC47C7334E45A906DB12FD859FB7#1"  
    }  
  ]  
}  
```  
#### EUProofOfVaccination NGSI-v2 normalizzato Esempio  
Ecco un esempio di EUProofOfVaccination in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non usa opzioni e restituisce i dati di contesto di una singola entità.  
```json  
{  
  "id": "urn:ngsi-ld:1234:ABCD",  
  "type": "EUProofOfVaccination",  
  "ver": {  
    "type": "Text",  
    "value": "1.3.0"  
  },  
  "nam": {  
    "type": "StructuredValue",  
    "value": {  
      "fn": "Smith-Jones",  
      "fnt": "SMITH<JONES",  
      "gn": "Charles Edward",  
      "gnt": "CHARLES<EDWARD"  
    }  
  },  
  "dob": {  
    "type": "DateTime",  
    "value": "1964-01-01"  
  },  
  "r": {  
    "type": "array",  
    "value": [  
      {  
        "tg": "840539006",  
        "fr": "2021-06-01",  
        "co": "NL",  
        "is": "Ministry of Health Welfare and Sport",  
        "df": "2021-06-12",  
        "du": "2021-11-28",  
        "ci": "URN:UVCI:01:NL:DADFCC47C7334E45A906DB12FD859FB7#1"  
      }  
    ]  
  }  
}  
```  
#### EUProofOfVaccination NGSI-LD valori-chiave Esempio  
Ecco un esempio di EUProofOfVaccination in formato JSON-LD come valori chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
```json  
{  
  "id": "urn:ngsi-ld:1234:ABCD",  
  "type": "EUProofOfVaccination",  
  "ver": "1.3.0",  
  "nam": {  
    "fn": "Smith-Jones",  
    "fnt": "SMITH<JONES",  
    "gn": "Charles Edward",  
    "gnt": "CHARLES<EDWARD"  
  },  
  "dob": "1964-01-01",  
  "v": [  
    {  
      "tg": "840539006",  
      "vp": "1119349007",  
      "mp": "EU/1/20/1507",  
      "ma": "ORG-100031184",  
      "dn": 1,  
      "sd": 2,  
      "dt": "2021-06-11",  
      "co": "NL",  
      "is": "Ministry of Health Welfare and Sport",  
      "ci": "URN:UVCI:01:NL:DADFCC47C7334E45A906DB12FD859FB7#1"  
    }  
  ],  
  "@context": [  
    "https://smart-data-models.github.io/dataModel.COVID19/context.jsonld"  
  ]  
}  
```  
#### EUProofOfVaccination NGSI-LD normalizzato Esempio  
Ecco un esempio di EUProofOfVaccination in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non usa opzioni e restituisce i dati di contesto di una singola entità.  
```json  
{  
  "id": "urn:ngsi-ld:1234:ABCD",  
  "type": "EUProofOfVaccination",  
  "ver": {  
    "type": "Property",  
    "value": "1.3.0"  
  },  
  "nam": {  
    "type": "Property",  
    "value": {  
      "fn": "Smith-Jones",  
      "fnt": "SMITH<JONES",  
      "gn": "Charles Edward",  
      "gnt": "CHARLES<EDWARD"  
    }  
  },  
  "dob": {  
    "type": "Property",  
    "value": {  
      "@type": "date-time",  
      "@value": "1964-01-01"  
    }  
  },  
  "t": {  
    "type": "Property",  
    "value": [  
      {  
        "tg": "840539006",  
        "tt": "LP6464-4",  
        "nm": "ELITechGroup, SARS-CoV-2 ELITe MGBÂ® Kit",  
        "sc": "2021-06-11T17:30:00Z",  
        "tr": "260415000",  
        "tc": "Example Test Corp, Big City",  
        "co": "NL",  
        "is": "Ministry of Health Welfare and Sport",  
        "ci": "URN:UVCI:01:NL:DADFCC47C7334E45A906DB12FD859FB7#1"  
      }  
    ]  
  },  
  "@context": [  
    "https://smart-data-models.github.io/dataModel.COVID19/context.jsonld"  
  ]  
}  
```  
Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per avere una risposta su come trattare le unità di grandezza  
