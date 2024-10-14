Q1: 
```
CREATE TABLE Department(
Deptno INT,
Deptname VARCHAR(100),
Location varchar(100)
)


DESC Department
```
![Alt text](/AssignmentImg/001.png "student")

```
CREATE TABLE Employee(
Empno INT,
ManagerID INT,
FirstName VARCHAR(100),
LastName VARCHAR(100),
UserID NUMBER,
DeptNo INT,
Salary NUMBER,
Commission INT,
JoiningDate DATE,
Designation VARCHAR(100)
)

DESC Employee
```

![Alt text](/AssignmentImg/0012.png "student")


Q2:

```
ALTER TABLE Department ADD CONSTRAINT dep_ref PRIMARY KEY(Deptno)
ALTER TABLE Department ADD CONSTRAINT uniq_ref UNIQUE(Deptname)
ALTER TABLE Department MODIFY Deptno NUMBER(2,0)
ALTER TABLE Department MODIFY Deptname VARCHAR2(20)
ALTER TABLE Department MODIFY Location VARCHAR2(20)
ALTER TABLE Department ADD Floor NUMBER(2,0)


DESC Department
```
![Alt text](/AssignmentImg/0020.png "student")


Q3: 
```
ALTER TABLE Employee ADD CONSTRAINT emp_ref PRIMARY KEY(Empno)
ALTER TABLE Employee MODIFY Empno NUMBER(3,0)
ALTER TABLE Employee MODIFY ManagerID NUMBER(3,0)
ALTER TABLE Employee MODIFY FirstName VARCHAR2(20) NOT NULL
ALTER TABLE Employee MODIFY LastName VARCHAR2(20)
ALTER TABLE Employee MODIFY UserID VARCHAR2(20)
ALTER TABLE Employee MODIFY deptno NUMBER(2,0)
ALTER TABLE Employee ADD CONSTRAINT emp_fk_ref FOREIGN KEY(deptno) REFERENCES Department(Deptno)
ALTER TABLE Employee MODIFY deptno NUMBER(2,0)
ALTER TABLE Employee MODIFY Salary NUMBER(5,2)
ALTER TABLE Employee MODIFY Salary NUMBER(3,0)
ALTER TABLE Employee MODIFY Designation VARCHAR2(25)

DESC Employee
```
![Alt text](/AssignmentImg/0030.png "student")

Q4:

```
ALTER TABLE Employee ADD HRA NUMBER
ALTER TABLE Employee ADD PF NUMBER

DESC Employee
```
![Alt text](/AssignmentImg/0040.png "student")

Q5:

```
ALTER TABLE Employee MODIFY HRA NUMBER(5,2)
DESC Employee
```
![Alt text](/AssignmentImg/0050.png "student")

Q6
```
ALTER TABLE Employee MODIFY PF NUMBER(5,2)
ALTER TABLE Employee ADD constraint pf_ref CHECK(PF<5000)
DESC Employee
```

![Alt text](/AssignmentImg/0060.png "student")

