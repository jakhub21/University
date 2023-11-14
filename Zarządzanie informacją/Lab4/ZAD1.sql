ZAD1
SELECT `email` 
FROM `employees` 
ORDER BY `email`

ZAD2
SELECT `productName`,`buyPrice` 
FROM `products` 
ORDER BY `buyPrice` DESC

ZAD3
SELECT MIN(`buyPrice`) 
FROM `products`

ZAD4
SELECT MAX(`MSRP`) 
FROM `products`

ZAD5
SELECT SUM(`amount`)
FROM `payments`

ZAD6
SELECT SUM(`priceEach`*`quantityOrdered`) 
FROM `orderdetails` 

ZAD7
SELECT SUM(`buyPrice`) 
FROM `products` 
WHERE `productLine` = "Classic Cars"

ZAD8
SELECT COUNT( * )
FROM `products`
WHERE `buyPrice` >50

ZAD9
SELECT COUNT( * )
FROM `customers`
WHERE `country`
IN (
'USA', 'UK', 'Australia'
)

ZAD10
SELECT COUNT( DISTINCT `country` )
FROM `customers`

ZAD11
SELECT COUNT( * ) , `country`
FROM `customers`
GROUP BY `country`

ZAD12
SELECT `productLine` , COUNT( * )
FROM `products`
WHERE `buyPrice` <30
GROUP BY `productLine`

ZAD13
SELECT `customerNumber` , SUM( `amount` )
FROM `payments`
GROUP BY `customerNumber`
ORDER BY SUM( `amount` ) DESC

ZAD14
SELECT `productLine` 
FROM `products`
GROUP BY `productLine`
HAVING SUM( `buyPrice` ) >1000

ZAD15
SELECT `productScale` , COUNT( * )
FROM `products`
GROUP BY `productScale`
HAVING COUNT( `productScale` ) >=10
ORDER BY COUNT( `productScale` ) 

ZAD16
SELECT COUNT( * )
FROM `customers`
WHERE `country`
IN (
SELECT `country`
FROM `offices`
)

ZAD17
SELECT `country` , COUNT( * )
FROM `customers`
WHERE `country`
IN (
SELECT `country`
FROM `offices`
)
GROUP BY `country`