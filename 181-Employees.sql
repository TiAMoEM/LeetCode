select Name as Employee from Employee e1
where e1.Salary > (select e2.Salary from Employee e2 where e1.ManagerId = e2.Id);

select a.Name as Employee
from Employee as a
inner join Employee as b
on a.ManagerId = b.Id
and a.Salary > b.Salary
