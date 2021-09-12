use HR;
create table departments(
department_id int primary key not null,
department_name char not null,
location_id int foreign key references  locations(location_id)

)
