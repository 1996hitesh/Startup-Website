-- phpMyAdmin SQL Dump
-- version 4.8.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 30, 2020 at 12:58 PM
-- Server version: 10.1.34-MariaDB
-- PHP Version: 7.2.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `startup`
--

-- --------------------------------------------------------

--
-- Table structure for table `contact`
--

CREATE TABLE `contact` (
  `sno` int(11) NOT NULL,
  `name` text NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone_num` varchar(15) NOT NULL,
  `msg` text NOT NULL,
  `date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `contact`
--

INSERT INTO `contact` (`sno`, `name`, `email`, `phone_num`, `msg`, `date`) VALUES
(9, 'asdfasdg', 'asdfasdg', 'asdgasdf', 'dafadfg', '2020-04-29 18:16:08'),
(10, 'masnbdmanbsf', 'masbfmnasbf', 'masnbfmnabsf', 'bnnmdsbfmansb', '2020-04-29 18:22:24'),
(11, 'My name', 'myemail@email.com', '8797947522', 'This is a test message', '2020-05-20 14:34:31'),
(12, 'My name', 'myemail@email.com', '8797947522', 'This is a test message', '2020-05-20 15:13:39');

-- --------------------------------------------------------

--
-- Table structure for table `courses`
--

CREATE TABLE `courses` (
  `sno` int(11) NOT NULL,
  `title` text NOT NULL,
  `content` text NOT NULL,
  `slug` varchar(30) NOT NULL,
  `subtitle` text NOT NULL,
  `icon` varchar(30) NOT NULL,
  `background` varchar(30) NOT NULL,
  `about` text NOT NULL,
  `objectives` text NOT NULL,
  `audience` text NOT NULL,
  `prerequisites` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `courses`
--

INSERT INTO `courses` (`sno`, `title`, `content`, `slug`, `subtitle`, `icon`, `background`, `about`, `objectives`, `audience`, `prerequisites`) VALUES
(1, 'This is the title for first course.', 'This training is designed for all, who wants to learn ABC of Artificial Intelligence and quickly get familiar with this popular technology and its importance. This training will familiarize you with applications and real-life use cases of AI in different industries, including e-commerce, banking, healthcare, automation, etc. Additionally, you’ll also get to know about various AI techniques, ML subsets & process, and popular Machine Learning models. Our Machine Learning beginner course will equip you with the fundamentals of the AI & ML concepts. This training will serve as the foundation that you need before you can set out on our comprehensive and diverse learning paths of Machine Learning that are aligned to your needs.', 'first-course', 'Subtitle of the course', 'ML.png', 'course background', 'about the course', 'course objectives', 'target audience', 'prerequisites of the course');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contact`
--
ALTER TABLE `contact`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `courses`
--
ALTER TABLE `courses`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contact`
--
ALTER TABLE `contact`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `courses`
--
ALTER TABLE `courses`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
