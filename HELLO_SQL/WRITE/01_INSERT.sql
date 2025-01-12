INSERT INTO users
  (idusers, name, surname)
VALUES(11, "Bugs", "Bunny");
-- Se puede definir el numero de identificacion ya que al crear la tabla se configuro para que fuera autoincremental

INSERT INTO users
  (name, surname)
VALUES("Lola", "Bunny");
-- Si no se define id igual funcionara

INSERT INTO users
  (idusers, name, surname)
VALUES(14, "Daffy", "Duck");
-- Si se define un id mas alto igual funcionara

