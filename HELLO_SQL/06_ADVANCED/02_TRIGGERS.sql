CREATE TABLE email_history
(
  email_history_id int NOT NULL identity(1,1),
  user_id int NOT NULL,
  email varchar(100) DEFAULT NULL,
  PRIMARY KEY(email_history_id),
  UNIQUE (email_history_id)
)


-- TRIGGER in MySQL Workbench

/*
DELIMITER $$

CREATE TRIGGER tg_email
AFTER
UPDATE
ON users
FOR EACH ROW
BEGIN
  IF OLD.email <> NEW.email THEN
  INSERT INTO email_history
    (user_id, email)
  VALUES
    (OLD.user_id, OLD.email);
END
IF;
END

DELIMITER ;
*/

-- SQL Server

CREATE TRIGGER tg_email
ON users
AFTER UPDATE
AS
BEGIN
  -- Comprobamos si el campo 'email' ha cambiado
  IF EXISTS (SELECT 1
  FROM inserted i
    JOIN deleted d ON i.user_id = d.user_id
  WHERE i.email <> d.email)
    BEGIN
    -- Insertamos el valor antiguo en la tabla de historial
    INSERT INTO email_history
      (user_id, email)
    SELECT d.user_id, d.email
    FROM deleted d
      JOIN inserted i ON d.user_id = i.user_id
    WHERE i.email <> d.email;
  END
END;
GO

DROP TRIGGER tg_email;
