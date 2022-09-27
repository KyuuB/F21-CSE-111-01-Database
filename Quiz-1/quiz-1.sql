-- SQLite
.headers on

--1
SELECT maker
from Product P, Printer
WHERE Printer.price < 120
AND Printer.color = 1
AND P.model = Printer.model;


--2
SELECT maker
FROM Product
WHERE type = 'pc'
EXCEPT
SELECT maker
FROM Product
WHERE type = 'laptop'
OR type = 'printer';


--3
SELECT maker, MAX(Laptop.price + PC.price)
--, PC.model, Laptop.model, Laptop.price, PC.price
FROM Product P, PC, Laptop
WHERE P.type = 'laptop' 
INTERSECT
SELECT maker, MAX(Laptop.price + PC.price)
--, PC.model, Laptop.model, Laptop.price, PC.price
FROM Product P, PC, Laptop
WHERE P.type = 'pc'


--4
--What laptop screen size are offered in
--at least 2 different models?
SELECT screen
FROM Laptop
GROUP BY 1
having count(*) > 1;

--5
--What laptops are more expensive than
--all the PCs? Print the model and the 
--the price
SELECT Laptop.price, Laptop.model, max(PC.price)
FROM Laptop, PC
GROUP BY 1
HAVING Laptop.price > PC.price

--6
--What makers produce at least a PC or
--Laptop model and at least 2 Printer models

select maker
from Product
where type = 'laptop'
UNION
SELECT maker 
from Product
where type = 'pc'
INTERSECT 
SELECT maker
FROM Product
GROUP BY 1
having count(type = 'printer') > 1

