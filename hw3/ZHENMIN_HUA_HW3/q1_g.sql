use sakila;

SELECT first_name, last_name FROM film_actor, actor WHERE film_actor.actor_id=actor.actor_id GROUP BY film_actor.actor_id HAVING COUNT(film_id)>30 ORDER BY first_name ASC, last_name ASC;

