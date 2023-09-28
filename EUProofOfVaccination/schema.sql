/* (Beta) Export of data model EUProofOfVaccination of the subject dataModel.COVID19 for a postgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE EUProofOfVaccination_type AS ENUM ('EUProofOfVaccination');
CREATE TABLE EUProofOfVaccination (dob text, id text, nam json, r json, t json, type EUProofOfVaccination_type, v json, ver text);