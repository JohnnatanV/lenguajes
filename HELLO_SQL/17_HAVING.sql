select *
from users
having age > 20;

select count(age)
from users
having age > 20;

select count(age)
from users
having count(age) >= 9;