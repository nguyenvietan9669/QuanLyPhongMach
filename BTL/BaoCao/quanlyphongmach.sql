-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 13, 2020 at 06:35 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `quanlyphongmach`
--

-- --------------------------------------------------------

--
-- Table structure for table `benhnhan`
--

CREATE TABLE `benhnhan` (
  `mabenhnhan` int(11) NOT NULL,
  `tenbenhnhan` varchar(50) COLLATE utf8mb4_unicode_520_ci DEFAULT NULL,
  `namsinh` date NOT NULL,
  `diachi` varchar(100) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `gioitinh` varchar(10) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `sodienthoai` int(11) DEFAULT NULL,
  `ngaykham` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;

-- --------------------------------------------------------

--
-- Table structure for table `benhnhandangkykham`
--

CREATE TABLE `benhnhandangkykham` (
  `manguoidangky` int(11) NOT NULL,
  `tenbenhnhan` varchar(50) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `namsinh` date NOT NULL,
  `diachi` varchar(100) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `gioitinh` varchar(10) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `sodienthoai` int(11) DEFAULT NULL,
  `thoigiandenkham` date NOT NULL,
  `status` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;

--
-- Dumping data for table `benhnhandangkykham`
--

INSERT INTO `benhnhandangkykham` (`manguoidangky`, `tenbenhnhan`, `namsinh`, `diachi`, `gioitinh`, `sodienthoai`, `thoigiandenkham`, `status`) VALUES
(1, 'Nguyễn Trung Hiếu ', '1999-06-25', 'Ninh Thuận', 'Nam', 923272840, '2020-09-14', 0);

-- --------------------------------------------------------

--
-- Table structure for table `cachdung`
--

CREATE TABLE `cachdung` (
  `macachdung` int(11) NOT NULL,
  `cachdung` varchar(100) COLLATE utf8mb4_unicode_520_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;

--
-- Dumping data for table `cachdung`
--

INSERT INTO `cachdung` (`macachdung`, `cachdung`) VALUES
(1, 'CÁCH DÙNG 1'),
(2, 'CÁCH DÙNG 2'),
(3, 'CÁCH DÙNG 3'),
(4, 'CÁCH DÙNG 4');

-- --------------------------------------------------------

--
-- Table structure for table `chitietphieukham`
--

CREATE TABLE `chitietphieukham` (
  `id_phieukham` int(11) NOT NULL,
  `id_loaibenh` int(11) NOT NULL,
  `trieuchung` varchar(255) COLLATE utf8mb4_unicode_520_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;

-- --------------------------------------------------------

--
-- Table structure for table `chitiettoathuoc`
--

CREATE TABLE `chitiettoathuoc` (
  `id_thuoc` int(11) NOT NULL,
  `id_toathuoc` int(11) NOT NULL,
  `soluong` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;

-- --------------------------------------------------------

--
-- Table structure for table `donvi`
--

CREATE TABLE `donvi` (
  `madonvi` int(11) NOT NULL,
  `tendonvi` varchar(50) COLLATE utf8mb4_unicode_520_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;

--
-- Dumping data for table `donvi`
--

INSERT INTO `donvi` (`madonvi`, `tendonvi`) VALUES
(1, 'Viên'),
(2, 'Chai');

-- --------------------------------------------------------

--
-- Table structure for table `hoadon`
--

CREATE TABLE `hoadon` (
  `mahoadon` int(11) NOT NULL,
  `id_phieukham` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;

-- --------------------------------------------------------

--
-- Table structure for table `loaibenh`
--

CREATE TABLE `loaibenh` (
  `mabenh` int(11) NOT NULL,
  `tenloaibenh` varchar(50) COLLATE utf8mb4_unicode_520_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;

--
-- Dumping data for table `loaibenh`
--

INSERT INTO `loaibenh` (`mabenh`, `tenloaibenh`) VALUES
(1, 'Sốt'),
(2, 'Tiêu Chảy'),
(3, 'Cảm Cúm'),
(4, 'Đau Đầu'),
(5, 'Sổ mũi');

-- --------------------------------------------------------

--
-- Table structure for table `phieukham`
--

CREATE TABLE `phieukham` (
  `maphieukham` int(11) NOT NULL,
  `id_benhnhan` int(11) NOT NULL,
  `id_toathuoc` int(11) DEFAULT NULL,
  `id_tien` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;

-- --------------------------------------------------------

--
-- Table structure for table `soluongbenhnhan`
--

CREATE TABLE `soluongbenhnhan` (
  `id` int(11) NOT NULL,
  `soluong` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;

--
-- Dumping data for table `soluongbenhnhan`
--

INSERT INTO `soluongbenhnhan` (`id`, `soluong`) VALUES
(1, 40);

-- --------------------------------------------------------

--
-- Table structure for table `thuoc`
--

CREATE TABLE `thuoc` (
  `mathuoc` int(11) NOT NULL,
  `tenthuoc` varchar(100) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `gia` float DEFAULT NULL,
  `id_cachdung` int(11) NOT NULL,
  `id_donvi` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;

--
-- Dumping data for table `thuoc`
--

INSERT INTO `thuoc` (`mathuoc`, `tenthuoc`, `gia`, `id_cachdung`, `id_donvi`) VALUES
(1, 'Thuốc 1', 10000, 2, 2),
(2, 'Thuốc 2', 10000, 2, 1),
(3, 'Thuốc 3', 10000, 1, 1),
(4, 'Thuốc 4', 20000, 1, 2),
(5, 'Thuốc 5', 5000, 1, 1),
(6, 'Thuốc 6', 2000, 4, 1),
(7, 'Thuốc 7', 7000, 3, 2),
(8, 'Thuốc 8', 1500, 3, 2),
(9, 'Thuốc 9', 2500, 4, 1),
(10, 'Thuốc 10', 15000, 2, 2),
(11, 'Thuốc 11', 10000, 2, 2),
(12, 'Thuốc 12', 20000, 2, 2),
(13, 'Thuốc 13', 4000, 2, 1),
(14, 'Thuốc 14', 2000, 1, 2),
(15, 'Thuốc 15', 5000, 1, 1),
(16, 'Thuốc 16', 8000, 3, 2),
(17, 'Thuốc 17', 5000, 4, 2),
(18, 'Thuốc 18', 2000, 1, 1),
(19, 'Thuốc 19', 15000, 1, 2),
(20, 'Thuốc 20', 8000, 1, 1),
(21, 'Thuốc 21', 6000, 2, 2),
(22, 'Thuốc 22', 25000, 1, 2),
(23, 'Thuốc 23', 14000, 1, 1),
(24, 'Thuốc 24', 1500, 1, 1),
(25, 'Thuốc 25', 12000, 1, 2),
(26, 'Thuốc 26', 2000, 3, 2),
(27, 'Thuốc 27', 14000, 1, 2),
(28, 'Thuốc 28', 5000, 2, 2),
(29, 'Thuốc 29', 5000, 2, 2),
(30, 'Thuốc 30', 5000, 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `tienkham`
--

CREATE TABLE `tienkham` (
  `matien` int(11) NOT NULL,
  `sotien` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;

--
-- Dumping data for table `tienkham`
--

INSERT INTO `tienkham` (`matien`, `sotien`) VALUES
(1, 30000);

-- --------------------------------------------------------

--
-- Table structure for table `toathuoc`
--

CREATE TABLE `toathuoc` (
  `matoathuoc` int(11) NOT NULL,
  `ngayketoa` datetime DEFAULT NULL,
  `nguoiketoa` varchar(100) COLLATE utf8mb4_unicode_520_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `name` varchar(50) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `active` tinyint(1) DEFAULT NULL,
  `username` varchar(50) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `password` varchar(50) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `type` int(11) NOT NULL
) ;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `name`, `active`, `username`, `password`, `type`) VALUES
(1, 'an', 0, 'admin', 'e10adc3949ba59abbe56e057f20f883e', 0),
(2, 'hieu', 0, 'user', 'e10adc3949ba59abbe56e057f20f883e', 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `benhnhan`
--
ALTER TABLE `benhnhan`
  ADD PRIMARY KEY (`mabenhnhan`);

--
-- Indexes for table `benhnhandangkykham`
--
ALTER TABLE `benhnhandangkykham`
  ADD PRIMARY KEY (`manguoidangky`);

--
-- Indexes for table `cachdung`
--
ALTER TABLE `cachdung`
  ADD PRIMARY KEY (`macachdung`);

--
-- Indexes for table `chitietphieukham`
--
ALTER TABLE `chitietphieukham`
  ADD PRIMARY KEY (`id_phieukham`,`id_loaibenh`),
  ADD KEY `id_loaibenh` (`id_loaibenh`);

--
-- Indexes for table `chitiettoathuoc`
--
ALTER TABLE `chitiettoathuoc`
  ADD PRIMARY KEY (`id_thuoc`,`id_toathuoc`),
  ADD KEY `id_toathuoc` (`id_toathuoc`);

--
-- Indexes for table `donvi`
--
ALTER TABLE `donvi`
  ADD PRIMARY KEY (`madonvi`);

--
-- Indexes for table `hoadon`
--
ALTER TABLE `hoadon`
  ADD PRIMARY KEY (`mahoadon`),
  ADD KEY `id_phieukham` (`id_phieukham`);

--
-- Indexes for table `loaibenh`
--
ALTER TABLE `loaibenh`
  ADD PRIMARY KEY (`mabenh`);

--
-- Indexes for table `phieukham`
--
ALTER TABLE `phieukham`
  ADD PRIMARY KEY (`maphieukham`,`id_benhnhan`),
  ADD KEY `id_benhnhan` (`id_benhnhan`),
  ADD KEY `id_toathuoc` (`id_toathuoc`),
  ADD KEY `id_tien` (`id_tien`);

--
-- Indexes for table `soluongbenhnhan`
--
ALTER TABLE `soluongbenhnhan`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `thuoc`
--
ALTER TABLE `thuoc`
  ADD PRIMARY KEY (`mathuoc`),
  ADD KEY `id_cachdung` (`id_cachdung`),
  ADD KEY `id_donvi` (`id_donvi`);

--
-- Indexes for table `tienkham`
--
ALTER TABLE `tienkham`
  ADD PRIMARY KEY (`matien`);

--
-- Indexes for table `toathuoc`
--
ALTER TABLE `toathuoc`
  ADD PRIMARY KEY (`matoathuoc`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `benhnhan`
--
ALTER TABLE `benhnhan`
  MODIFY `mabenhnhan` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `benhnhandangkykham`
--
ALTER TABLE `benhnhandangkykham`
  MODIFY `manguoidangky` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `cachdung`
--
ALTER TABLE `cachdung`
  MODIFY `macachdung` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `donvi`
--
ALTER TABLE `donvi`
  MODIFY `madonvi` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `hoadon`
--
ALTER TABLE `hoadon`
  MODIFY `mahoadon` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `loaibenh`
--
ALTER TABLE `loaibenh`
  MODIFY `mabenh` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `phieukham`
--
ALTER TABLE `phieukham`
  MODIFY `maphieukham` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `soluongbenhnhan`
--
ALTER TABLE `soluongbenhnhan`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `thuoc`
--
ALTER TABLE `thuoc`
  MODIFY `mathuoc` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- AUTO_INCREMENT for table `tienkham`
--
ALTER TABLE `tienkham`
  MODIFY `matien` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `toathuoc`
--
ALTER TABLE `toathuoc`
  MODIFY `matoathuoc` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `chitietphieukham`
--
ALTER TABLE `chitietphieukham`
  ADD CONSTRAINT `chitietphieukham_ibfk_1` FOREIGN KEY (`id_phieukham`) REFERENCES `phieukham` (`maphieukham`),
  ADD CONSTRAINT `chitietphieukham_ibfk_2` FOREIGN KEY (`id_loaibenh`) REFERENCES `loaibenh` (`mabenh`);

--
-- Constraints for table `chitiettoathuoc`
--
ALTER TABLE `chitiettoathuoc`
  ADD CONSTRAINT `chitiettoathuoc_ibfk_1` FOREIGN KEY (`id_thuoc`) REFERENCES `thuoc` (`mathuoc`),
  ADD CONSTRAINT `chitiettoathuoc_ibfk_2` FOREIGN KEY (`id_toathuoc`) REFERENCES `toathuoc` (`matoathuoc`);

--
-- Constraints for table `hoadon`
--
ALTER TABLE `hoadon`
  ADD CONSTRAINT `hoadon_ibfk_1` FOREIGN KEY (`id_phieukham`) REFERENCES `phieukham` (`maphieukham`);

--
-- Constraints for table `phieukham`
--
ALTER TABLE `phieukham`
  ADD CONSTRAINT `phieukham_ibfk_1` FOREIGN KEY (`id_benhnhan`) REFERENCES `benhnhan` (`mabenhnhan`),
  ADD CONSTRAINT `phieukham_ibfk_2` FOREIGN KEY (`id_toathuoc`) REFERENCES `toathuoc` (`matoathuoc`),
  ADD CONSTRAINT `phieukham_ibfk_3` FOREIGN KEY (`id_tien`) REFERENCES `tienkham` (`matien`);

--
-- Constraints for table `thuoc`
--
ALTER TABLE `thuoc`
  ADD CONSTRAINT `thuoc_ibfk_1` FOREIGN KEY (`id_cachdung`) REFERENCES `cachdung` (`macachdung`),
  ADD CONSTRAINT `thuoc_ibfk_2` FOREIGN KEY (`id_donvi`) REFERENCES `donvi` (`madonvi`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
