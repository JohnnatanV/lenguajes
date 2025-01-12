create table companies
(
  -- company_id int auto_increment not null primary key,
  company_id int identity(1,1) not null primary key,
  name varchar(100)
);

create table languages
(
  -- language_id int auto_increment not null primary key,
  language_id int identity(1,1) not null primary key,
  name varchar(100)
);

create table users
(
  -- user_id int auto_increment not null primary key,
  user_id int identity(1,1) not null primary key,
  name varchar(100) not null,
  surname varchar(100),
  age int,
  company_id int not null,
  foreign key(company_id) references companies(company_id)
);

create table dni
(
  -- dni_id int auto_increment not null primary key,
  dni_id int identity(1,1) not null primary key,
  dni_number int not null,
  user_id int,
  foreign key(user_id) references users(user_id)
);

create table users_languages
(
  -- user_language_id int auto_increment not null primary key,
  user_language_id int identity(1,1) not null primary key,
  user_id int,
  language_id int,
  foreign key(user_id) references users(user_id),
  foreign key(language_id) references languages(language_id)
);


-- 4:07:33