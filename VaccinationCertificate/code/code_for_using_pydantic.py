from __future__ import annotations

from datetime import date
from enum import Enum
from typing import List, Optional, Union

from pydantic import AnyUrl, AwareDatetime, BaseModel, Field, RootModel, constr


class Address(BaseModel):
    addressCountry: Optional[str] = Field(
        None, description='The country. For example, Spain'
    )
    addressLocality: Optional[str] = Field(
        None,
        description='The locality in which the street address is, and which is in the region',
    )
    addressRegion: Optional[str] = Field(
        None,
        description='The region in which the locality is, and which is in the country',
    )
    district: Optional[str] = Field(
        None,
        description='A district is a type of administrative division that, in some countries, is managed by the local government',
    )
    postOfficeBoxNumber: Optional[str] = Field(
        None,
        description='The post office box number for PO box addresses. For example, 03578',
    )
    postalCode: Optional[str] = Field(
        None, description='The postal code. For example, 24004'
    )
    streetAddress: Optional[str] = Field(None, description='The street address')
    streetNr: Optional[str] = Field(
        None, description='Number identifying a specific property on a public street'
    )


class Proof(BaseModel):
    created: Optional[AwareDatetime] = Field(
        None, description='Date and time of proof creation'
    )
    proofValue: Optional[str] = Field(
        None, description='Signature, Hash or JWT value of the proof'
    )
    verificationMethod: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(None, description='verificationMethod object')


class Gender(Enum):
    male = 'male'
    female = 'female'
    other = 'other'


class Recipient(BaseModel):
    birthDate: Optional[date] = Field(
        None,
        description='this rule applies to. The date on which the vaccine recipient was born',
    )
    familyName: Optional[str] = Field(
        None,
        description='The name of the family with which the vaccine recipient identifies',
    )
    gender: Optional[Gender] = Field(
        None,
        description="Enum:'male, female, other'. The gender of the vaccine recipient",
    )
    givenName: Optional[str] = Field(
        None,
        description='The non-family name with which the vaccine recipient identifies',
    )


class Vaccine(BaseModel):
    atcCode: Optional[str] = Field(
        None, description='Anatomical Therapeutic Chemical Code'
    )
    disease: Optional[str] = Field(
        None,
        description='Disease or agent that the vaccination administered to the recipient provides protection against',
    )
    marketingAuthorizationHolder: Optional[str] = Field(
        None, description='Marketing Authorization Holder'
    )
    medicinalProductName: Optional[str] = Field(
        None, description='Medicinal product name'
    )


class CredentialSubject(BaseModel):
    administeringCentre: Optional[str] = Field(
        None,
        description='Name/code of administering centre or a health authority responsible for the vaccination event',
    )
    batchNumber: Optional[str] = Field(
        None,
        description='A distinctive combination of numbers and/or letters which specifically identifies a batch',
    )
    countryOfVaccination: Optional[str] = Field(
        None, description='The country in which the vaccine recipient was vaccinated'
    )
    healthProfessional: Optional[str] = Field(
        None,
        description='Name or health professional code responsible for administering the vaccine or prophylaxis',
    )
    proof: Optional[Proof] = Field(None, description='Proof of Immunization')
    recipient: Optional[Recipient] = Field(
        None, description='The recipient of the vaccine'
    )
    vaccine: Optional[Vaccine] = Field(
        None,
        description='Generic description of the vaccine/prophylaxis or its component(s)',
    )


class Type(Enum):
    Point = 'Point'


class Location(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[float] = Field(..., min_length=2)
    type: Type


class Coordinate(RootModel[List[float]]):
    root: List[float]


class Type1(Enum):
    LineString = 'LineString'


class Location1(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[Coordinate] = Field(..., min_length=2)
    type: Type1


class Type2(Enum):
    Polygon = 'Polygon'


class Location2(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type2


class Type3(Enum):
    MultiPoint = 'MultiPoint'


class Location3(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[float]]
    type: Type3


class Type4(Enum):
    MultiLineString = 'MultiLineString'


class Location4(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type4


class Type5(Enum):
    MultiPolygon = 'MultiPolygon'


class Location5(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[List[Coordinate]]]
    type: Type5


class Type6(Enum):
    VaccinationCertificate = 'VaccinationCertificate'


class VaccinationCertificate(BaseModel):
    address: Optional[Address] = Field(None, description='The mailing address')
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    credentialSubject: Optional[CredentialSubject] = Field(
        None, description='Vaccine, Vaccine Event and recipient object'
    )
    dataProvider: Optional[str] = Field(
        None,
        description='A sequence of characters identifying the provider of the harmonised data entity',
    )
    dateCreated: Optional[AwareDatetime] = Field(
        None,
        description='Entity creation timestamp. This will usually be allocated by the storage platform',
    )
    dateModified: Optional[AwareDatetime] = Field(
        None,
        description='Timestamp of the last modification of the entity. This will usually be allocated by the storage platform',
    )
    description: Optional[str] = Field(None, description='A description of this item')
    expirationDate: Optional[AwareDatetime] = Field(
        None, description='Date and time of expiry'
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
    issuanceDate: Optional[AwareDatetime] = Field(
        None, description='Date and time of issuance'
    )
    issuer: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(None, description='Identity of the issuer')
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    name: Optional[str] = Field(None, description='The name of this item')
    owner: Optional[
        List[
            Union[
                constr(
                    pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!,:\\\\]+$',
                    min_length=1,
                    max_length=256,
                ),
                AnyUrl,
            ]
        ]
    ] = Field(
        None,
        description='A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)',
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    type: Optional[Type6] = Field(
        None, description='NSGI Entity Type. it has to be VaccinationCertificate'
    )
