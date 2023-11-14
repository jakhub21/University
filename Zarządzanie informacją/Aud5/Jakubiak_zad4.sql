-- phpMyAdmin SQL Dump
-- version 3.3.10
-- http://www.phpmyadmin.net
--
-- Host: db.zut.edu.pl
-- Czas wygenerowania: 24 Maj 2023, 19:31
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
-- Struktura tabeli dla  `DetaleZamowien_2NF`
--

CREATE TABLE IF NOT EXISTS `DetaleZamowien_2NF` (
  `NumerZam` int(11) NOT NULL,
  `idProdukt` int(11) NOT NULL,
  `Ilosc` int(11) DEFAULT NULL,
  PRIMARY KEY (`NumerZam`,`idProdukt`),
  KEY `idProdukt` (`idProdukt`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

--
-- Zrzut danych tabeli `DetaleZamowien_2NF`
--

INSERT INTO `DetaleZamowien_2NF` (`NumerZam`, `idProdukt`, `Ilosc`) VALUES
(1, 1, 4),
(2, 2, 4),
(3, 2, 4),
(4, 3, 1),
(5, 4, 1);

-- --------------------------------------------------------

--
-- Struktura tabeli dla  `DetaleZamowien_3NF`
--

CREATE TABLE IF NOT EXISTS `DetaleZamowien_3NF` (
  `NumDetal` int(11) NOT NULL,
  `NumerZam` int(11) DEFAULT NULL,
  `idProdukt` int(11) DEFAULT NULL,
  `Ilosc` int(11) DEFAULT NULL,
  PRIMARY KEY (`NumDetal`),
  KEY `NumerZam` (`NumerZam`),
  KEY `idProdukt` (`idProdukt`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Zrzut danych tabeli `DetaleZamowien_3NF`
--

INSERT INTO `DetaleZamowien_3NF` (`NumDetal`, `NumerZam`, `idProdukt`, `Ilosc`) VALUES
(1, 1, 1, 4),
(2, 2, 2, 4),
(3, 3, 2, 4),
(4, 4, 3, 2),
(5, 5, 4, 2);

-- --------------------------------------------------------

--
-- Struktura tabeli dla  `Klient_2NF`
--

CREATE TABLE IF NOT EXISTS `Klient_2NF` (
  `NumerKlienta` int(11) NOT NULL,
  `NazwaKlienta` varchar(100) DEFAULT NULL,
  `Adres` varchar(100) DEFAULT NULL,
  `KodPocztowy` varchar(10) DEFAULT NULL,
  `Miejscowosc` varchar(100) DEFAULT NULL,
  `Wojewodztwo` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`NumerKlienta`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Zrzut danych tabeli `Klient_2NF`
--

INSERT INTO `Klient_2NF` (`NumerKlienta`, `NazwaKlienta`, `Adres`, `KodPocztowy`, `Miejscowosc`, `Wojewodztwo`) VALUES
(1, 'Jan Kowalski', 'ul. Jana Pawła 12', '61-600', 'Poznań', 'Wielkopolskie'),
(2, 'Anna Dymna', 'ul. Staszica 1', '30-600', 'Kraków', 'Małopolskie'),
(3, 'Piotr Wawrzyniak', 'ul. Niepodległości 1', '30-600', 'Kraków', 'Małopolskie'),
(4, 'Jan Kowalski', 'ul. Poznańska 8', '21-120', 'Wrocław', 'Dolnośląskie');

-- --------------------------------------------------------

--
-- Struktura tabeli dla  `Klient_3NF`
--

CREATE TABLE IF NOT EXISTS `Klient_3NF` (
  `NumerKlienta` int(11) NOT NULL,
  `NazwaKlienta` varchar(100) DEFAULT NULL,
  `Adres` varchar(100) DEFAULT NULL,
  `KodPocztowy` varchar(10) DEFAULT NULL,
  `Miejscowosc` varchar(100) DEFAULT NULL,
  `Wojewodztwo` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`NumerKlienta`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Zrzut danych tabeli `Klient_3NF`
--

INSERT INTO `Klient_3NF` (`NumerKlienta`, `NazwaKlienta`, `Adres`, `KodPocztowy`, `Miejscowosc`, `Wojewodztwo`) VALUES
(1, 'Jan Kowalski', 'ul. Jana Pawła 12', '61-600', 'Poznań', 'Wielkopolskie'),
(2, 'Anna Dymna', 'ul. Staszica 1', '30-600', 'Kraków', 'Małopolskie'),
(3, 'Piotr Wawrzyniak', 'ul. Niepodległości 1', '30-600', 'Kraków', 'Małopolskie'),
(4, 'Jan Kowalski', 'ul. Poznańska 8', '21-120', 'Wrocław', 'Dolnośląskie');

-- --------------------------------------------------------

--
-- Struktura tabeli dla  `Produkty_2NF`
--

CREATE TABLE IF NOT EXISTS `Produkty_2NF` (
  `idProdukt` int(11) NOT NULL,
  `Produkt` varchar(50) DEFAULT NULL,
  `CenaZaSztuke` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`idProdukt`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Zrzut danych tabeli `Produkty_2NF`
--

INSERT INTO `Produkty_2NF` (`idProdukt`, `Produkt`, `CenaZaSztuke`) VALUES
(1, 'Opony 205 R16', 300.00),
(2, 'Alufelgi Silver ', 550.00),
(3, 'Komplet żarówek', 80.00),
(4, 'Trójkąt ostrzegawczy', 15.00);

-- --------------------------------------------------------

--
-- Struktura tabeli dla  `Produkty_3NF`
--

CREATE TABLE IF NOT EXISTS `Produkty_3NF` (
  `idProdukt` int(11) NOT NULL,
  `Produkt` varchar(50) DEFAULT NULL,
  `CenaZaSztuke` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`idProdukt`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Zrzut danych tabeli `Produkty_3NF`
--

INSERT INTO `Produkty_3NF` (`idProdukt`, `Produkt`, `CenaZaSztuke`) VALUES
(1, 'Opony 205 R16', 300.00),
(2, 'Alufelgi Silver ', 550.00),
(3, 'Komplet żarówek', 80.00),
(4, 'Trójkąt ostrzegawczy', 15.00);

-- --------------------------------------------------------

--
-- Struktura tabeli dla  `Zamowienia_2NF`
--

CREATE TABLE IF NOT EXISTS `Zamowienia_2NF` (
  `NumerZam` int(11) NOT NULL,
  `NumerKlienta` int(11) DEFAULT NULL,
  `DataZamowienia` date DEFAULT NULL,
  PRIMARY KEY (`NumerZam`),
  KEY `NumerKlienta` (`NumerKlienta`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Zrzut danych tabeli `Zamowienia_2NF`
--

INSERT INTO `Zamowienia_2NF` (`NumerZam`, `NumerKlienta`, `DataZamowienia`) VALUES
(1, 1, '2012-01-02'),
(2, 2, '2012-03-22'),
(3, 3, '2012-03-22'),
(4, 1, '2012-10-22'),
(5, 4, '2012-05-22');

-- --------------------------------------------------------

--
-- Struktura tabeli dla  `Zamowienia_3NF`
--

CREATE TABLE IF NOT EXISTS `Zamowienia_3NF` (
  `NumerZam` int(11) NOT NULL,
  `NumerKlienta` int(11) DEFAULT NULL,
  `DataZamowienia` date DEFAULT NULL,
  PRIMARY KEY (`NumerZam`),
  KEY `NumerKlienta` (`NumerKlienta`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Zrzut danych tabeli `Zamowienia_3NF`
--

INSERT INTO `Zamowienia_3NF` (`NumerZam`, `NumerKlienta`, `DataZamowienia`) VALUES
(1, 1, '2012-01-02'),
(2, 2, '2012-03-22'),
(3, 3, '2012-03-22'),
(4, 1, '2012-10-22'),
(5, 4, '2012-05-22');

-- --------------------------------------------------------

--
-- Struktura tabeli dla  `Zamowienia_UNF`
--

CREATE TABLE IF NOT EXISTS `Zamowienia_UNF` (
  `NumerZam` int(11) DEFAULT NULL,
  `NazwaKlienta` varchar(100) DEFAULT NULL,
  `AdresKlienta` varchar(100) DEFAULT NULL,
  `DataZamowienia` date DEFAULT NULL,
  `SzczegolyZamowienia` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Zrzut danych tabeli `Zamowienia_UNF`
--

INSERT INTO `Zamowienia_UNF` (`NumerZam`, `NazwaKlienta`, `AdresKlienta`, `DataZamowienia`, `SzczegolyZamowienia`) VALUES
(101, 'Jan Kowalski', 'ul. Jana Pawła 12, 61-600 Poznań, woj. Wielkopolskie', '2012-01-02', 'Opony 205 R16 4szt, koszt 1200 PLN'),
(102, 'Anna Dymna', 'ul. Staszica 1, 30-600 Kraków, Małopolska', '2012-03-22', 'Alufelgi Silver 4 szt, koszt 2200 PLN'),
(103, 'Piotr Wawrzyniak', 'al. Niepodległości 1, 30-600 Kraków, woj. Małopolskie', '2012-03-22', 'Alufelgi Silver 4 szt, koszt 2200 PLN'),
(104, 'Jan Kowalski', 'ul. Jana Pawła 12, 61-600 Poznań, woj. Wielkopolskie', '2012-10-22', 'Komplet żarówek, koszt 80 PLN'),
(105, 'Jan Kowalski', 'ul. Poznańska 8, 21-120 Wrocław, Dolnośląskie', '2012-05-22', 'Trójkąt ostrzegawczy 1szt, koszt 15 PLN');

-- --------------------------------------------------------

--
-- Struktura tabeli dla  `Zamowienie_1NF`
--

CREATE TABLE IF NOT EXISTS `Zamowienie_1NF` (
  `NumerZam` int(11) DEFAULT NULL,
  `NazwaKlienta` varchar(50) DEFAULT NULL,
  `Adres` varchar(100) DEFAULT NULL,
  `KodPocztowy` varchar(10) DEFAULT NULL,
  `Miejscowosc` varchar(100) DEFAULT NULL,
  `Wojewodztwo` varchar(100) DEFAULT NULL,
  `DataZamowienia` date DEFAULT NULL,
  `Produkt` varchar(50) DEFAULT NULL,
  `Ilosc` int(11) DEFAULT NULL,
  `Koszt` decimal(10,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Zrzut danych tabeli `Zamowienie_1NF`
--

INSERT INTO `Zamowienie_1NF` (`NumerZam`, `NazwaKlienta`, `Adres`, `KodPocztowy`, `Miejscowosc`, `Wojewodztwo`, `DataZamowienia`, `Produkt`, `Ilosc`, `Koszt`) VALUES
(101, 'Jan Kowalski', 'ul. Jana Pawła 12', '61-600', 'Poznań', 'woj. Wielkopolskie', '2012-01-02', 'Opony 205 R16', 4, 1200.00),
(102, 'Anna Dymna', 'ul. Staszica 1', '30-600', 'Kraków', 'Małopolskie', '2012-03-22', 'Alufelgi\r\nSilver', 4, 2200.00),
(103, 'Piotr Wawrzyniak', 'al. Niepodległości 1', '30-600', 'Kraków', 'woj. Małopolskie', '2012-03-22', 'Alufelgi Silver', 4, 2200.00),
(104, 'Jan Kowalski', 'ul. Jana Pawła 12', '61-600', 'Poznań', 'woj. Wielkopolskie', '2012-10-22', 'Komplet żarówek', 1, 80.00),
(105, 'Jan Kowalski', 'ul. Poznańska 8', '21-120', 'Wrocław', 'Dolnośląskie', '2012-05-22', 'Trójkąt ostrzegawczy', 1, 15.00);

--
-- Ograniczenia dla zrzutów tabel
--

--
-- Ograniczenia dla tabeli `DetaleZamowien_2NF`
--
ALTER TABLE `DetaleZamowien_2NF`
  ADD CONSTRAINT `DetaleZamowien_2NF_ibfk_1` FOREIGN KEY (`NumerZam`) REFERENCES `Zamowienia_2NF` (`NumerZam`),
  ADD CONSTRAINT `DetaleZamowien_2NF_ibfk_2` FOREIGN KEY (`idProdukt`) REFERENCES `Produkty_2NF` (`idProdukt`);

--
-- Ograniczenia dla tabeli `DetaleZamowien_3NF`
--
ALTER TABLE `DetaleZamowien_3NF`
  ADD CONSTRAINT `DetaleZamowien_3NF_ibfk_1` FOREIGN KEY (`NumerZam`) REFERENCES `Zamowienia_3NF` (`NumerZam`),
  ADD CONSTRAINT `DetaleZamowien_3NF_ibfk_2` FOREIGN KEY (`idProdukt`) REFERENCES `Produkty_3NF` (`idProdukt`);

--
-- Ograniczenia dla tabeli `Zamowienia_2NF`
--
ALTER TABLE `Zamowienia_2NF`
  ADD CONSTRAINT `NumerKlienta` FOREIGN KEY (`NumerKlienta`) REFERENCES `Klient_2NF` (`NumerKlienta`);

--
-- Ograniczenia dla tabeli `Zamowienia_3NF`
--
ALTER TABLE `Zamowienia_3NF`
  ADD CONSTRAINT `Zamowienia_3NF_ibfk_1` FOREIGN KEY (`NumerKlienta`) REFERENCES `Klient_2NF` (`NumerKlienta`);
