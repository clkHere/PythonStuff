<h1>Company Database Project</h1> 
This project will require that a database be constructed based on the characters from the U.S. TV series "The Office". 

-----
<h2> Company Data Storage Requirements</h2>
Req 1. The company is organized into <b>branches</b>. Each branch has a <b>unique number</b>, a name, and a particular employee who manages it.<br><br>
Req 2. The company makes it’s money by selling to <b>clients</b>. Each client has a name and a <b>unique number</b> to identify it.<br><br>
Req 3. The foundation of the company is it’s <b>employees</b>. Each employee has a name, birthday, sex, salary and a <b>unique number</b>.<br><br>
Req 4. An employee can work for one branch at a time, and each branch will be managed by one of the employees that work there. We’ll also want to keep track of <u>when the current manager started as manager</u>.<br><br>
Req 5. An employee can act as a supervisor for other employees at the branch, an employee may also act as the supervisor for employees at other branches. An employee can have <u>at most one supervisor</u>.<br><br>
Req 6. A branch may handle a number of clients, with each client having a name and a unique number to identify it. A <b>single client</b> may only be handled by <u>one branch at a time</u>.<br><br>
Req 7. Employees can work with clients controlled by their branch to sell them stuff. If nescessary multiple employees can work with the same client. We’ll want to <u>keep track of how many dollars worth of stuff each employee sells to each client they work with</u>.<br><br>
Req 8. Many branches will need to work with <b>suppliers</b> to buy inventory. For each supplier we’ll <u>keep track of their name and the type of product they’re selling the branch</u>. <b>A single supplier may supply products to multiple branches</b>.<br><br>

-----

<h2>My Solution</h2>
  
<ins>Thought Process</ins>:<br><br> 
<b>A.</b> I will need to create at least 5 tables to represent <code>Employees, Branches, Suppliers, Sales by Employees, Clients</code>.<br><br>
<b>B.</b> I'll need to add the <code>branch_id</code> and <code>super_id</code> <b> foriegn keys</b> to the 'Employee' table once the 'Branch' table is created.<br><br>
<b>C.</b> Because of the 'supervisor' criteria, I'll need to insert data by branch, starting with manager data so that I can update <code>super_id</code> and <code>branch_id</code> more efficiently.<br><br>
<b>D.</b> Afterwards, I'll have to insert data by dependencies for the other tables: Supplier -> Client -> Works_With. <br><br>
<b>E.</b> Finally, I'll run some analysis on the database to ensure it's functionality with arbitrary prompts.<br> 
<hr style="border:2px solid gray"></hr>

<h3 align="center">Create Tables (<i>Solutions A & B</i>)</h3>

<br><b>Employee Table</b>
```sql 
-- Creating the Employee table:
CREATE TABLE employee (
  emp_id INT PRIMARY KEY,
  first_name VARCHAR(40),
  last_name VARCHAR(40),
  birth_day DATE,
  sex VARCHAR(1),
  salary INT,
  super_id INT,
  branch_id INT
);
```
| emp_id | first_name | last_name | birth_day | sex | salary | super_id* | branch_id* |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |

<br><b>Branch Table</b>
```sql 
-- Creating the Branch table:
CREATE TABLE branch (
  branch_id INT PRIMARY KEY,
  branch_name VARCHAR(40),
  mgr_id INT,
  mgr_start_date DATE,
  FOREIGN KEY(mgr_id) REFERENCES employee(emp_id) ON DELETE SET NULL
);
```
| branch_id | branch_name | mgr_id | mgr_start_date |  
| :---: | :---: | :---: | :---: |

<br>

```sql
-- Adding the FOREIGN KEYs (branch_id*) & (super_id*)
ALTER TABLE employee
ADD FOREIGN KEY(branch_id)  
REFERENCES branch(branch_id)
ON DELETE SET NULL;

ALTER TABLE employee
ADD FOREIGN KEY(super_id)  
REFERENCES employee(emp_id)
ON DELETE SET NULL;
```


<br><b>Client Table</b>
```sql
-- creating Client table:
CREATE TABLE client (
  client_id INT PRIMARY KEY,
  client_name VARCHAR(40),
  branch_id INT,
  FOREIGN KEY(branch_id) REFERENCES branch(branch_id) ON DELETE SET NULL
);
```
| client_id | client_name | branch_id |   
| :---: | :---: | :---: |

<br><b>Works_With Table</b>
```sql
-- creating Works_With table: 
CREATE TABLE works_with (
  emp_id INT,
  client_id INT,
  total_sales INT,
  PRIMARY KEY(emp_id, client_id),
  FOREIGN KEY(emp_id) REFERENCES employee(emp_id) ON DELETE CASCADE,
  FOREIGN KEY(client_id) REFERENCES client(client_id) ON DELETE CASCADE
);
```
| emp_id | client_id | total_sales |
| :---: | :---: | :---: |

