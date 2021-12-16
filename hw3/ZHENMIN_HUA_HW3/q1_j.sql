use sakila;

SELECT title, release_year FROM film WHERE film_id=ANY(SELECT film_id FROM film_actor WHERE actor_id=1);

