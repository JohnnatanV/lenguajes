-- Creamos una tabla con la siguiente sintaxis para crearla en una database a la que tengamos acceso pero que no sea la que estamos trabajando
CREATE TABLE test.persons
(
  id int,
  name varchar(100),
  age int,
  email varchar(50),
  creation_date date
);

-- Sin definir la localizacion de la tabla se crea directamente sobre la tabla en la que estamos trabajando
CREATE TABLE persons
(
  id int,
  name varchar(100),
  age int,
  email varchar(50),
  creation_date date
);

DROP table persons;
-- Funcion para borrar la tabla en la base de datos que estamos trabajando


-- NOT NULL
-- Definir si la columna creada en la nueva tabla puede tener espacios vacios

CREATE TABLE persons2
(
  id int not null,
  -- NOT NULL
  name varchar(100) not null,
  -- NOT NULL
  age int,
  email varchar(50),
  creation_date date
);

-- UNIQUE()
-- Asegura que la tabla no tenga valores repetidos que generalmente se asigna a la identificacion o la llave primaria

CREATE TABLE persons3
(
  id int not null,
  name varchar(100) not null,
  age int,
  email varchar(50),
  creation_date date,
  UNIQUE(id)
  -- UNIQUE()
);


-- PRIMARY KEY()
-- Asigna la llave primaria de la tabla y tambien asegura que esa llave primaria es un identificador unico

CREATE TABLE persons4
(
  id int not null,
  name varchar(100) not null,
  age int,
  email varchar(50),
  creation_date date,
  UNIQUE(id),
  PRIMARY KEY(id)
  -- PRIMARY KEY()
);

-- CHECK()
-- Esta instruccion asigna un metodo de verificacion para la informacion que va a ingresar a la tabla, en este caso verifica que la edad de los datos debe ser mayor a 18 años

CREATE TABLE persons5
(
  id int not null,
  name varchar(100) not null,
  age int,
  email varchar(50),
  creation_date date,
  UNIQUE(id),
  PRIMARY KEY(id),
  CHECK(age >= 18)
);


-- DEFAULT
-- Permite asignar una funcion predeterminada en la columna, en el caso de creation_date asigna de valor predeterminado la fecha y hora en el que se creo

CREATE TABLE persons6
(
  id int not null,
  name varchar(100) not null,
  age int,
  email varchar(50),
  creation_date datetime DEFAULT current_timestamp,
  -- No funciono revisar las sintaxis para corregir el error en esta caso para VSCode
  UNIQUE(id),
  PRIMARY KEY(id),
  CHECK(age >= 18)
);


-- AUTO_INCREMENT (IDENTITY)
CREATE TABLE persons7
(
  id int not null IDENTITY(1,1),
  -- auto_increment es la sintaxis para sql identity() es la sintaxis para sql server, tener en cuenta estas diferencias
  name varchar(100) not null,
  age int,
  email varchar(50),
  creation_date datetime DEFAULT CURRENT_TIMESTAMP,
  UNIQUE(id),
  PRIMARY KEY(id),
  CHECK(age >= 18)
)


-- DROP

CREATE TABLE persons8
(
  name varchar(100) not null
);

DROP TABLE persons8
-- Funcion para eliminar tablas especificas



-- ALTER TABLE
CREATE TABLE persons8
(
  id int not null IDENTITY(1,1),
  -- auto_increment es la sintaxis para sql identity() es la sintaxis para sql server, tener en cuenta estas diferencias
  name varchar(100) not null,
  age int,
  email varchar(50),
  creation_date datetime DEFAULT CURRENT_TIMESTAMP,
  UNIQUE(id),
  PRIMARY KEY(id),
  CHECK(age >= 18)
);

-- ADD 
-- Agrega una columna nueva a la tabla
ALTER TABLE persons9
ADD surname varchar(100)


-- RENAME

-- SQL
-- ALTER TABLE persons9
-- RENAME COLUMN surname TO description

-- SQL Server:
EXEC sp_rename 'table_name.old_name',  'new_name', 'COLUMN';

-- 3:31:09

-- MODIFY

-- SQL
-- ALTER TABLE persons9 MODIFY COLUMN description varchar(250)

ALTER TABLE persons9 
ALTER COLUMN description varchar(250)


-- DROP COLUMN

ALTER TABLE persons9 DROP COLUMN description