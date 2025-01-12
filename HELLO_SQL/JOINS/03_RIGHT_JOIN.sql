SELECT name, surname, dni_number
FROM users
  RIGHT JOIN dni
  ON users.user_id = dni.user_id;

SELECT users.name, surname, languages.name, companies.name
FROM users_languages
  right join users on users_languages.user_id = users.user_id
  right join languages on users_languages.language_id = languages.language_id
  right join companies on companies.company_id = users.company_id;

SELECT *
FROM users
  right JOIN dni
  ON users.user_id = dni.user_id;

SELECT name, surname, dni_number
FROM users
  right JOIN dni
  ON users.user_id = dni.user_id;