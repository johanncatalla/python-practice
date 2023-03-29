create database ENROLLMENTDB;
use ENROLLMENTDB;

create table Course(
	CourseCode varchar(20) primary key,
    CoursName varchar(255) not null
);

create table Municipality(
	ZipCode int primary key,
    Town varchar(255)
);

create table Student(
	StudentNo varchar(20) primary key,
    LastName varchar(50) not null,
    Firstame varchar(255) not null,
    MiddleName varchar(50),
    BirthDate date not null,
    CourseCode varchar(20) not null,
    Email varchar(255),
    Address varchar(255) not null,
    RatePerUnit float not null,
    ZipCode int not null,
    foreign key(CourseCode) references Course(CourseCode),
    foreign key(ZipCode) references Municipality(ZipCode)
);

create table professor(
	ProfId varchar(20) primary key,
    LastName varchar(50) not null,
    FirstName varchar(255) not null,
    MiddleName varchar(50),
    ProfRank varchar(50) not null
);

create table Section(
	SectionCode varchar(20) not null,
    SY varchar(10) not null,
    Sem int not null,
    SubjCode varchar(10) not null,
    SectionDay varchar(10),
    SectionTime time,
    Room varchar(20) not null,
    ProfID varchar(20) not null,
    foreign key(ProfID) references professor(ProfId),
    primary key(SectionCode, SY, Sem)
);
    
create table Enrollment(
	StudentNo varchar(20) not null,
    SectionCode varchar(20) not null,
    SY varchar(10) not null,
    Sem int not null,
    foreign key(StudentNo) references Student(StudentNo),
    foreign key(SectionCode, SY, Sem) references Section(SectionCode, SY, Sem)
);





