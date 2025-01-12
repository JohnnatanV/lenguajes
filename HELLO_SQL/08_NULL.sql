select *
from users
where email is null;

select *
from users
where email is not null;

select *
from users
where email is not null and age > 30;

-- IFNULL
SELECT name, surname, IFNULL(age, 0) AS age
FROM users;