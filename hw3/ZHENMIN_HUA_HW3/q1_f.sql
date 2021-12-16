use sakila;

SELECT actor_id, COUNT(film_id) AS film_count FROM film_actor GROUP BY actor_id ORDER BY film_count DESC LIMIT 5;