<br><b>Branch Supplier</b>
```sql   
-- creating Branch_Supplier table:
CREATE TABLE branch_supplier (
  branch_id INT,
  supplier_name VARCHAR(40),
  supply_type VARCHAR(40),
  PRIMARY KEY(branch_id, supplier_name),
  FOREIGN KEY(branch_id) REFERENCES branch(branch_id) ON DELETE CASCADE
);
```
| branch_id | supplier_name | supply_type |
| :---: | :---: | :---: |

<hr style="border:2px solid gray"></hr>

<h2 align="center"><b>Inserting Data Pt.1 (<i>Solution C</i>)</b></h2>

<br><b>Corporate Branch</b>
```sql
-- populating corporate branch data:
-- manager information has to complete first to ensure all foreign keys work appropriately:
INSERT INTO employee VALUES(100, 'David', 'Wallace', '1967-11-17', 'M', 250000, NULL, NULL);
INSERT INTO branch VALUES(1, 'Corporate', 100, '2006-02-09');

--update the foreign key
UPDATE employee
SET branch_id = 1
WHERE emp_id = 100;

INSERT INTO employee VALUES(101, 'Jan', 'Levinson', '1961-05-11', 'F', 110000, 100, 1);
```

<br><b>Scranton Branch</b>
```sql
-- populating scranton branch data:
-- manager information has to complete first to ensure all foreign keys work appropriately:
INSERT INTO employee VALUES(102, 'Michael', 'Scott', '1964-03-15', 'M', 75000, 100, NULL);
INSERT INTO branch VALUES(2, 'Scranton', 102, '1992-04-06');

--update the foreign key
UPDATE employee
SET branch_id = 2
WHERE emp_id = 102;

INSERT INTO employee VALUES(103, 'Angela', 'Martin', '1971-06-25', 'F', 63000, 102, 2);
INSERT INTO employee VALUES(104, 'Kelly', 'Kapoor', '1980-02-05', 'F', 55000, 102, 2);
INSERT INTO employee VALUES(105, 'Stanley', 'Hudson', '1958-02-19', 'M', 69000, 102, 2);
```

<br><b>Stamford Branch</b>
```sql
-- populating stamford branch data:
-- manager information has to complete first to ensure all foreign keys work appropriately:
INSERT INTO employee VALUES(106, 'Josh', 'Porter', '1969-09-05', 'M', 78000, 100, NULL);
INSERT INTO branch VALUES(3, 'Stamford', 106, '1998-02-13');

--update the foreign key
UPDATE employee
SET branch_id = 3
WHERE emp_id = 106;

INSERT INTO employee VALUES(107, 'Andy', 'Bernard', '1973-07-22', 'M', 65000, 106, 3);
INSERT INTO employee VALUES(108, 'Jim', 'Halpert', '1978-10-01', 'M', 71000, 106, 3);
```

<b>[Employee Table]</b>
| emp_id | first_name | last_name | birth_day | sex | salary | super_id* | branch_id* |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 100 | David | Wallace | 1967-11-17 | M | 250,000 | NULL | 1 | 
| 101 | Jan | Levinson | 1961-05-11 | F | 110,000 | 100 | 1 | 
| 102 | Michael | Scott | 1964-03-15 | M | 75,000 | 100 | 2 | 
| 103 | Angela | Martin | 1971-06-25 | F | 63,000 | 102 | 2 | 
| 104 | Kelly | Kapoor | 1980-02-05 | F | 55,000 | 102 | 2 | 
| 105 | Stanley | Hudson | 1958-02-19 | M | 69,000 | 102 | 2 |
| 106 | Josh | Porter | 1969-09-05 | M | 78,000 | 100 | 3 |
| 107 | Andy | Bernard | 1973-07-22 | M | 65,000 | 106 | 3 |
| 108 | Jim | Halpert | 1978-10-01 | M | 71,000 | 106 | 3 |

<b>[Branch Table]</b>
| branch_id | branch_name | mgr_id | mgr_start_date |  
| :---: | :---: | :---: | :---: |
| 1 | Corporate | 100 | 2006-02-09 |
| 2 | Scranton | 102 | 1992-04-06 |
| 3 | Stamford | 106 | 1998-02-13 |


<hr style="border:2px solid gray"></hr>

<h2 align="center"><b>Inserting Data Pt.2 (<i>Solution D</i>)</b></h2>

<br><b>Branch Supplier</b>
```sql
-- BRANCH SUPPLIER
INSERT INTO branch_supplier VALUES(2, 'Hammer Mill', 'Paper');
INSERT INTO branch_supplier VALUES(2, 'Uni-ball', 'Writing Utensils');
INSERT INTO branch_supplier VALUES(3, 'Patriot Paper', 'Paper');
INSERT INTO branch_supplier VALUES(2, 'J.T. Forms & Labels', 'Custom Forms');
INSERT INTO branch_supplier VALUES(3, 'Uni-ball', 'Writing Utensils');
INSERT INTO branch_supplier VALUES(3, 'Hammer Mill', 'Paper');
INSERT INTO branch_supplier VALUES(3, 'Stamford Lables', 'Custom Forms');
```

