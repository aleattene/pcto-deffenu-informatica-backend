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


/* payments read */
SELECT *
FROM payments_payment

/* payments create */
INSERT INTO payments_payment (payment_date, amount, trainer_id)
VALUES ('2024-10-01', 500, 2)

/* payments delete */
DELETE FROM payments_payment
WHERE id = 3;

/* payments update */
UPDATE payments_payment
SET amount = 1500
WHERE id=2;


/* sport-certificates read */
SELECT *
FROM documentation_sportcertificate

/* sport-certificates create */
INSERT INTO documentation_sportcertificate (issue_date, expiration_date, athlete_id, sport_doctor_id)
VALUES ('2024-12-05', '2025-12-05', 1, 3)

/* sport-certificates delete */
DELETE FROM documentation_sportcertificate
WHERE id = 1;

/* sport-certificates update */
UPDATE documentation_sportcertificate
SET issue_date = '2024-11-05', expiration_date = '2025-11-05'
WHERE id=2;


/* athletes-category-AF */
SELECT first_name, last_name
FROM profiles_athlete AS pa
JOIN profiles_category AS pc 
ON pa.category_id = pc.id
WHERE pc.code = 'AF';




















