Q1:

```
INSERT INTO employee(empNo,managerid,firstname,lastname,userid,deptno,salary,commission,joiningdate,designation,hra,pf) VALUES (110,201,'Alent','s','w',10,4500,250,'11-12-1989','manager',23,25)

SELECT firstname AS "Employee Name",(((Salary + commission + HRA + PF) * 12 )* 0.30) AS "Annual Tax" FROM Employee;

select * from Employee
```

![Alt text](/ASSIGNMENT%203/img/1.png "student")


Q2
```
```
Q3
```
```
Q4
```
select * from Employee where firstname LIKE 'A%e%t'
```
![Alt text](/ASSIGNMENT%203/img/4.png "student")


Q5
```
INSERT INTO employee(empNo,managerid,firstname,lastname,userid,deptno,salary,commission,joiningdate,designation,hra,pf) VALUES (111,201,'Sam','shyam','pi',10,45000,250,'11-12-2019','Associate',23,25)

select * from Employee where joiningdate > '01/01/1998' AND SALARY > 25000
```
![Alt text](/ASSIGNMENT%203/img/5.png "student")


Q6

```
select * from employee where commission IS NULL
```
![Alt text](/ASSIGNMENT%203/img/6.png "student")


Q7
```
SELECT 'Festival offer' AS Offer_Heading,productname || ' costs ' || ROUND(priceperunit * 0.9) || ' after discount' AS Product_Details FROM PRODUCT;
```
![Alt text](/ASSIGNMENT%203/img/7.png "student")

Q8
```
SELECT * FROM PRODUCT WHERE priceperunit > 50 AND priceperunit < 100;
```
![Alt text](/ASSIGNMENT%203/img/8.png "student")

Q9
```
SELECT * FROM PRODUCT WHERE priceperunit BETWEEN 50 AND 100;
```
![Alt text](/ASSIGNMENT%203/img/9.png "student")

Q10

```
SELECT DISTINCT designation FROM employee
```

![Alt text](/ASSIGNMENT%203/img/10.png "student")

