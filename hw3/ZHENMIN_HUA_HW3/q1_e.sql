use sakila;

SELECT DISTINCT film_actor.actor_id FROM film, film_actor WHERE film.film_id=film_actor.film_id AND film.length<48 ORDER BY film_actor.actor_id ASC;

