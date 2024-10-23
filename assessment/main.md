```
CREATE TABLE category(
cID INT PRIMARY KEY,
cName VARCHAR(50),
DayR NUMBER(10,2),
HrR NUMBER(10,2)    
);

desc category
```

```
CREATE TABLE rooms(
rID INT PRIMARY KEY,
rNo INT,
cID INT, 
rate NUMBER(10,2),  
FOREIGN KEY (cid) REFERENCES category(cid)
);
```
```
CREATE TABLE Customers (
custID INT PRIMARY KEY,
name VARCHAR(20),
phone NUMBER
);
```
```
CREATE TABLE Rates(
RateID INT PRIMARY KEY,
rID INT,
Tax NUMBER(10, 2),
HKCharge NUMBER(10, 2),
Misc NUMBER(10, 2) DEFAULT 0,
FOREIGN KEY (rID) REFERENCES Rooms(rID)
);
```
```
CREATE TABLE Bookings (
BookingID INT PRIMARY KEY,
CustID INT,
rID INT,
BookingDate DATE,
OccupancyDate DATE,
AdvanceReceived DECIMAL(10, 2),
noOfDays INT,
FOREIGN KEY (custID) REFERENCES Customers(custID),
FOREIGN KEY (rID) REFERENCES Rooms(rID)
);

desc category
```
```
INSERT ALL
INTO category (cID, cName, DayR, HrR) VALUES (1001, 'Single', 1500, NULL)
INTO category (cID, cName, DayR, HrR) VALUES (1002, 'Double', 2000, NULL)
INTO category (cID, cName, DayR, HrR) VALUES (1003, 'Suite', 3000, NULL)
INTO category (cID, cName, DayR, HrR) VALUES (1004, 'Convention Hall', NULL, 500)
INTO category (cID, cName, DayR, HrR) VALUES (1005, 'Ball Room', NULL, 700)
SELECT * FROM DUAL

select * from category

```
```
INSERT ALL
INTO rooms (rID, rNo, cID, rate) VALUES (2001, 10011, 1001, 1000)
INTO rooms (rID, rNo, cID, rate) VALUES (2002, 10012, 1001, 1100)
INTO rooms (rID, rNo, cID, rate) VALUES (2003, 10021, 1002, 2000)
INTO rooms (rID, rNo, cID, rate) VALUES (2004, 10022, 1002, 2100)
INTO rooms (rID, rNo, cID, rate) VALUES (2005, 10031, 1003, 3000)
INTO rooms (rID, rNo, cID, rate) VALUES (2006, 10032, 1003, 3100)
INTO rooms (rID, rNo, cID, rate) VALUES (2007, 10041, 1004, 700)
INTO rooms (rID, rNo, cID, rate) VALUES (2008, 10042, 1004, 700)
INTO rooms (rID, rNo, cID, rate) VALUES (2009, 10051, 1005, 200)
INTO rooms (rID, rNo, cID, rate) VALUES (2010, 10052, 1005, 500)
SELECT * FROM DUAL

select * from rooms
```
```
desc customers
INSERT ALL
INTO Customers (custID,name,phone) VALUES (3001, 'Alonn',9934567890)
INTO Customers (custID,name,phone) VALUES (3002, 'Aiden',9912545478)
INTO Customers (custID,name,phone) VALUES (3003, 'Susan',9784541225)
SELECT * FROM DUAL;

select * from customers

```
```
desc rates



INSERT ALL
INTO Rates (RateID, rID, Tax, HKCharge, Misc) VALUES (4001, 2001, 150.00, 50.00, 0)
INTO Rates (RateID, rID, Tax, HKCharge, Misc) VALUES (4002, 2002, 200.00, 60.00, 0)
INTO Rates (RateID, rID, Tax, HKCharge, Misc) VALUES (4003, 2009, 300.00, 70.00, 0)
INTO Rates (RateID, rID, Tax, HKCharge, Misc) VALUES (4004, 2004, 50.00, 20.00, 0)
INTO Rates (RateID, rID, Tax, HKCharge, Misc) VALUES (4005, 2007, 70.00, 30.00, 0)
SELECT * FROM DUAL

select * FROM rates
```
```

INSERT ALL
INTO Bookings (BookingID, CustID, rID, BookingDate, OccupancyDate, advance, noOfDays) VALUES (5001, 3001, 2003, SYSDATE, '10-25-2024', 200.00, 1)
INTO Bookings (BookingID, CustID, rID, BookingDate, OccupancyDate, advance, noOfDays) VALUES (5002, 3002, 2002, SYSDATE, SYSDATE, 500.00, 4)
INTO Bookings (BookingID, CustID, rID, BookingDate, OccupancyDate, advance, noOfDays) VALUES (5003, 3003, 2004, SYSDATE, SYSDATE, 300.00, 5)
SELECT * FROM DUAL;

select * FROM Bookings
```



### 1
```
SELECT category.cName AS ROOMS, rooms.rNo, rooms.rate AS Rate
FROM rooms
INNER JOIN category 
ON rooms.cID = category.cID
ORDER BY category.cName, rooms.rNo;
```

