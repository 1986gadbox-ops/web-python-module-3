SELECT Teachers.Name AS TeacherName, Teachers.Surname AS TeacherSurname, Groups.Name AS GroupName
FROM Teachers
CROSS JOIN Groups
SELECT DISTINCT f1.Name AS FacultyName
FROM Faculties f1
JOIN Departments d ON d.FacultyId = f1.Id
JOIN Departments d2 ON d.FacultyId = f2.Id AND d.Financing > d2.Financing
JOIN Faculties f2 ON f2.Id = d2.FacultyId
WHERE d.Financing > d2.Financing
SELECT DISTINCT f1.Name AS FacultyName
FROM Faculties f1
JOIN Departments d1 ON d1.FacultyId = f1.Id
JOIN Departments d2 ON d2.FacultyId = f1.Id
WHERE d1.Financing > d2.Financing
SELECT DISTINCT f.Name AS FacultyName
FROM Faculties f
JOIN Departments d ON d.FacultyId = f.Id
WHERE d.Financing > f.Financing
SELECT Curators.Surname, Groups.Name AS GroupName
FROM Curators
JOIN GroupsCurators ON GroupsCurators.CuratorId = Curators.Id
JOIN Groups ON Groups.Id = GroupsCurators.GroupId
SELECT DISTINCT Teachers.Name, Teachers.Surname
FROM Teachers
JOIN Lectures ON Lectures.TeacherId = Teachers.Id
JOIN GroupsLectures ON GroupsLectures.LectureId = Lectures.Id
JOIN Groups ON Groups.Id = GroupsLectures.GroupId
WHERE Groups.Name = 'P107'
SELECT DISTINCT Teachers.Surname, Faculties.Name AS FacultyName
FROM Teachers
JOIN Lectures ON Lectures.TeacherId = Teachers.Id
JOIN Departments ON Departments.Id = Lectures.SubjectId
JOIN Faculties ON Faculties.Id = Departments.FacultyId
SELECT Departments.Name AS DepartmentName, Groups.Name AS GroupName
FROM Departments
JOIN Groups ON Groups.DepartmentId = Departments.Id
SELECT DISTINCT Subjects.Name
FROM Teachers
JOIN Lectures ON Lectures.TeacherId = Teachers.Id
JOIN Subjects ON Subjects.Id = Lectures.SubjectId
WHERE Teachers.Name = 'Samantha' AND Teachers.Surname = 'Adams'
SELECT DISTINCT Departments.Name
FROM Departments
JOIN Subjects ON Subjects.Id IN (
    SELECT SubjectId FROM Lectures
)
WHERE Departments.Id IN (
    SELECT DISTINCT Departments.Id
    FROM Departments
    JOIN Subjects ON Subjects.Id = Lectures.SubjectId
)
SELECT Groups.Name
FROM Groups
JOIN Departments ON Departments.Id = Groups.DepartmentId
JOIN Faculties ON Faculties.Id = Departments.FacultyId
WHERE Faculties.Name = 'Computer Science'

SELECT Groups.Name AS GroupName, Faculties.Name AS FacultyName
FROM Groups
JOIN Departments ON Departments.Id = Groups.DepartmentId
JOIN Faculties ON Faculties.Id = Departments.FacultyId
WHERE Groups.Year = 5

SELECT 
    Teachers.Name + ' ' + Teachers.Surname AS FullName,
    Subjects.Name AS SubjectName,
    Groups.Name AS GroupName,
    Lectures.LectureRoom
FROM Lectures
JOIN Teachers ON Teachers.Id = Lectures.TeacherId
JOIN Subjects ON Subjects.Id = Lectures.SubjectId
JOIN GroupsLectures ON GroupsLectures.LectureId = Lectures.Id
JOIN Groups ON Groups.Id = GroupsLectures.GroupId
WHERE Lectures.LectureRoom = 'B103'