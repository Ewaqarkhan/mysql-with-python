use HR;
create table regions(
region_id int primary key not null,
region_name nchar not null,

)
create table countries(
country_id int primary key not null,
country_name char not null,
region_id int foreign key references regions(region_id)
)
create table locations(
location_id pint not null,
street_address nvarchar not null,
postal_code nvarchar not null,
city char not null,
state_province char not null,
country_id int foreign key references countries(country_id)

)