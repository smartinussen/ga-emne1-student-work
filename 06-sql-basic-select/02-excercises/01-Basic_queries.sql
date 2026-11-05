-- Oppgave 1
SELECT Name, Population FROM city
WHERE CountryCode = 'SWE'
ORDER BY Population DESC;

-- Aggregate test counting cities in countries
SELECT CountryCode, COUNT(CountryCode) AS cities FROM city
WHERE CountryCode = 'SWE' OR CountryCode = 'NOR'
GROUP BY CountryCode;

