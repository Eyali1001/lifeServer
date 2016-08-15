drop table if exists patients;
create table patients (
  id integer primary key autoincrement,
  patient_name text not null UNIQUE,
  diagnosis text not null,
  gender text not null,
  age int not null,
  category text not null
);