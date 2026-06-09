CREATE DATABASE Academy;
GO

USE Academy;
GO

CREATE TABLE Departments (
    Id INT IDENTITY(1,1) PRIMARY KEY,
    Financing MONEY NOT NULL DEFAULT 0,
    Name NVARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE Faculties (
    Id INT IDENTITY(1,1) PRIMARY KEY,
    Dean NVARCHAR(MAX) NOT NULL,
    Name NVARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE Groups (
    Id INT IDENTITY(1,1) PRIMARY KEY,
    Name NVARCHAR(10) NOT NULL UNIQUE,
    Rating INT NOT NULL CHECK (Rating BETWEEN 0 AND 5),
    Year INT NOT NULL CHECK (Year BETWEEN 1 AND 5)
);

CREATE TABLE Teachers (
    Id INT IDENTITY(1,1) PRIMARY KEY,
    EmploymentDate DATE NOT NULL CHECK (EmploymentDate >= '1990-01-01'),
    IsAssistant BIT NOT NULL DEFAULT 0,
    IsProfessor BIT NOT NULL DEFAULT 0,
    Name NVARCHAR(MAX) NOT NULL,
    Position NVARCHAR(MAX) NOT NULL,
    Premium MONEY NOT NULL DEFAULT 0,
    Salary MONEY NOT NULL CHECK (Salary > 0),
    Surname NVARCHAR(MAX) NOT NULL
);

SELECT Name, Financing, Id
FROM Departments;

SELECT Name AS 'Groups.Name', Rating AS 'Groups.Rating'
FROM Groups;

SELECT 
    Surname,
    CASE WHEN Premium <> 0 THEN (Salary / Premium) * 100 ELSE NULL END AS 'Salary to Premium (%)',
    CASE WHEN (Salary + Premium) <> 0 THEN (Salary / (Salary + Premium)) * 100 ELSE NULL END AS 'Salary to Total Compensation (%)'
FROM Teachers;

SELECT 'The dean of faculty ' + Name + ' is ' + Dean AS FacultyInfo
FROM Faculties;

SELECT Surname
FROM Teachers
WHERE IsProfessor = 1 AND Salary > 1050;

SELECT Name
FROM Departments
WHERE Financing < 11000 OR Financing > 25000;

SELECT Name
FROM Faculties
WHERE Name <> 'Computer Science';

SELECT Surname, Position
FROM Teachers
WHERE IsProfessor = 0;

SELECT Surname, Position, Salary, Premium
FROM Teachers
WHERE IsAssistant = 1 AND Premium BETWEEN 160 AND 550;

SELECT Surname, Salary
FROM Teachers
WHERE IsAssistant = 1;

SELECT Surname, Position
FROM Teachers
WHERE EmploymentDate < '2000-01-01';

SELECT Name AS 'Name of Department'
FROM Departments
WHERE Name < 'Solfware Development'
ORDER BY Name;

SELECT Surname
FROM Teachers
WHERE IsAssistant = 1 AND (Salary + Premium) <= 1200;

SELECT Name
FROM Groups
WHERE Year = 5 AND Rating BETWEEN 2 AND 4;

SELECT Surname
FROM Teachers
WHERE IsAssistant = 1 AND (Premium < 550 OR Salary < 200);