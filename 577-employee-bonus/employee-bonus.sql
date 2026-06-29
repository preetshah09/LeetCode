# Write your MySQL query statement below
select emp.name, bon.bonus
from Employee as emp
left join Bonus as bon
on emp.empID = bon.empID
where bon.bonus<1000 or bon.bonus is NULL