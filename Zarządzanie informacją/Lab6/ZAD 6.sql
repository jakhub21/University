ZAD 1 
SELECT `firstName` , `lastName` , `email` , (
SELECT city
FROM `offices`
WHERE `offices`.`officeCode` = `employees`.`officeCode`
) AS city
FROM `employees`

ZAD2
SELECT `firstName` , `lastName` , `email`
FROM `employees`
WHERE (
SELECT city
FROM `offices`
WHERE `offices`.`officeCode` = `employees`.`officeCode`
) = "Sydney"

ZAD3
SELECT `customerName` , (
SELECT `email`
FROM `employees` AS e
WHERE e.`employeeNumber` = c.`salesRepEmployeeNumber`
) AS salesRepEmail
FROM `customers` AS c

ZAD4
SELECT `productName` , (
`MSRP` - `buyPrice`
) AS roznica
FROM `products`
ORDER BY roznica DESC

ZAD4 A
SELECT `productName` , roznica
FROM (

SELECT `productName` , (
`MSRP` - `buyPrice`
) AS roznica
FROM `products`
) 
WHERE roznica >50
ORDER BY roznica DESC

ZAD5
SELECT `customerName` , (
SELECT SUM( `amount` )
FROM `payments`
WHERE `customers`.`customerNumber` = `payments`.`customerNumber`
) AS suma
FROM `customers`

ZAD5 A
SELECT *
FROM (
SELECT `customerName` , (
SELECT SUM( `amount` )
FROM `payments`
WHERE `customers`.`customerNumber` = `payments`.`customerNumber`
) AS suma
FROM `customers`
) AS a
WHERE a.suma >100000
ORDER BY a.suma

ZAD6
SELECT `contactLastName`
FROM `customers`
UNION ALL
SELECT `lastName`
FROM `employees`

ZAD6 A
SELECT `contactLastName` , COUNT( * )
FROM `customers`
GROUP BY `customerNumber`
UNION ALL
SELECT `lastName` , COUNT( * )
FROM `employees`
GROUP BY `employeeNumber`

ZAD6 B
SELECT `contactLastName` , COUNT( * )
FROM `customers`
GROUP BY `contactLastName`
HAVING COUNT( * ) >1
UNION ALL
SELECT `lastName` , COUNT( * )
FROM `employees`
GROUP BY `lastName`
HAVING COUNT( * ) >1

ZAD6 C

