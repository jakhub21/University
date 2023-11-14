-- phpMyAdmin SQL Dump
-- version 3.3.10
-- http://www.phpmyadmin.net
--
-- Host: db.zut.edu.pl
-- Czas wygenerowania: 19 Mar 2023, 09:29
-- Wersja serwera: 1.0.335
-- Wersja PHP: 5.4.16

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Baza danych: `jh50985`
--

-- --------------------------------------------------------

--
-- Struktura tabeli dla  `customers`
--

CREATE TABLE IF NOT EXISTS `customers` (
  `customerNumber` int(11) NOT NULL,
  `customerName` varchar(50) NOT NULL,
  `contactLastName` varchar(50) NOT NULL,
  `conatctFirstName` varchar(50) NOT NULL,
  `phone` varchar(50) NOT NULL,
  `addressLine1` varchar(50) NOT NULL,
  `addressLine2` varchar(50) DEFAULT NULL,
  `city` varchar(50) NOT NULL,
  `state` varchar(50) DEFAULT NULL,
  `postalCode` varchar(16) DEFAULT NULL,
  `country` varchar(50) NOT NULL,
  `creditLimit` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`customerNumber`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

--
-- Zrzut danych tabeli `customers`
--


-- --------------------------------------------------------

--
-- Struktura tabeli dla  `orderdetails`
--

CREATE TABLE IF NOT EXISTS `orderdetails` (
  `order_number` int(11) NOT NULL,
  `product_number` int(11) NOT NULL,
  `quantity` int(11) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  KEY `order_number` (`order_number`),
  KEY `product_number` (`product_number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Zrzut danych tabeli `orderdetails`
--


-- --------------------------------------------------------

--
-- Struktura tabeli dla  `orders`
--

CREATE TABLE IF NOT EXISTS `orders` (
  `order_number` int(11) NOT NULL,
  `order_date` date NOT NULL,
  `customerNumber` int(11) NOT NULL,
  `delivery_type` varchar(50) DEFAULT NULL,
  `comment` text DEFAULT NULL,
  `status` text DEFAULT NULL,
  PRIMARY KEY (`order_number`),
  KEY `customerNumber` (`customerNumber`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Zrzut danych tabeli `orders`
--


-- --------------------------------------------------------

--
-- Struktura tabeli dla  `paymenst`
--

CREATE TABLE IF NOT EXISTS `paymenst` (
  `customerNumber` int(11) NOT NULL,
  `paymentDate` date NOT NULL,
  `amount` decimal(10,2) NOT NULL,
  KEY `customerNumber` (`customerNumber`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Zrzut danych tabeli `paymenst`
--


-- --------------------------------------------------------

--
-- Struktura tabeli dla  `products`
--

CREATE TABLE IF NOT EXISTS `products` (
  `code_product` int(11) NOT NULL,
  `product_Name` varchar(50) DEFAULT NULL,
  `description` text DEFAULT NULL,
  `details` text DEFAULT NULL,
  `amount` int(11) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `manufaktor` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`code_product`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Zrzut danych tabeli `products`
--

INSERT INTO `products` (`code_product`, `product_Name`, `description`, `details`, `amount`, `price`, `manufaktor`) VALUES
(3, 'Monitor LCD 29"', NULL, NULL, 15, 550.00, 'Belinea'),
(7, 'plyta glowna', NULL, NULL, 20, 350.20, 'Assus'),
(9, 'mysz bezprzewodowa', NULL, NULL, 23, 51.00, 'Pro'),
(10, 'pamiec SSD', NULL, NULL, 50, 75.25, 'BIGComp');

--
-- Ograniczenia dla zrzutów tabel
--

--
-- Ograniczenia dla tabeli `orderdetails`
--
ALTER TABLE `orderdetails`
  ADD CONSTRAINT `orderdetails_ibfk_1` FOREIGN KEY (`order_number`) REFERENCES `products` (`code_product`);

--
-- Ograniczenia dla tabeli `orders`
--
ALTER TABLE `orders`
  ADD CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`customerNumber`) REFERENCES `customers` (`customerNumber`);

--
-- Ograniczenia dla tabeli `paymenst`
--
ALTER TABLE `paymenst`
  ADD CONSTRAINT `paymenst_ibfk_1` FOREIGN KEY (`customerNumber`) REFERENCES `customers` (`customerNumber`);
