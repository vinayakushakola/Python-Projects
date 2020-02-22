create database Activity;
create table Activity.RegData(
	Fullname varchar(20),
    Activity varchar(20),
    Username varchar(20) primary key,
    Password varchar(20)
);
create table Activity.Data(
	Name varchar(20),
	Date varchar(10),
	Time varchar(10)
 );
create table Activity.users
(
	Username varchar(20) ,
    Password varchar(20)
);
drop table activity.regdata;
drop table activity.users;
drop table activity.data;