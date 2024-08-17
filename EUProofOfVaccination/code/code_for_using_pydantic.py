from __future__ import annotations

from datetime import date
from enum import Enum
from typing import List, Optional, Union

from pydantic import AnyUrl, AwareDatetime, BaseModel, Field, confloat, constr


class Nam(BaseModel):
    fn: Optional[constr(max_length=80)] = Field(
        None,
        description='Surname. The surname or primary name(s) of the person addressed in the certificate',
    )
    fnt: Optional[constr(pattern=r'^[A-Z<]*$', max_length=80)] = Field(
        None,
        description='Standardised surname. The surname(s) of the person, transliterated ICAO 9303',
    )
    gn: Optional[constr(max_length=80)] = Field(
        None,
        description='Forename. The forename(s) of the person addressed in the certificate',
    )
    gnt: Optional[constr(pattern=r'^[A-Z<]*$', max_length=80)] = Field(
        None,
        description='Standardised forename. The forename(s) of the person, transliterated ICAO 9303',
    )


class RItem(BaseModel):
    ci: constr(max_length=80) = Field(
        ...,
        description='Unique Certificate Identifier: UVCI. Certificate Identifier, format as per UVCI: Annex 2 in  https://ec.europa.eu/health/sites/health/files/ehealth/docs/vaccination-proof_interoperability-guidelines_en.pdf',
    )
    co: constr(pattern=r'[A-Z]{1,10}') = Field(
        ...,
        description='Country of Vaccination / Test, ISO 3166 alpha-2 where possible',
    )
    df: date = Field(..., description='ISO 8601 complete date: Certificate Valid From')
    du: date = Field(..., description='ISO 8601 complete date: Certificate Valid Until')
    fr: date = Field(
        ..., description='ISO 8601 complete date of first positive NAA test result'
    )
    is_: constr(max_length=80) = Field(
        ..., alias='is', description='Certificate Issuer'
    )
    tg: str = Field(
        ...,
        description='Disease or agent targeted. EU eHealthNetwork: Value Sets for Digital Covid Certificates. version 1.0, 2021-04-16, section 2.1. For COVID19 the value has to be 840539006. More info in https://github.com/ehn-dcc-development/ehn-dcc-schema/blob/release/1.3.0/valuesets/disease-agent-targeted.json For other values check https://www.snomed.org/snomed-ct/five-step-briefing',
    )


class TItem(BaseModel):
    ci: constr(max_length=80) = Field(
        ...,
        description='Unique Certificate Identifier: UVCI. Certificate Identifier, format as per UVCI: Annex 2 in  https://ec.europa.eu/health/sites/health/files/ehealth/docs/vaccination-proof_interoperability-guidelines_en.pdf',
    )
    co: constr(pattern=r'[A-Z]{1,10}') = Field(
        ..., description='Country of Test, ISO 3166 alpha-2 where possible'
    )
    is_: constr(max_length=80) = Field(
        ..., alias='is', description='Certificate Issuer'
    )
    ma: Optional[str] = Field(
        None,
        description='RAT Test name and manufacturer. EU eHealthNetwork: Value Sets for Digital Covid Certificates. version 1.0, 2021-04-16, section 2.4. The values are ORG-100001699 for AstraZeneca AB, ORG-100030215 for Biontech Manufacturing GmbH, ORG-100001417 for Janssen-Cilag International, ORG-100031184 for Moderna Biotech Spain S.L., ORG-100006270 for Curevac AG, ORG-100013793 for CanSino Biologics, ORG-100020693 for China Sinopharm International Corp. - Beijing location, ORG-100010771 for Sinopharm Weiqida Europe Pharmaceutical s.r.o. - Prague location, ORG-100024420 for Sinopharm Zhijun (Shenzhen) Pharmaceutical Co. Ltd. - Shenzhen location, ORG-100032020 for Novavax CZ AS, Gamaleya-Research-Institute for Gamaleya Research Institute, Vector-Institute for Vector Institute, Sinovac-Biotech for Sinovac Biotech, Bharat-Biotech for Bharat Biotech. More info at https://github.com/ehn-dcc-development/ehn-dcc-schema/blob/release/1.3.0/valuesets/vaccine-mah-manf.json',
    )
    nm: Optional[constr(max_length=80)] = Field(None, description='NAA Test Name')
    sc: AwareDatetime = Field(..., description='Date/Time of Sample Collection')
    tc: Optional[constr(max_length=80)] = Field(None, description='Testing Centre')
    tg: str = Field(
        ...,
        description='Disease or agent targeted. EU eHealthNetwork: Value Sets for Digital Covid Certificates. version 1.0, 2021-04-16, section 2.1. For COVID19 the value has to be 840539006. More info in https://github.com/ehn-dcc-development/ehn-dcc-schema/blob/release/1.3.0/valuesets/disease-agent-targeted.json For other values check https://www.snomed.org/snomed-ct/five-step-briefing',
    )
    tr: str = Field(
        ...,
        description='EU eHealthNetwork: Value Sets for Digital Covid Certificates. version 1.0, 2021-04-16, section 2.9. Test Result. the values for COVID19 are 260415000 for Not detected and 260373001 for Detected. More info at https://github.com/ehn-dcc-development/ehn-dcc-schema/blob/release/1.3.0/valuesets/test-result.json',
    )
    tt: str = Field(
        ...,
        description='Type of Test. EU eHealthNetwork: Value Sets for Digital Covid Certificates version 1.0, 2021-04-16, section 2.7. The values for COVID19 are LP6464-4 for Nucleic acid amplification with probe detection, LP217198-3 for Rapid immunoassay. ',
    )


