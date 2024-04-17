-- full creation of table
create table IF NOT EXISTS second_table (
id INT,
name VARCHAR(256),
score INT
);
insert into second_table
values
(1, "John", 10),
(2, "Alex", 3),
(3, "Bob", 14),
(4, "George", 8)
