SELECT *,
  CASE
	when age > 18 then 'Es mayor de edad'
    when age = 18 then 'Acaba de cumplir la mayoria de edad'
	else 'Es menor de edad'
END as agetext
-- El articulo de la columna toma el nombre del alias
FROM users;

SELECT *,
  CASE
	when age > 17 then True
	else False
END as "Es mayor de edad"
FROM users;

SELECT *,
  CASE
	when age > 17 then True
	else False
END
-- Sin un alias, el articulo toma toda la evaluacion del caso
FROM users;