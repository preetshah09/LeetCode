select cus.name as Customers
from Customers as cus
left join Orders as orde
on cus.id = orde.customerID
where orde.id is NULL