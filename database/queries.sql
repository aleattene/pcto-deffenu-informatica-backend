/* athlets read */
SELECT * 
FROM  profiles_athlete;

/* athlets create */
INSERT INTO profiles_athlete (first_name, last_name, date_of_birth, place_of_birth, fiscal_code, category_id)
VALUES ('Luca', 'Sanna', '2000-01-01', 'Terni', 'ADMSJFKCNH101094', 2)

/* athlets delete */
DELETE FROM profiles_athlete 
WHERE id=3;

/* athlets update */
UPDATE profiles_athlete 
SET place_of_birth = 'Torino'
WHERE id=6;


/* trainers read */
SELECT *
FROM profiles_trainer
  
/* trainers create */
INSERT INTO profiles_trainer (first_name, last_name, fiscal_code)
VALUES ('Davide', 'Rossi', 'ADMSJFKCNH901094')

/* trainers delete */
DELETE FROM profiles_trainer
WHERE id = 3;

/* trainers update */
UPDATE profiles_trainer
SET fiscal_code = 'RBTTYE55G10K987W'
WHERE id=1;


/* sport-doctors read */
SELECT *
FROM profiles_sportdoctor

/* sport-doctors create */
INSERT INTO profiles_sportdoctor (first_name, last_name, vat_number)
VALUES ('Riccardo', 'Piro', '12345678912')

/* sport-doctors delete */
DELETE FROM profiles_sportdoctor
WHERE id = 1;

/* sport-doctors update */
UPDATE profiles_sportdoctor
SET last_name = 'Tornaindietro'
WHERE id=2;
















