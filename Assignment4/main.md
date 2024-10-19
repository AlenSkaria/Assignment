Q1: 
```
INSERT INTO employee(empNo,managerid,firstname,lastname,userid,deptno,salary,commission,joiningdate,designation,hra,pf) VALUES (201,205,'akhil','q','p',10,45000,250,'11-12-1989','manager',23,25)


SELECT DISTINCT e1.FirstName || ' ' || e1.LastName AS "Manager Name"
FROM employee e1
    JOIN employee e2 ON e1.EmpNo = e2.ManagerID;
```
![Alt text](/Assignment4/img/1.png "student")

Q3: 
```
SELECT 'Every Year ' || e.FirstName || ' ' || e.LastName || ' of ' || d.Deptname || ' department earns amount ' || ((e.Salary + e.HRA + e.PF) * 12) AS "Annual income Report"
FROM employee e
JOIN Department d 
ON e.Deptno = d.Deptno;
```
![Alt text](/Assignment4/img/2.png "student")


Q5:
```
SELECT department.deptname, employee.firstname 
FROM Employee 
JOIN Department 
ON Employee.DeptNo = Department.DeptNo
ORDER BY Department.DeptName ASC,Employee.firstname DESC;  
```
![Alt text](/Assignment4/img/5.png "student")

Q6: 
```
select employee.firstname, department.deptname 
FROM employee
JOIN department 
ON Employee.DeptNo = Department.DeptNo
WHERE deptname IN ('Toy','Shoe')

```
![Alt text](/Assignment4/img/6.png "student")


Q7:

```
INSERT INTO employee(empNo,managerid,firstname,lastname,userid,deptno,salary,commission,joiningdate,designation,hra,pf) VALUES (112,110,'midhun','q','p',13,4500,250,'11-12-1989','sales',21,25)

INSERT INTO employee(empNo,managerid,firstname,lastname,userid,deptno,salary,commission,joiningdate,designation,hra,pf) VALUES (113,110,'jerry','s','p',14,4100,250,'11-16-1997','sales',21,25)


SELECT employee.firstname || ', ' ||  department.deptname AS "EMPLOYEE AND DEPARTMENT"
FROM employee 
JOIN department 
ON Employee.DeptNo = Department.DeptNo
```
![Alt text](/Assignment4/img/7.png "student")


Q8: 
```
SELECT Employee.FirstName,Employee.Designation,Department.Deptno,Department.Deptname
FROM Employee
JOIN Department ON Employee.Deptno = Department.Deptno
WHERE Department.LOCATION='DALLAS';
```

![Alt text](/Assignment4/img/8.png "student")
Q9
```
SELECT 
    e1.FirstName || ' ' || e1.LastName AS "Employee Name", 
    e2.FirstName || ' ' || e2.LastName AS "Manager Name"
FROM 
    Employee e1
    LEFT JOIN Employee e2 
        ON e1.ManagerID = e2.Empno;
```
![Alt text](/Assignment4/img/9.png "student")


Q10
```
SELECT 
    e1.FirstName || ' ' || e1.LastName AS "Employee Name", 
    e1.ManagerID AS "Manager Number", 
    CASE 
        WHEN e2.FirstName IS NOT NULL THEN e2.FirstName || ' ' || e2.LastName
        ELSE 'No Manager'
    END AS "Manager Name"
FROM 
    Employee e1
LEFT JOIN 
    Employee e2 ON e1.ManagerID = e2.Empno;
```
![Alt text](/Assignment4/img/10.png "student")




Q11
```
SELECT 
    e1.FirstName  AS "Employee Name", 
    e1.Deptno AS "Department Number", 
    e2.FirstName  AS "Colleague"
FROM 
    Employee e1
JOIN 
    Employee e2 ON e1.Deptno = e2.Deptno
WHERE 
    e1.FirstName = 'Aiden'
AND e1.FirstName <> e2.FirstName; 
```
![Alt text](/Assignment4/img/11.png "student")

    
    
Q12
```
SELECT DISTINCT 
    e.designation AS "Job Title", 
    d.Location AS "Location"
FROM 
    Employee e
JOIN 
    Department d 
ON e.DeptNo = d.DeptNo
WHERE 
    e.DeptNo = 10;
```
![Alt text](/Assignment4/img/12.png "student")


Q13:
```
SELECT participant.firstname, course.title 
FROM participant 
JOIN batch 
ON participant.batchid = batch.batchid 
JOIN course 
ON batch.courseid = course.courseid
```
![Alt text](/Assignment4/img/13.png "student")


Q14:
```
SELECT participant.firstname, batch.batchname 
FROM participant 
JOIN batch 
ON participant.batchid = batch.batchid 
```

![Alt text](/Assignment4/img/14.png "student")

Q15
```
SELECT participant.firstname, course.title 
FROM batch 
LEFT JOIN participant 
ON participant.batchid = batch.batchid 
INNER JOIN course 
ON batch.courseid = course.courseid
```
![Alt text](/Assignment4/img/15.png "student")


Q16
```
SELECT 
    c.custno AS "Customer Name", 
    o.orderdate AS "Order Date", 
    i.itemname AS "Item Ordered"
FROM 
    CUSTOMER c
JOIN 
    ORDERS o ON c.custno = o.custno
JOIN 
    ORDERITEM i ON o.orderno = i.orderno;
```

![Alt text](/Assignment4/img/16.png "student")
