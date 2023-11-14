1
SELECT `productLine`,`textDescription` 
FROM `productlines`
2
SELECT `country` 
FROM `customers`
3
SELECT DISTINCT `country` 
FROM `customers`
4
SELECT `productName`,`productCode`,`quantityInStock` 
FROM `products` 
WHERE `quantityInStock` > 9000
5
SELECT `status`,`comments`,`customerNumber` 
FROM `orders` 
WHERE `status` 
IN ("Cancelled","On Hold","Resolved")
6
SELECT `productCode`,`quantityOrdered`,`priceEach` 
FROM `orderdetails` 
WHERE (`quantityOrdered` > 80 OR `priceEach` > 200) 
AND NOT (`quantityOrdered` > 80 AND `priceEach` > 200)
7
SELECT `status` , `comments` , `customerNumber`
FROM `orders`
WHERE `shippedDate` IS NULL
8
SELECT `comments`
FROM `orders` 
WHERE `comments` IS NOT NULL
9
SELECT `productName`, 
ROUND(`buyPrice`*`quantityInStock`,1) 
AS `Wartosc` 
FROM `products`
10
SELECT `customerName` , `city` , `country`
FROM `customers`
WHERE `country`
IN (
SELECT `country`
FROM `customers`
WHERE `city`
IN (
"Oulu", "Herzlia", "Hatfield", "Cowes"
))
11
SELECT `customerName`, `country`,`creditLimit`
FROM `customers`
WHERE `creditLimit` >
ALL(
SELECT `creditLimit`
FROM `customers`
WHERE `country` = "UK")