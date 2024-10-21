### Shop Table
```
CREATE TABLE shoptest(
shopid INT PRIMARY KEY,
shopname VARCHAR(20)
)

INSERT ALL
INTO shoptest(shopid,shopname) VALUES (1001,'Amal Stores')
INTO shoptest(shopid,shopname) VALUES (1002,'Jyothi Stores')
INTO shoptest(shopid,shopname) VALUES (1003,'Indira Stores')
SELECT * FROM DUAL

select * FROM shoptest
```
![Alt text](/workshop/img/1001.png "student")

### UNIT TABLE
```
CREATE TABLE unittest(
unitid INT PRIMARY KEY,
unit VARCHAR(10)
)
INSERT ALL
INTO unittest(unitid,unit) VALUES (2001,'Piece')
INTO unittest(unitid,unit) VALUES (2002,'Box pack')
SELECT * FROM DUAL

select * from unittest

```
![Alt text](/workshop/img/1002.png "student")

### ITEM TABLE

```
CREATE TABLE itemtest(
itemid INT PRIMARY KEY,
itemname VARCHAR(20)
)
select * from unittest
INSERT ALL
INTO itemtest(itemid,itemname) VALUES (3001,'Bar-one')
INTO itemtest(itemid,itemname) VALUES (3002,'Kit-kat')
INTO itemtest(itemid,itemname) VALUES (3003,'MilkyBar')
INTO itemtest(itemid,itemname) VALUES (3004,'Munch')

SELECT * FROM DUAL

select * from itemtest

```
![Alt text](/workshop/img/1003.png "student")


### SALES TABLE
```


CREATE TABLE salestest(
salesid INT PRIMARY KEY,
itemid INT,
shopid INT,
quantity INT,
unitid INT,
unitprice INT,
salesdate DATE,
FOREIGN KEY(shopid) REFERENCES shoptest(shopid),
FOREIGN KEY(unitid) REFERENCES unittest(unitid),
FOREIGN KEY(itemid) REFERENCES itemtest(itemid)
)

INSERT ALL
.
.
.
.

INTO salestest(SALESID, ITEMID, SHOPID, QUANTITY, UNITID, UNITPRICE, SALESDATE) VALUES (4012,3001,1001,150,2001,10,'09-15-2018')
INTO salestest(SALESID, ITEMID, SHOPID, QUANTITY, UNITID, UNITPRICE, SALESDATE) VALUES (4013,3002,1001,250,2001,15,'09-15-2018')
INTO salestest(SALESID, ITEMID, SHOPID, QUANTITY, UNITID, UNITPRICE, SALESDATE) VALUES (4014,3004,1001,200,2001,10,'10-10-2018')


SELECT * FROM DUAL

select * from salestest


```

![Alt text](/workshop/img/1004.png "student")

### FINAL OUTPUT

```
select salestest.salesid,itemtest.itemname,shoptest.shopname,salestest.quantity,unittest.unit,salestest.unitprice,salestest.salesdate FROM salestest 
INNER JOIN itemtest
ON salestest.itemid = itemtest.itemid
INNER JOIN shoptest
ON salestest.shopid = shoptest.shopid
INNER JOIN unittest
ON salestest.unitid = unittest.unitid

```


![Alt text](/workshop/img/final.png "student")
