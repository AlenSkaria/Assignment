Q1 :

```
SELECT empno, firstname,lastname,salary,
concat(substr(firstname,1,1),substr(lastname,1,7)) AS "user id" FROM employee
```
![Alt text](/Assignment5/images/1.png "student")

Q2 :

```
SELECT employee.DEPTNO,employee.DESIGNATION,MIN(employee.salary) AS "Minimum salary" 
FROM employee 
GROUP BY employee.DEPTNO,employee.DESIGNATION 
HAVING MIN(employee.salary)> 1000

```

![Alt text](/Assignment5/images/2.png "student")
