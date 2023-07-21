-- SQL-команды для создания таблиц
CREATE TABLE customers
(
	customer_id varchar(6) PRIMARY KEY,
	company_name varchar(40) NOT NULL,
	contact_name varchar(40) NOT NULL
);

CREATE TABLE  employees
(
	employee_id int2 PRIMARY KEY,
	first_name varchar(10) NOT NULL,
	last_name varchar(20) NOT NULL,
	title varchar(40) NOT NULL,
	birhh_date varchar(10) NOT NULL,
	notes text NOT NULL
);

CREATE TABLE orders
(
	order_id int2 PRIMARY KEY,
	customer_id varchar(6) REFERENCES customers(customer_id) NOT NULL,
	employee_id int2  REFERENCES employees(employee_id) NOT NULL,
	order_date varchar(10) NOT NULL,
	ship_city varchar(20) NOT NULL
);