![Alt text](/assessment/img/1.png "student")
### 2 
```
select * from rooms
select * from category
select * from bookings

SELECT rooms.rNo, category.cname as "Room type"
FROM rooms
INNER JOIN bookings
ON rooms.rID = bookings.rID
INNER JOIN category
ON rooms.cid = category.cid
WHERE bookings.OccupancyDate BETWEEN SYSDATE AND SYSDATE + 2;
```

![Alt text](/assessment/img/2.png "student")

### 3 
```
SELECT rooms.rNo, category.cname as "Room type",rooms.rate
FROM rooms
INNER JOIN category
ON rooms.cid = category.cid
ORDER BY rate ASC;

```
![Alt text](/assessment/img/3.png "student")
### 4
```
SELECT rooms.rNo, category.cname as "Room type",rooms.rate
FROM rooms
INNER JOIN category
ON rooms.cid = category.cid
WHERE rate > 2000
ORDER BY rate DESC;
```
![Alt text](/assessment/img/4.png "student")
### 5

```
SELECT SUM(rate) AS "Total Rate"
FROM rooms;
```
![Alt text](/assessment/img/5.png "student")

### 6
```
SELECT category.cName AS "Category Name", rooms.rNo AS "Room Number",rooms.rate,bookings.advance
FROM 
rooms
INNER JOIN 
category ON rooms.cID = category.cID
INNER JOIN 
Bookings ON rooms.rID = bookings.rID
WHERE 
bookings.advance>0
ORDER BY 
category.cName, rooms.rNo;
```
![Alt text](/assessment/img/6.png "student")
### 7
```
select * from bookings
INSERT INTO Bookings (BookingID, CustID, rID, BookingDate, OccupancyDate, advance, noOfDays) VALUES (5004, 3001, 2002, SYSDATE, '10-24-2024', 200.00, 1)

SELECT rooms.rNo, category.cName
FROM rooms
INNER JOIN Bookings 
ON rooms.rID = bookings.rID
INNER JOIN category
category ON rooms.cID = category.cID
WHERE bookings.OccupancyDate BETWEEN '10-20-2024' AND '10-24-2024'
```
![Alt text](/assessment/img/7.png "student")
### 8
```
select * from customers
INSERT INTO customers (custID,name,phone) VALUES (3004, 'JOHN',9975421890)
select * from bookings
INSERT INTO Bookings (BookingID, CustID, rID, BookingDate, OccupancyDate, advance, noOfDays) VALUES (5005, 3004, 2005, SYSDATE, '10-25-2024', 200.00, 1)


SELECT customers.*
FROM customers
INNER JOIN bookings 
ON customers.custID = bookings.custID
INNER JOIN rooms 
ON bookings.rID = rooms.rID
INNER JOIN category 
ON rooms.cID = category.cID
WHERE customers.name LIKE '%JOHN%' AND category.cName = 'Suite';
```

![Alt text](/assessment/img/8.png "student")
### 9
```
SELECT 
rooms.rID, 
rooms.rNo, 
rooms.rate , 
category.cName
FROM 
rooms
INNER JOIN 
category 
ON rooms.cID = category.cID
WHERE 
category.cName = 'Suite' 
ORDER BY 
rooms.rNo ASC;
```
![Alt text](/assessment/img/9.png "student")
### 10
```
INSERT INTO rooms (rID, rNo, cID, rate) VALUES (2011, 10013, 1001, 1000)
select * from rooms

SELECT category.cName AS "Category", 
COUNT(rooms.rID) AS "Count"
FROM 
category 
INNER JOIN 
rooms 
ON category.cID = rooms.cID
GROUP BY 
category.cName
```
![Alt text](/assessment/img/10.png "student")
### 11
```
SELECT rNo, rate
FROM rooms
ORDER BY rate DESC;
```

![Alt text](/assessment/img/11.png "student")
### 12
```
SELECT rooms.rNo
FROM rooms
LEFT JOIN bookings 
ON rooms.rID = bookings.rID
WHERE bookings.rID IS NULL;
```

![Alt text](/assessment/img/12.png "student")

### 13
```
INSERT INTO Customers (custID,name,phone) VALUES (3005, 'Ahana',7545215485)
select * from bookings
INSERT INTO Bookings (BookingID, CustID, rID, BookingDate, OccupancyDate, advance, noOfDays) VALUES (5006, 3005, 2002, SYSDATE, '10-24-2024', 200.00, 1)


SELECT customers.*
FROM customers 
INNER JOIN bookings  
ON customers.custID = bookings.custID
WHERE customers.name LIKE 'Ah%' AND bookings.Advance > 0;
```
![Alt text](/assessment/img/13.png "student")

### 14
```
SELECT rNo, rate
FROM rooms
WHERE rate < 1000
ORDER BY rate DESC;
```
![Alt text](/assessment/img/14.png "student")
### 15

```
SELECT SUM(rate) AS "Total Rate"
FROM rooms;
```
![Alt text](/assessment/img/15.png "student")