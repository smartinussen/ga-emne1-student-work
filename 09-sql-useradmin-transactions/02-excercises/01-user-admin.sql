use world;

-- Opprett bruker
CREATE USER 'city_reader'@'%'
IDENTIFIED BY 'ReadOnly';

-- Gi rettigheter
GRANT SELECT ON world.city
to 'city_reader'@'%';

-- Vis rettigheter
SHOW GRANTS
FOR 'city_reader'@'%';

-- Se innlogget bruker
SELECT CURRENT_USER(), CONNECTION_ID();


SELECT city.Name, city.Population
FROM world.city
WHERE CountryCode = 'NOR'
    AND Name IN ('Oslo', 'Bergen');
