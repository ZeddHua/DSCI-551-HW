use sakila;

SELECT COUNT(DISTINCT category_id) AS number_of_categories FROM film_category, film_actor, actor WHERE film_category.film_id=film_actor.film_id AND film_actor.actor_id=actor.actor_id AND actor.first_name='Ed' AND actor.last_name='Chase';

