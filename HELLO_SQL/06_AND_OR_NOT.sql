select *
from users
where email not like '%@gmail%';


select *
from users
where not email = 'bar.simpson@gmail.co';

select *
from users
where not email = 'bar.simpson@gmail.co' or age > 40;


select *
from users
where not email = 'bar.simpson@gmail.co' and age > 40;