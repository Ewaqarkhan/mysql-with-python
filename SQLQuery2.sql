use HR;
create table dependents(
dependent_id int primary key not null,
first_name char not null,
last_name char not null,
relationship nvarchar not null,
employee_id int foreign key references employees(employee_id)



)