<b>[Branch Supplier Table]</b>
| branch_id | supplier_name | supply_type |
| :---: | :---: | :---: |
| 2 | Hammer Mill | Paper | 
| 2 | Uni-ball | Writing Utensils | 
| 3 | Patriot Paper | Paper | 
| 2 | J.T. Forms & Labels | Custom Forms | 
| 3 | Uni-ball | Writing Utensils | 
| 3 | Hammer Mill | Paper |
| 3 | Stamford Labels | Custom Forms | 

<br><b> Client Table</b>
```sql
-- CLIENT
INSERT INTO client VALUES(400, 'Dunmore Highschool', 2);
INSERT INTO client VALUES(401, 'Lackawana Country', 2);
INSERT INTO client VALUES(402, 'FedEx', 3);
INSERT INTO client VALUES(403, 'John Daly Law, LLC', 3);
INSERT INTO client VALUES(404, 'Scranton Whitepages', 2);
INSERT INTO client VALUES(405, 'Times Newspaper', 3);
INSERT INTO client VALUES(406, 'FedEx', 2);
```

<b>[Client Table]</b>
| client_id | client_name | branch_id |   
| :---: | :---: | :---: |
| 400 | Dunmore Highschool | 2 | 
| 401 | Lackawana County | 2 | 
| 402 | FedEx | 3 | 
| 403 | John Daly Law, LLC | 3 | 
| 404 | Scranton Whitepages | 2 |
| 405 | Times Newspaper | 3 |
| 406 | FedEx | 2 |

<br><b>Works_With Table</b>
```sql
-- WORKS_WITH
INSERT INTO works_with VALUES(105, 400, 55000);
INSERT INTO works_with VALUES(102, 401, 267000);
INSERT INTO works_with VALUES(108, 402, 22500);
INSERT INTO works_with VALUES(107, 403, 5000);
INSERT INTO works_with VALUES(108, 403, 12000);
INSERT INTO works_with VALUES(105, 404, 33000);
INSERT INTO works_with VALUES(107, 405, 26000);
INSERT INTO works_with VALUES(102, 406, 15000);
INSERT INTO works_with VALUES(105, 406, 130000);
```

<b>[Works_With Table]</b>
| emp_id | client_id | total_sales |
| :---: | :---: | :---: |
| 105 | 400 | 55,000 |
| 102 | 401 | 267,000 |
| 108 | 402 | 22,500 |
| 107 | 403 | 5,000 |
| 108 | 403 | 12,000 |
| 105 | 404 | 33,000 |
| 107 | 405 | 26,000 |
| 102 | 406 | 15,000 |
| 105 | 406 | 130,000 |

<hr style="border:2px solid gray"></hr>

<h2 align="center"><b>Testing Functionality in MySQL(<i>Solution D</i>)</b></h2>

| <ins>Find the total number of employees.</ins> | <ins>Find the sum of all employee's salaries.</ins> | <ins>Find any client's that are an LLC.</ins> |
| :---: | :---: | :---: |
| <p align="left">`SELECT COUNT(emp_id)`<br>`FROM employee;`<br><b>COUNT = 8</b></p> | <p align="left">`SELECT SUM(salary)`<br>`FROM employee;`<br><b>SUM = 836000</b></p> | <p align="left">`SELECT *`<br>`FROM client`<br>`WHERE client_name LIKE "%LLC";`<br><b>403 - John Daly Law, LLC - 3</b></p> |

| <ins>Find a list of employee and branch names.</ins> | <ins>Find all the branches and the names of their managers.</ins> |
| :---: | :---: |
| <p align="left">`SELECT first_name`<br>`FROM employee`<br>`UNION`<br>`SELECT branch_name`<br>`FROM branch;`<br>David<br>Jan<br>Michael<br>Angela<br>cont'd...</p> | <p align="left">`SELECT emp_id, first_name, branch_name`<br>`FROM employee`<br>`JOIN branch`<br>`ON emp_id = mgr_id;`<br><br>100--David--Corporate<br>102--Michael--Scranton<br>106--Josh--Stamford</p> |

| <ins>Find names of all employees who have sold over 30,000 to a single client</ins> | <ins>Find all clients who are handled by the branch that Michael Scott manages.</ins> |
| :---: | :---: |
|<p align="left">`SELECT employee.first_name, employee.last_name`<br>`FROM employee`<br>`WHERE employee.emp_id IN (`<br><blockquote align="left">`SELECT works_with.emp_id`<br>`FROM works_with`<br>`WHERE works_with.total_sales > 30000);`</blockquote><br><p align="left"><ins><b>Results:</ins><br>Michael Scott<br>Stanley Hudson</p></b></p> | <p align="left">`SELECT client.client_name`<br>`FROM client`<br>`WHERE client.branch_id = (`<br><blockquote align="left">`SELECT branch.branch_id`<br>`FROM branch`<br>`WHERE branch.mgr_id = 102);`</blockquote><br><p align="left"><ins><b>Results:</ins><br>Dunmore Highschool<br>Lackawana County<br>Scranton Whitepages<br>FedEx</p></b></p>

<h1 align="center"> -- END OF PROJECT -- <h1>
