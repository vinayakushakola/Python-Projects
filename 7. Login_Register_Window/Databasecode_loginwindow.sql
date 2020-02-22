create database loginwindow;
create table loginwindow.RegData(
Fullname varchar(20),
username varchar(20) primary key,
password varchar(20)
);

create table loginwindow.Users(
Username varchar(20) primary key,
Password varchar(20)
);

select * from loginwindow.regdata;
select * from loginwindow.users;