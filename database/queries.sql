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


















