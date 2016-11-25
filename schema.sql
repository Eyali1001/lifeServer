drop table if exists patients;
create table patients (
  id integer primary key autoincrement,
  patient_name text not null UNIQUE,
  password text not null,
  image blob,
  diagnosis text,
  gender text not null,
  age int not null,
  category text,
  activechats text not null,
  treated integer not null
);

drop table if exists users;
create table users (
  id integer primary key autoincrement,
  username text not null UNIQUE,
  password text not null,
  image blob,
  activechats text not null,
  category text
);

drop table if exists images;
create table images (
   image blob not null,
   username text not null

);

drop table if exists locations;
create table locations (
	lat text not null,
	lng text not null,
	category text not null
)