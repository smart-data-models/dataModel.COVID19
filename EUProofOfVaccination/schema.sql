/* (Beta) Export of data model EUProofOfVaccination of the subject dataModel.COVID19 for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE EUProofOfVaccination_type AS ENUM ('EUProofOfVaccination');
CREATE TABLE EUProofOfVaccination (dob TEXT, nam JSON, r JSON, t JSON, type EUProofOfVaccination_type, v JSON, ver TEXT);