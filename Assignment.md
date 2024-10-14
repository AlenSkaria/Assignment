>ASSIGNMENT
#### Question 1: 
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


#### Question 2:

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


#### Question 3: 
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

#### Question 4:

```
ALTER TABLE Employee ADD HRA NUMBER
ALTER TABLE Employee ADD PF NUMBER

DESC Employee
```
![Alt text](/AssignmentImg/0040.png "student")

#### Question 5:

```
ALTER TABLE Employee MODIFY HRA NUMBER(5,2)
DESC Employee
```
![Alt text](/AssignmentImg/0050.png "student")

#### Question 6
```
ALTER TABLE Employee MODIFY PF NUMBER(5,2)
ALTER TABLE Employee ADD constraint pf_ref CHECK(PF<5000)
DESC Employee
```

![Alt text](/AssignmentImg/0060.png "student")


#### Question 7

```
CREATE TABLE Customer(
Custno NUMBER(3,0),
CustnoName varchar2(20),
Address varchar2(40)
)

DESC Customer


CREATE TABLE Orders(
OrderNo NUMBER(3,0),
custno NUMBER(3,0),
orderdate DATE
)
DESC Orders

CREATE TABLE OrderItem(
ItemID NUMBER(3,0),
OrderNo NUMBER(3,0),
ItemName VARCHAR2(20),
Quantity NUMBER(2,0)
)

DESC OrderItem
```
![Alt text](/AssignmentImg/0070.png "student")
![Alt text](/AssignmentImg/0071.png "student")
![Alt text](/AssignmentImg/0072.png "student")

#### Question 8:
```
ALTER TABLE Customer ADD CONSTRAINT cus_pk PRIMARY KEY(Custno)
DESC Customer
```
![Alt text](/AssignmentImg/0080.png "student")

#### Question 9:
```
ALTER TABLE Orders ADD CONSTRAINT ord_pk PRIMARY KEY(OrderNo)

ALTER TABLE Orders ADD CONSTRAINT ord_fk FOREIGN KEY(custno) REFERENCES Customer(Custno)

DESC Orders 
```
![Alt text](/AssignmentImg/0090.png "student")



#### Question 10:

```
ALTER TABLE OrderItem ADD CONSTRAINT ordIT_pk PRIMARY KEY(ItemID)

ALTER TABLE OrderItem ADD CONSTRAINT ordIT_fk FOREIGN KEY(OrderNo) REFERENCES Orders(OrderNo)

DESC OrderItem
```
![Alt text](/AssignmentImg/1000.png "student")
#### Question 11:
```
ALTER TABLE Customer MODIFY Address VARCHAR2(100)

DESC Customer
```
![Alt text](/AssignmentImg/1001.png "student")



#### Question 12:
```
CREATE TABLE Course(
Courseid VARCHAR2(25),
StreamID VARCHAR2(20),
Description VARCHAR2(200),
Fees NUMBER
)

DESC Course

CREATE TABLE Batch(
BatchID VARCHAR2(30),
CourseID VARCHAR2(5),
BatchName CHAR
)

DESC Batch

CREATE TABLE Students(
StudID VARCHAR2(20),
LastName VARCHAR2(25),
MiddleName VARCHAR2(30),
FirstName VARCHAR2(20),
BatchID VARCHAR2(30),
Grade CHAR
)

DESC Students
```
![Alt text](/AssignmentImg/1012.png "student")
![Alt text](/AssignmentImg/10122.png "student")
![Alt text](/AssignmentImg/10123.png "student")


#### Question 13:
```
ALTER TABLE Course ADD CONSTRAINT pk1 PRIMARY KEY(Courseid)

ALTER TABLE Course ADD Title VARCHAR2(40)

DESC Course

```
![Alt text](/AssignmentImg/1013.png "student")
#### Question 14:

```
ALTER TABLE Batch ADD CONSTRAINT fk FOREIGN KEY(CourseID) REFERENCES Course(Courseid)

DESC Batch 

```
![Alt text](/AssignmentImg/1014.png "student")
#### Question 15:
```
ALTER TABLE Students ADD DOB DATE
ALTER TABLE Students ADD Address VARCHAR2(50)
ALTER TABLE Students ADD City VARCHAR2(20)
ALTER TABLE Students ADD State VARCHAR2(2)
ALTER TABLE Students ADD Zipcode VARCHAR2(9)
ALTER TABLE Students ADD Telephone VARCHAR2(10)
ALTER TABLE Students ADD Fax VARCHAR2(10)
ALTER TABLE Students ADD Email VARCHAR2(30)
ALTER TABLE Students ADD CONSTRAINT pkst PRIMARY KEY(StudID)

DESC Students 
```
![Alt text](/AssignmentImg/10115.png "student")

#### Question 16:
```
ALTER TABLE Students DROP COLUMN MiddleName 

DESC Students 
```
![Alt text](/AssignmentImg/1016.png "student")
#### Question 17:
```
RENAME Students TO Participant

DESC Participant
```
![Alt text](/AssignmentImg/1017.png "student")



