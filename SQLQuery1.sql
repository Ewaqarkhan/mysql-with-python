use HR;
create table  employees(
employee_id  int primary key not null,
first_name nchar not null,
last_name nchar not null,
email nvarchar  not null,
phone_number int  not null,
hair_date Date not null,
job_id int foreign key references jobs(job_id),
salary int not null,
manager_id int not null,
department_id int not null

)