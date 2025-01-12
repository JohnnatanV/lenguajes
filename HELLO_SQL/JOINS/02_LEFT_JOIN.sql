/*
En este caso al hacer el join el resultado devuelve los los datos relacionados a la izquierda
es decir que se centra en la informacion de la tabla izquierda y deja en segundo lo relacionado a la derecha
*/

SELECT *
FROM users
  LEFT JOIN dni
  ON users.user_id = dni.user_id;

SELECT name, surname, dni_number
FROM users
  LEFT JOIN dni
  ON users.user_id = dni.user_id;

SELECT *
FROM dni
  LEFT JOIN users
  ON users.user_id = dni.user_id;

SELECT dni_number, name, surname
FROM dni
  LEFT JOIN users
  ON users.user_id = dni.user_id;

SELECT users.name, surname, languages.name, companies.name
FROM users_languages
  left join users on users_languages.user_id = users.user_id
  left join languages on users_languages.language_id = languages.language_id
  left join companies on companies.company_id = users.company_id;

-- Arroja el mismo resultado debido a las restricciones de informacion