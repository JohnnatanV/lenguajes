/*

Las relaciones principales en SQL son 4

Relacion 1:1
Es decir que cada elemento de una tabla esta relacionada solo a un elemento de otra tabla y viceversa

Relacion 1:N
1 elemento de una tabla puede estar relacionada a multiples elementos de otra tabla pero en la otra tabla solo puede estar relacionada a un solo elemento

Relacion N:M
En este caso, la relacion es de muchos a muchos, quiere decir que  multiples elementos dentro de una tabla pueden estar relacionados a multiples elementos de otra tabla y viceversa

Relacion autoreferencia
Este caso es una relacion dentro de la misma tabla donde se hace lo que dice una autoreferencia dentro de la tabla

*/


-- ## Creacion de tabla con relacion 1:1

create table dni
(
  -- dni_id int not null auto_increment primary key,
  dni_id int not null IDENTITY(1,1) primary key,
  dni_number int not null,
  user_id int,
  unique(dni_id),
  foreign key(user_id) references users(idusers)
)


-- ## Creacion de tabla con relacion 1:N


create table companies
(
  company_id varchar(100) primary key,
  name varchar(100) not null,
);
-- Crear la tabla donde se hara la relacion N o en su defecto dentro de una tabla creada, crear la columna con la que se va a hacer la relacion luego
alter table users
add company_id int not NULL

-- Luego se puede hacer la conexion entre las 2 tablas
alter table users
ADD constraint company_id -- Esta linea agrega un sobre nombre a la llave externa que vincula la relacion entre las tablas
foreign key (company_id) references companies(company_id)


-- ## Creacion de tabla con relacion N:N

-- Este caso es especial ya que para poder hacer una relacion N:N entre 2 tablas se debe integrar una 3ra tabla que es la que va a tener la relacion entre las 2 tablas para un ejemplo practico 

CREATE TABLE languages
(
  -- language_id int auto_increment not null primary key,
  language_id int IDENTITY(1,1) not null primary key,
  name varchar(100)
);

CREATE TABLE users_languages
(
  -- user_language_id int auto_increment not null primary key,
  user_language_id int IDENTITY(1,1) not null primary key,
  user_id int,
  language_id int,
  foreign key(user_id) references users(user_id),
  foreign key(language_id) references languages(language_id),
  unique (user_id, language_id)
);

/*
El concepto es simple, crear un tabla de lenguajes de programacion, esta va estar relacionada a una tabla de ususarios
cada uno de los usuarios puede saber uno o mas lenguajes de programacion, por ende cada lenguaje de programacion puede estar asignado a mas de un usuario
debido a esta relacion es que se necesita que exista una tercera tabla donde va a ir la relacion entre ususario y lenguajes.
*/

