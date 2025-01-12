-- UPDATE users SET AGE = 21 -- Si usamos esta instruccion la edad de todos los usuarios se actualizaran a 21 años

UPDATE users SET AGE = 21 where idusers = 7;
-- Siempre se debe agregar un filtro de seleccion

UPDATE users SET AGE = '20', init_date = "2023-10-10" where idusers = 7; -- Cambiando 2 elementos de la tabla