-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 20, 2020 at 10:55 AM
-- Server version: 10.4.10-MariaDB
-- PHP Version: 7.3.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `dexcommunity`
--

-- --------------------------------------------------------

--
-- Table structure for table `resources`
--

CREATE TABLE `resources` (
  `id` int(10) NOT NULL,
  `f_name` varchar(50) NOT NULL,
  `competition_name` varchar(100) NOT NULL,
  `required_skills` varchar(100) NOT NULL,
  `suggested_courses` varchar(100) NOT NULL,
  `duration` varchar(50) NOT NULL,
  `designation` varchar(50) NOT NULL,
  `company_name` varchar(100) NOT NULL,
  `experience` varchar(20) NOT NULL,
  `linked_in` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `resources`
--

INSERT INTO `resources` (`id`, `f_name`, `competition_name`, `required_skills`, `suggested_courses`, `duration`, `designation`, `company_name`, `experience`, `linked_in`) VALUES
(1, 'Chandresh', 'SparkAR Hackathon', 'AR', 'Spark AR Developer', '8 Week', 'Student', 'PPSU', '3rd Year BTech', 'linkedin.com/crman'),
(2, ' Ma', 'Elocution', 'Speaking', 'Online', '1 Week', 'Student', 'PPSU', '3rd year b.tech', 'linkedin.com/xyz'),
(8, 'Dexterity', 'LeaderShip', 'Leadership and Managing', 'Online', '5 to 8 Weeks', 'Student', 'Dexterity Global', '2', 'linkedin.com/dg');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `resources`
--
ALTER TABLE `resources`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `resources`
--
ALTER TABLE `resources`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
