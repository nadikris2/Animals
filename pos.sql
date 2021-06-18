-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 17, 2021 at 07:10 PM
-- Server version: 10.4.18-MariaDB
-- PHP Version: 8.0.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pos`
--

-- --------------------------------------------------------

--
-- Table structure for table `historyproducts`
--

CREATE TABLE `historyproducts` (
  `id` int(11) NOT NULL,
  `id_barang` int(11) NOT NULL,
  `id_user` int(11) NOT NULL,
  `action` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `historyproducts`
--

INSERT INTO `historyproducts` (`id`, `id_barang`, `id_user`, `action`) VALUES
(1, 1, 1, 'Insert'),
(2, 2, 1, 'Insert'),
(3, 1, 1, 'Delete'),
(4, 2, 1, 'Delete'),
(5, 3, 1, 'Delete'),
(6, 4, 1, 'Delete'),
(7, 6, 1, 'Insert'),
(8, 5, 1, 'Delete'),
(9, 6, 1, 'Delete'),
(10, 7, 1, 'Insert'),
(11, 8, 1, 'Insert'),
(12, 9, 1, 'Insert'),
(13, 10, 1, 'Insert'),
(14, 11, 1, 'Insert'),
(15, 12, 1, 'Insert'),
(16, 13, 1, 'Insert'),
(17, 14, 1, 'Insert'),
(18, 15, 1, 'Insert'),
(19, 16, 1, 'Insert'),
(20, 16, 1, 'Delete'),
(21, 15, 1, 'Delete'),
(22, 7, 1, 'Delete');

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE `products` (
  `id` int(11) NOT NULL,
  `barang` varchar(45) NOT NULL,
  `harga` int(11) NOT NULL,
  `jumlah` int(11) NOT NULL,
  `user_id` int(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `products`
--

INSERT INTO `products` (`id`, `barang`, `harga`, `jumlah`, `user_id`) VALUES
(8, 'Dog Food', 276000, 89, 1),
(9, 'Dog Toy Spidey', 172400, 100, 1),
(10, 'Dog Toy Frisbee', 206880, 100, 1),
(11, 'Dog Toy Bone', 137747, 100, 1),
(12, 'Dog Toy Banana', 86000, 100, 1),
(13, 'Dog Mask', 86000, 10, 1),
(14, 'Dog Medical Collar', 258582, 10, 1);

-- --------------------------------------------------------

--
-- Table structure for table `transactions`
--

CREATE TABLE `transactions` (
  `id` int(11) NOT NULL,
  `create_on` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `transactions`
--

INSERT INTO `transactions` (`id`, `create_on`) VALUES
(2, '2021-06-17 23:46:44'),
(3, '2021-06-17 23:47:10');

-- --------------------------------------------------------

--
-- Table structure for table `transaction_products`
--

CREATE TABLE `transaction_products` (
  `id` int(11) NOT NULL,
  `transaction_id` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  `product_qty` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `transaction_products`
--

INSERT INTO `transaction_products` (`id`, `transaction_id`, `product_id`, `product_qty`) VALUES
(1, 2, 8, 1),
(2, 3, 8, 10);

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(30) NOT NULL,
  `username` varchar(20) NOT NULL,
  `email` varchar(20) NOT NULL,
  `role` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `username`, `email`, `role`) VALUES
(1, 'nadikris', 'nadikris2@gmail.com', 'admin'),
(2, 'nadikris2', 'nadikris10@gmail.com', 'customer');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `historyproducts`
--
ALTER TABLE `historyproducts`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `transactions`
--
ALTER TABLE `transactions`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `transaction_products`
--
ALTER TABLE `transaction_products`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `historyproducts`
--
ALTER TABLE `historyproducts`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT for table `products`
--
ALTER TABLE `products`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `transactions`
--
ALTER TABLE `transactions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `transaction_products`
--
ALTER TABLE `transaction_products`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(30) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
