CREATE VIEW [v_user_ages]
AS
  SELECT name, age
  FROM users
  WHERE AGE >= 25;

SELECT *
FROM v_user_ages;

SELECT *
FROM users;

-- DROP
DROP VIEW v_user_ages;