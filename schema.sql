drop table if exists patients;
create table patients (
  id integer primary key autoincrement,
  patient_name text not null,
  diagnosis text not null,
  gender text not null,
  age int not null,
  category text not null
);

drop table if exists users;
create table users (
  id integer primary key autoincrement,
  username text not null UNIQUE,
  password text not null,
  activechats text not null
);