use sakila;

SELECT film_actor.actor_id, actor.first_name, actor.last_name, film.film_id, film.title FROM film, actor, film_actor WHERE film.film_id=film_actor.film_id AND actor.actor_id=film_actor.actor_id AND actor.actor_id=1;

