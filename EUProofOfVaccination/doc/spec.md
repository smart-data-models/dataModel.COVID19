<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entity: EUProofOfVaccination  
============================<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://github.com/smart-data-models//dataModel.COVID19/blob/master/EUProofOfVaccination/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Global description: **EU Digital Covid Certificate version 1.3.0 adapted to work with NGSI standard by Smart Data Models Program**  
version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## List of properties  

<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>  
- `dob[string]`: Date of birth. Date of Birth of the person addressed in the DCC. ISO 8601 date format restricted to range 1900-2099 or empty  - `id[*]`: Unique identifier of the entity  - `nam[object]`: Surname(s), forename(s) - in that order  	- `fn[string]`: Surname. The surname or primary name(s) of the person addressed in the certificate    
	- `fnt[string]`: Standardised surname. The surname(s) of the person, transliterated ICAO 9303    
	- `gn[string]`: Forename. The forename(s) of the person addressed in the certificate    
- `r[array]`: Recovery Group  - `t[array]`: Test Group  - `type[string]`: NGSI entity type. It has to be EUProofOfVaccination  - `v[array]`: Vaccination Group  - `ver[string]`: Schema version. Version of the schema, according to Semantic versioning (ISO, https://semver.org/ version 2.0.0 or newer)  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Required properties  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
This data model is an adaptation of the EU proof of vaccination version 1.3.0. More info at [https://ec.europa.eu/health/sites/default/files/ehealth/docs/vaccination-proof_interoperability-guidelines_en.pdf](https://ec.europa.eu/health/sites/default/files/ehealth/docs/vaccination-proof_interoperability-guidelines_en.pdf). The adaptation adds two mandatory attributes to be compabtible with NGSI standard, id and type.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Data Model description of properties  
Sorted alphabetically (click for details)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
EUProofOfVaccination:    
  description: EU Digital Covid Certificate version 1.3.0 adapted to work with NGSI standard by Smart Data Models Program    
  properties:    
    dob:    
      description: Date of birth. Date of Birth of the person addressed in the DCC. ISO 8601 date format restricted to range 1900-2099 or empty    
      pattern: ^((19|20)\d\d(-\d\d){0,2}){0,1}$    
      type: string    
      x-ngsi:    
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
    nam:    
      description: 'Surname(s), forename(s) - in that order'    
      properties:    
        fn:    
          description: Surname. The surname or primary name(s) of the person addressed in the certificate    
          maxLength: 80    
          type: string    
          x-ngsi:    
            type: Property    
        fnt:    
          description: 'Standardised surname. The surname(s) of the person, transliterated ICAO 9303'    
          maxLength: 80    
          pattern: ^[A-Z<]*$    
          type: string    
          x-ngsi:    
            type: Property    
        gn:    
          description: Forename. The forename(s) of the person addressed in the certificate    
          maxLength: 80    
          type: string    
          x-ngsi:    
            type: Property    
        gnt:    
          description: 'Standardised forename. The forename(s) of the person, transliterated ICAO 9303'    
          maxLength: 80    
          pattern: ^[A-Z<]*$    
          type: string    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
    r:    
      description: Recovery Group    
      items:    
        description: Recovery Entry    
        properties:    
          ci:    
            description: 'Unique Certificate Identifier: UVCI. Certificate Identifier, format as per UVCI: Annex 2 in  https://ec.europa.eu/health/sites/health/files/ehealth/docs/vaccination-proof_interoperability-guidelines_en.pdf'    
            maxLength: 80    
            type: string    
            x-ngsi:    
              type: Property    
          co:    
            description: 'Country of Vaccination / Test, ISO 3166 alpha-2 where possible'    
            pattern: "[A-Z]{1,10}"    
            type: string    
            x-ngsi:    
              type: Property    
          df:    
            description: 'ISO 8601 complete date: Certificate Valid From'    
            format: date    
            type: string    
          du:    
            description: 'ISO 8601 complete date: Certificate Valid Until'    
            format: date    
            type: string    
          fr:    
            description: ISO 8601 complete date of first positive NAA test result    
            format: date    
            type: string    
          is:    
            description: Certificate Issuer    
            maxLength: 80    
            type: string    
          tg:    
            description: 'Disease or agent targeted. EU eHealthNetwork: Value Sets for Digital Covid Certificates. version 1.0, 2021-04-16, section 2.1. For COVID19 the value has to be 840539006. More info in https://github.com/ehn-dcc-development/ehn-dcc-schema/blob/release/1.3.0/valuesets/disease-agent-targeted.json For other values check https://www.snomed.org/snomed-ct/five-step-briefing'    
            type: string    
            x-ngsi:    
              type: Property    
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
      description: Test Group    
      items:    
        description: Test Entry    
        properties:    
          ci:    
            description: 'Unique Certificate Identifier: UVCI. Certificate Identifier, format as per UVCI: Annex 2 in  https://ec.europa.eu/health/sites/health/files/ehealth/docs/vaccination-proof_interoperability-guidelines_en.pdf'    
            maxLength: 80    
            type: string    
            x-ngsi:    
              type: Property    
          co:    
            description: 'Country of Test, ISO 3166 alpha-2 where possible'    
            pattern: "[A-Z]{1,10}"    
            type: string    
            x-ngsi:    
              type: Property    
          is:    
            description: Certificate Issuer    
            maxLength: 80    
            type: string    
          ma:    
            description: 'RAT Test name and manufacturer. EU eHealthNetwork: Value Sets for Digital Covid Certificates. version 1.0, 2021-04-16, section 2.4. The values are ORG-100001699 for AstraZeneca AB, ORG-100030215 for Biontech Manufacturing GmbH, ORG-100001417 for Janssen-Cilag International, ORG-100031184 for Moderna Biotech Spain S.L., ORG-100006270 for Curevac AG, ORG-100013793 for CanSino Biologics, ORG-100020693 for China Sinopharm International Corp. - Beijing location, ORG-100010771 for Sinopharm Weiqida Europe Pharmaceutical s.r.o. - Prague location, ORG-100024420 for Sinopharm Zhijun (Shenzhen) Pharmaceutical Co. Ltd. - Shenzhen location, ORG-100032020 for Novavax CZ AS, Gamaleya-Research-Institute for Gamaleya Research Institute, Vector-Institute for Vector Institute, Sinovac-Biotech for Sinovac Biotech, Bharat-Biotech for Bharat Biotech. More info at https://github.com/ehn-dcc-development/ehn-dcc-schema/blob/release/1.3.0/valuesets/vaccine-mah-manf.json'    
            type: string    
            x-ngsi:    
              type: Property    
          nm:    
            description: NAA Test Name    
            maxLength: 80    
            type: string    
          sc:    
            description: Date/Time of Sample Collection    
            format: date-time    
            type: string    
          tc:    
            description: Testing Centre    
            maxLength: 80    
            type: string    
          tg:    
            description: 'Disease or agent targeted. EU eHealthNetwork: Value Sets for Digital Covid Certificates. version 1.0, 2021-04-16, section 2.1. For COVID19 the value has to be 840539006. More info in https://github.com/ehn-dcc-development/ehn-dcc-schema/blob/release/1.3.0/valuesets/disease-agent-targeted.json For other values check https://www.snomed.org/snomed-ct/five-step-briefing'    
            type: string    
            x-ngsi:    
              type: Property    
          tr:    
            description: 'EU eHealthNetwork: Value Sets for Digital Covid Certificates. version 1.0, 2021-04-16, section 2.9. Test Result. the values for COVID19 are 260415000 for Not detected and 260373001 for Detected. More info at https://github.com/ehn-dcc-development/ehn-dcc-schema/blob/release/1.3.0/valuesets/test-result.json'    
            type: string    
            x-ngsi:    
              type: Property    
          tt:    
            description: 'Type of Test. EU eHealthNetwork: Value Sets for Digital Covid Certificates version 1.0, 2021-04-16, section 2.7. The values for COVID19 are LP6464-4 for Nucleic acid amplification with probe detection, LP217198-3 for Rapid immunoassay. '    
            type: string    
            x-ngsi:    
              type: Property    
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
      description: NGSI entity type. It has to be EUProofOfVaccination    
      enum:    
        - EUProofOfVaccination    
      type: string    
      x-ngsi:    
        type: Property    
    v:    
      description: Vaccination Group    
      items:    
        properties:    
          ci:    
            description: 'Unique Certificate Identifier: UVCI. Certificate Identifier, format as per UVCI: Annex 2 in  https://ec.europa.eu/health/sites/health/files/ehealth/docs/vaccination-proof_interoperability-guidelines_en.pdf'    
            maxLength: 80    
            type: string    
            x-ngsi:    
              type: Property    
          co:    
            description: 'Country of Vaccination / Test, ISO 3166 alpha-2 where possible'    
            pattern: "[A-Z]{1,10}"    
            type: string    
          dn:    
            description: 'Dose Number. Dose Number / Total doses in Series: positive integer'    
            minimum: 1    
            type: number    
            x-ngsi:    
              type: Property    
          dt:    
            description: 'ISO8601 complete date: Date of Vaccination'    
            format: date    
            type: string    
          is:    
            description: Certificate Issuer    
            maxLength: 80    
            type: string    
          ma:    
            description: 'Marketing Authorization Holder - if no MAH present, then manufacturer. EU eHealthNetwork: Value Sets for Digital Covid Certificates. version 1.0, 2021-04-16, section 2.4. The values are ORG-100001699 for AstraZeneca AB, ORG-100030215 for Biontech Manufacturing GmbH, ORG-100001417 for Janssen-Cilag International, ORG-100031184 for Moderna Biotech Spain S.L., ORG-100006270 for Curevac AG, ORG-100013793 for CanSino Biologics, ORG-100020693 for China Sinopharm International Corp. - Beijing location, ORG-100010771 for Sinopharm Weiqida Europe Pharmaceutical s.r.o. - Prague location, ORG-100024420 for Sinopharm Zhijun (Shenzhen) Pharmaceutical Co. Ltd. - Shenzhen location, ORG-100032020 for Novavax CZ AS, Gamaleya-Research-Institute for Gamaleya Research Institute, Vector-Institute for Vector Institute, Sinovac-Biotech for Sinovac Biotech, Bharat-Biotech for Bharat Biotech. More info at https://github.com/ehn-dcc-development/ehn-dcc-schema/blob/release/1.3.0/valuesets/vaccine-mah-manf.json'    
            type: string    
            x-ngsi:    
              type: Property    
          mp:    
            description: 'Vaccine medicinal product. EU eHealthNetwork: Value Sets for Digital Covid Certificates. version 1.0, 2021-04-16, section 2.3. The values are EU/1/20/1528 for Comirnaty, EU/1/20/1507 for COVID-19 Vaccine Moderna, EU/1/21/1529 for Vaxzevria, EU/1/20/1525 for COVID-19 Vaccine Janssen, CVnCoV for CVnCoV, Sputnik-V for Sputnik-V, Convidecia for Convidecia, EpiVacCorona for EpiVacCorona, BBIBP-CorV for BBIBP-CorV, Inactivated-SARS-CoV-2-Vero-Cell for Inactivated SARS-CoV-2 (Vero Cell), CoronaVac for CoronaVac, Covaxin for Covaxin (also known as BBV152 A, B, C). More info at https://github.com/ehn-dcc-development/ehn-dcc-schema/blob/release/1.3.0/valuesets/vaccine-medicinal-product.json'    
            type: string    
            x-ngsi:    
              type: Property    
          sd:    
            description: 'Total Series of Doses: positive integer'    
            minimum: 1    
            type: number    
            x-ngsi:    
              type: Property    
          tg:    
            description: 'Disease or agent targeted. EU eHealthNetwork: Value Sets for Digital Covid Certificates. version 1.0, 2021-04-16, section 2.1. For COVID19 the value has to be 840539006. More info in https://github.com/ehn-dcc-development/ehn-dcc-schema/blob/release/1.3.0/valuesets/disease-agent-targeted.json For other values check https://www.snomed.org/snomed-ct/five-step-briefing'    
            type: string    
            x-ngsi:    
              type: Property    
          vp:    
            description: 'Vaccine or prophylaxis. EU eHealthNetwork: Value Sets for Digital Covid Certificates. version 1.0, 2021-04-16, section 2.2. For COVID19 the values have to be 1119349007 for SARS-CoV-2 mRNA vaccine,1119305005 for SARS-CoV-2 antigen vaccine,J07BX03 for covid-19 vaccines. More info at https://github.com/ehn-dcc-development/ehn-dcc-schema/blob/release/1.3.0/valuesets/vaccine-prophylaxis.json and other values at https://www.snomed.org/snomed-ct'    
            type: string    
            x-ngsi:    
              type: Property    
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
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.COVID19/blob/master/EUProofOfVaccination/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.COVID19/EUProofOfVaccination/schema.json    
  x-model-tags: 'EU, COVID19'    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Example payloads    
#### EUProofOfVaccination NGSI-v2 key-values Example    
Here is an example of a EUProofOfVaccination in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### EUProofOfVaccination NGSI-v2 normalized Example    
Here is an example of a EUProofOfVaccination in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### EUProofOfVaccination NGSI-LD key-values Example    
Here is an example of a EUProofOfVaccination in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:1234:ABCD",  
    "type": "EUProofOfVaccination",  
    "dob": "1964-01-01",  
    "nam": {  
        "fn": "Smith-Jones",  
        "fnt": "SMITH<JONES",  
        "gn": "Charles Edward",  
        "gnt": "CHARLES<EDWARD"  
    },  
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
    "ver": "1.3.0",  
    "@context": [  
        "https://smart-data-models.github.io/dataModel.COVID19/context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.COVID19/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### EUProofOfVaccination NGSI-LD normalized Example    
Here is an example of a EUProofOfVaccination in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:1234:ABCD",  
    "type": "EUProofOfVaccination",  
    "dob": {  
        "type": "Property",  
        "value": {  
            "@type": "date-time",  
            "@value": "1964-01-01"  
        }  
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
    "t": {  
        "type": "Property",  
        "value": [  
            {  
                "tg": "840539006",  
                "tt": "LP6464-4",  
                "nm": "ELITechGroup, SARS-CoV-2 ELITe MGB\u00ae Kit",  
                "sc": "2021-06-11T17:30:00Z",  
                "tr": "260415000",  
                "tc": "Example Test Corp, Big City",  
                "co": "NL",  
                "is": "Ministry of Health Welfare and Sport",  
                "ci": "URN:UVCI:01:NL:DADFCC47C7334E45A906DB12FD859FB7#1"  
            }  
        ]  
    },  
    "ver": {  
        "type": "Property",  
        "value": "1.3.0"  
    },  
    "@context": [  
        "https://smart-data-models.github.io/dataModel.COVID19/context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.COVID19/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
See [FAQ 10](https://smartdatamodels.org/index.php/faqs/) to get an answer on how to deal with magnitude units  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
