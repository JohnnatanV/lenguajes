SELECT *
FROM users INNER JOIN dni ON users.user_id = dni.user_id;

/*
El inner join trae los datos que tienen en comun ambas tablas
*/

-- JOIN 1:1
SELECT *
FROM users JOIN dni ON users.user_id = dni.user_id;


SELECT *
FROM users JOIN dni ON users.user_id = dni.user_id
order by age desc;

SELECT name, surname, dni_number
FROM users JOIN dni ON users.user_id = dni.user_id
where age<30
order by age desc;


-- JOIN 1:N

SELECT *
FROM users
  join companies
  on users.company_id = companies.company_id;

SELECT *
FROM companies
  join users
  on users.company_id = companies.company_id;

SELECT companies.name, user_id, users.name, surname
FROM companies
  join users
  on users.company_id = companies.company_id;


SELECT companies.name, user_id, users.name, surname
FROM companies
  join users
  on users.company_id = companies.company_id
where companies.name = "Google";


-- JOIN N:M

SELECT *
FROM users_languages
  join users on users_languages.user_id = users.user_id
  join languages on users_languages.language_id = languages.language_id;


SELECT users.name, surname, languages.name
FROM users_languages
  join users on users_languages.user_id = users.user_id
  join languages on users_languages.language_id = languages.language_id;

SELECT users.name, surname, languages.name, companies.name
FROM users_languages
  join users on users_languages.user_id = users.user_id
  join languages on users_languages.language_id = languages.language_id
  join companies on companies.company_id = users.company_id;


-- Que lenguajes se utilizan en las distintas compañias?
SELECT languages.name, companies.name
FROM users_languages
  JOIN users ON users.user_id = users_languages.user_id
  JOIN languages ON languages.language_id = users_languages.language_id
  JOIN companies ON users.company_id = companies.company_id