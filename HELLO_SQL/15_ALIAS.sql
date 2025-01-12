-- ALIAS
select name, surname as lastname, init_date as date
from users;

select name, surname as apellido, init_date as 'Fecha de inicio'
from users;

select name, surname as apellido, init_date as 'Fecha de inicio'
from users
where name = "Johnnatan";


-- CONCAT

select concat(name, ' ',surname) as nombre, init_date as date
from users;


select concat(name, ' ',surname) as "Nombre completo", init_date as 'Fecha de inicio'
from users;