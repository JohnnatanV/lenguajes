DELIMITER
//
CREATE PROCEDURE p_all_users()
BEGIN
  SELECT *
  FROM users;
END
//

-- call p_all_users;


DELIMITER //
CREATE PROCEDURE p_age_users(IN age_param int)
BEGIN
  SELECT *
  FROM users
  WHERE age = age_param;
END
//

call p_age_users
(27);


DROP PROCEDURE p_all_users;