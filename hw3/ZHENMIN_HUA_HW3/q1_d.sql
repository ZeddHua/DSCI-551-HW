use sakila;

SELECT address.address_id, address.address, city.city_id FROM country, city, address WHERE country.country_id=city.country_id AND city.city_id=address.city_id AND country.country_id=6;

