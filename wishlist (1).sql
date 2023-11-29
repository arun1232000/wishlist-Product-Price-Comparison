-- phpMyAdmin SQL Dump
-- version 3.3.9
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Feb 25, 2021 at 10:55 AM
-- Server version: 5.5.8
-- PHP Version: 5.3.5

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `wishlist`
--

-- --------------------------------------------------------

--
-- Table structure for table `cart`
--

CREATE TABLE IF NOT EXISTS `cart` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cid` int(11) NOT NULL,
  `pid` int(11) NOT NULL,
  `qty` int(11) NOT NULL,
  `price` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `cart`
--


-- --------------------------------------------------------

--
-- Table structure for table `categories`
--

CREATE TABLE IF NOT EXISTS `categories` (
  `cat_id` int(11) NOT NULL AUTO_INCREMENT,
  `cat_title` varchar(50) NOT NULL,
  PRIMARY KEY (`cat_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `categories`
--

INSERT INTO `categories` (`cat_id`, `cat_title`) VALUES
(1, 'Mobile'),
(2, 'Cloths');

-- --------------------------------------------------------

--
-- Table structure for table `cusreg`
--

CREATE TABLE IF NOT EXISTS `cusreg` (
  `cid` int(11) NOT NULL AUTO_INCREMENT,
  `cname` varchar(50) NOT NULL,
  `address` varchar(50) NOT NULL,
  `pincode` int(11) NOT NULL,
  `gender` varchar(50) NOT NULL,
  `age` int(11) NOT NULL,
  `district` varchar(50) NOT NULL,
  `location` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `mobile` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  PRIMARY KEY (`cid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `cusreg`
--

INSERT INTO `cusreg` (`cid`, `cname`, `address`, `pincode`, `gender`, `age`, `district`, `location`, `email`, `mobile`, `password`) VALUES
(1, 'manu', 'dffgh', 698523, 'Male', 35, 'ernakulam', 'kaloor', 'manu@gmail.com', '9856365214', '123456');

-- --------------------------------------------------------

--
-- Table structure for table `customer_order`
--

CREATE TABLE IF NOT EXISTS `customer_order` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) NOT NULL,
  `pid` int(11) NOT NULL,
  `p_price` int(11) NOT NULL,
  `p_qty` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `customer_order`
--

INSERT INTO `customer_order` (`id`, `uid`, `pid`, `p_price`, `p_qty`) VALUES
(1, 0, 5, 38000, 2),
(2, 0, 5, 38000, 2),
(3, 1, 5, 19000, 1);

-- --------------------------------------------------------

--
-- Table structure for table `feedback`
--

CREATE TABLE IF NOT EXISTS `feedback` (
  `fid` int(11) NOT NULL AUTO_INCREMENT,
  `feedback` varchar(50) NOT NULL,
  `date` varchar(50) NOT NULL,
  `userid` int(11) NOT NULL,
  PRIMARY KEY (`fid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `feedback`
--

INSERT INTO `feedback` (`fid`, `feedback`, `date`, `userid`) VALUES
(2, 'very good website', '2021-02-03', 1),
(4, 'nice one', '2021-02-03', 1);

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE IF NOT EXISTS `login` (
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `usertype` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`username`, `password`, `usertype`) VALUES
('manu@gmail.com', '123456', 'Customer'),
('amazon@gmail.com', 'amazon', 'Shop'),
('admin@gmail.com', 'admin', 'Admin'),
('ann@gmail.com', '123456', 'Shop');

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE IF NOT EXISTS `products` (
  `product_id` int(11) NOT NULL AUTO_INCREMENT,
  `product_cat` varchar(50) NOT NULL,
  `product_brand` varchar(50) NOT NULL,
  `product_title` varchar(50) NOT NULL,
  `product_price` int(11) NOT NULL,
  `quantity` int(11) NOT NULL,
  `product_desc` varchar(50) NOT NULL,
  `product_image` varchar(200) NOT NULL,
  `product_keywords` varchar(50) NOT NULL,
  `shid` int(11) NOT NULL,
  PRIMARY KEY (`product_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=7 ;

--
-- Dumping data for table `products`
--

INSERT INTO `products` (`product_id`, `product_cat`, `product_brand`, `product_title`, `product_price`, `quantity`, `product_desc`, `product_image`, `product_keywords`, `shid`) VALUES
(4, '1', 'None', 'Redmi 6 A', 20000, 60, 'This phone has intern', '/media/p07lbt6x.jpg', 'redmi 6A', 1),
(5, '1', 'None', 'Redmi 5 A', 19000, 60, 'lens6', '/media/49687782373_e4c01a4bd6_4k.jpg', 'redmi 5A', 1),
(6, '1', 'None', 'Redmi 5 A', 26000, 65, 'This phone has intern', '/media/words-news-on-digital-blue-background-picture-id892726222-300x200.jpg', 'redmi 5A', 1);

-- --------------------------------------------------------

--
-- Table structure for table `shopreg`
--

CREATE TABLE IF NOT EXISTS `shopreg` (
  `sid` int(11) NOT NULL AUTO_INCREMENT,
  `shop` varchar(50) NOT NULL,
  `district` varchar(50) NOT NULL,
  `city` varchar(50) NOT NULL,
  `phone` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `reg_no` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL,
  PRIMARY KEY (`sid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `shopreg`
--

INSERT INTO `shopreg` (`sid`, `shop`, `district`, `city`, `phone`, `email`, `reg_no`, `password`, `status`) VALUES
(1, 'amazon', 'ernakulam', 'aluva', '09987654323', 'amazon@gmail.com', '6587452369', 'amazon', 'Accept'),
(2, 'ann', 'ernakulam', 'kaloor', '09563254789', 'ann@gmail.com', '2563145698', '123456', 'Accept');
