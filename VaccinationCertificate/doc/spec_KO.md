<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
엔티티: 백신 접종 인증서  
==============<!-- /10-Header -->  
<!-- 15-License -->  
[오픈 라이선스](https://github.com/smart-data-models//dataModel.COVID19/blob/master/VaccinationCertificate/LICENSE.md)  
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
글로벌 설명: **코로나19 백신 접종 증명서 설명.**  
버전: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 속성 목록  

<sup><sub>[*] 속성에 유형이 없는 것은 여러 유형 또는 다른 형식/패턴을 가질 수 있기 때문입니다</sub></sup>.  
- `address[object]`: 우편 주소  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 국가. 예를 들어, 스페인  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 도로명 주소가 있는 지역 및 해당 지역에 속한 지역  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: 해당 지역이 위치한 지역과 해당 국가의 지역  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 지구는 일부 국가에서는 지방 정부에서 관리하는 행정 구역의 일종입니다.    
	- `postOfficeBoxNumber[string]`: 사서함 주소의 우체국 사서함 번호입니다. 예: 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 우편 번호입니다. 예: 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 거리 주소  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: 공공 도로의 특정 건물을 식별하는 번호    
- `alternateName[string]`: 이 항목의 대체 이름  - `areaServed[string]`: 서비스 또는 제공 품목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)- `credentialSubject[object]`: 백신, 백신 이벤트 및 수신자 개체  	- `administeringCentre[string]`: 백신 접종 행사를 담당하는 관리 센터 또는 보건 당국의 이름/코드  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `batchNumber[string]`: 배치를 구체적으로 식별하는 고유한 숫자 및/또는 문자 조합  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `countryOfVaccination[string]`: 백신 접종자가 백신을 접종받은 국가  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `healthProfessional[string]`: 백신 또는 예방 접종을 담당하는 의료 전문가 이름 또는 코드  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `proof[object]`: 예방 접종 증명    
	- `recipient[object]`: 백신 접종 대상자  . Model: [https://schema.org/Patient](https://schema.org/Patient)  
	- `vaccine[object]`: 백신/예방접종 또는 그 성분에 대한 일반적인 설명    
- `dataProvider[string]`: 조화된 데이터 엔티티의 공급자를 식별하는 일련의 문자  - `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `description[string]`: 이 항목에 대한 설명  - `expirationDate[date-time]`: 만료 날짜 및 시간  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `id[*]`: 엔티티의 고유 식별자  - `issuanceDate[date-time]`: 발급 날짜 및 시간  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `issuer[*]`: 발급자의 신원  . Model: [http://schema.org/URL](http://schema.org/URL)- `location[*]`: 항목에 대한 지오숀 참조입니다. 포인트, 라인 문자열, 다각형, 멀티포인트, 멀티라인 문자열 또는 멀티폴리곤일 수 있습니다.  - `name[string]`: 이 항목의 이름  - `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  - `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  - `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 문자 시퀀스입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  - `type[string]`: NSGI 엔티티 유형. 백신 접종 인증서여야 합니다.  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
필수 속성  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 속성에 대한 데이터 모델 설명  
알파벳순으로 정렬(자세한 내용을 보려면 클릭)  
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
## 페이로드 예시  
#### 백신 접종 인증서 NGSI-v2 키 값 예시  
다음은 키-값으로 JSON-LD 형식의 백신 인증서의 예시입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
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
#### 백신접종증명서 NGSI-v2 정규화 예시  
다음은 정규화된 JSON-LD 형식의 백신 접종 인증서의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
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
</details>  
#### 백신접종증명서 NGSI-LD 키 값 예시  
다음은 키-값으로 JSON-LD 형식의 백신 인증서의 예시입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
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
#### 백신접종증명서 NGSI-LD 정규화 예시  
다음은 정규화된 JSON-LD 형식의 백신 접종 인증서의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
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
[FAQ 10](https://smartdatamodels.org/index.php/faqs/)을 참조하여 규모 단위를 다루는 방법에 대한 답변을 확인하세요.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
