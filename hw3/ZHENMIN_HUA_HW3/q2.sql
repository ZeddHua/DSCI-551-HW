USE sakila;
DROP VIEW IF EXISTS Comedy_film;

CREATE VIEW Comedy_film AS SELECT film.* FROM film, film_category, category WHERE film_category.category_id=category.category_id AND film.film_id=film_category.film_id AND name='Comedy';

SELECT DISTINCT actor.actor_id, first_name, last_name FROM Comedy_film, actor, film_actor WHERE Comedy_film.film_id=film_actor.film_id AND film_actor.actor_id=actor.actor_id ORDER BY actor.actor_id DESC;