class Type(Enum):
    EUProofOfVaccination = 'EUProofOfVaccination'


class VItem(BaseModel):
    ci: Optional[constr(max_length=80)] = Field(
        None,
        description='Unique Certificate Identifier: UVCI. Certificate Identifier, format as per UVCI: Annex 2 in  https://ec.europa.eu/health/sites/health/files/ehealth/docs/vaccination-proof_interoperability-guidelines_en.pdf',
    )
    co: Optional[constr(pattern=r'[A-Z]{1,10}')] = Field(
        None,
        description='Country of Vaccination / Test, ISO 3166 alpha-2 where possible',
    )
    dn: Optional[confloat(ge=1.0)] = Field(
        None,
        description='Dose Number. Dose Number / Total doses in Series: positive integer',
    )
    dt: Optional[date] = Field(
        None, description='ISO8601 complete date: Date of Vaccination'
    )
    is_: Optional[constr(max_length=80)] = Field(
        None, alias='is', description='Certificate Issuer'
    )
    ma: Optional[str] = Field(
        None,
        description='Marketing Authorization Holder - if no MAH present, then manufacturer. EU eHealthNetwork: Value Sets for Digital Covid Certificates. version 1.0, 2021-04-16, section 2.4. The values are ORG-100001699 for AstraZeneca AB, ORG-100030215 for Biontech Manufacturing GmbH, ORG-100001417 for Janssen-Cilag International, ORG-100031184 for Moderna Biotech Spain S.L., ORG-100006270 for Curevac AG, ORG-100013793 for CanSino Biologics, ORG-100020693 for China Sinopharm International Corp. - Beijing location, ORG-100010771 for Sinopharm Weiqida Europe Pharmaceutical s.r.o. - Prague location, ORG-100024420 for Sinopharm Zhijun (Shenzhen) Pharmaceutical Co. Ltd. - Shenzhen location, ORG-100032020 for Novavax CZ AS, Gamaleya-Research-Institute for Gamaleya Research Institute, Vector-Institute for Vector Institute, Sinovac-Biotech for Sinovac Biotech, Bharat-Biotech for Bharat Biotech. More info at https://github.com/ehn-dcc-development/ehn-dcc-schema/blob/release/1.3.0/valuesets/vaccine-mah-manf.json',
    )
    mp: Optional[str] = Field(
        None,
        description='Vaccine medicinal product. EU eHealthNetwork: Value Sets for Digital Covid Certificates. version 1.0, 2021-04-16, section 2.3. The values are EU/1/20/1528 for Comirnaty, EU/1/20/1507 for COVID-19 Vaccine Moderna, EU/1/21/1529 for Vaxzevria, EU/1/20/1525 for COVID-19 Vaccine Janssen, CVnCoV for CVnCoV, Sputnik-V for Sputnik-V, Convidecia for Convidecia, EpiVacCorona for EpiVacCorona, BBIBP-CorV for BBIBP-CorV, Inactivated-SARS-CoV-2-Vero-Cell for Inactivated SARS-CoV-2 (Vero Cell), CoronaVac for CoronaVac, Covaxin for Covaxin (also known as BBV152 A, B, C). More info at https://github.com/ehn-dcc-development/ehn-dcc-schema/blob/release/1.3.0/valuesets/vaccine-medicinal-product.json',
    )
    sd: Optional[confloat(ge=1.0)] = Field(
        None, description='Total Series of Doses: positive integer'
    )
    tg: Optional[str] = Field(
        None,
        description='Disease or agent targeted. EU eHealthNetwork: Value Sets for Digital Covid Certificates. version 1.0, 2021-04-16, section 2.1. For COVID19 the value has to be 840539006. More info in https://github.com/ehn-dcc-development/ehn-dcc-schema/blob/release/1.3.0/valuesets/disease-agent-targeted.json For other values check https://www.snomed.org/snomed-ct/five-step-briefing',
    )
    vp: Optional[str] = Field(
        None,
        description='Vaccine or prophylaxis. EU eHealthNetwork: Value Sets for Digital Covid Certificates. version 1.0, 2021-04-16, section 2.2. For COVID19 the values have to be 1119349007 for SARS-CoV-2 mRNA vaccine,1119305005 for SARS-CoV-2 antigen vaccine,J07BX03 for covid-19 vaccines. More info at https://github.com/ehn-dcc-development/ehn-dcc-schema/blob/release/1.3.0/valuesets/vaccine-prophylaxis.json and other values at https://www.snomed.org/snomed-ct',
    )


class EUProofOfVaccination(BaseModel):
    dob: Optional[constr(pattern=r'^((19|20)\\d\\d(-\\d\\d){0,2}){0,1}$')] = Field(
        None,
        description='Date of birth. Date of Birth of the person addressed in the DCC. ISO 8601 date format restricted to range 1900-2099 or empty',
    )
    id: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(None, description='Unique identifier of the entity')
    nam: Optional[Nam] = Field(
        None, description='Surname(s), forename(s) - in that order'
    )
    r: Optional[List[RItem]] = Field(
        None, description='Recovery Group', max_length=1, min_length=1
    )
    t: Optional[List[TItem]] = Field(
        None, description='Test Group', max_length=1, min_length=1
    )
    type: Optional[Type] = Field(
        None, description='NGSI entity type. It has to be EUProofOfVaccination'
    )
    v: Optional[List[VItem]] = Field(
        None, description='Vaccination Group', max_length=1, min_length=1
    )
    ver: Optional[constr(pattern=r'^\\d+.\\d+.\\d+$')] = Field(
        None,
        description='Schema version. Version of the schema, according to Semantic versioning (ISO, https://semver.org/ version 2.0.0 or newer)',
    )
