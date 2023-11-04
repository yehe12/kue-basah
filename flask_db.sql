CREATE DATABASE  IF NOT EXISTS `flask_db` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `flask_db`;
-- MySQL dump 10.13  Distrib 8.0.33, for Linux (x86_64)
--
-- Host: localhost    Database: flask_db
-- ------------------------------------------------------
-- Server version	8.0.33-0ubuntu0.22.04.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `damage_indication`
--

DROP TABLE IF EXISTS `damage_indication`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `damage_indication` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `indication_name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `damage_indication`
--

LOCK TABLES `damage_indication` WRITE;
/*!40000 ALTER TABLE `damage_indication` DISABLE KEYS */;
INSERT INTO `damage_indication` VALUES (1,'Mati total'),(2,'Sering not responding/ hang'),(3,'Sering mati tiba-tiba'),(4,'Saat shut down kembali nyala lagi'),(5,'Fan processor mati'),(6,'Nyala sebentar terus mati (tidak sampai tampil dimonitor)'),(7,'Driver VGA error saat di install'),(8,'Layar monitor blue screen'),(9,'Hanya tampil boot screen'),(10,'Bunyi beep panjang 1 kali dan pendek 1 kali'),(11,'Saat install windows tiba-tiba error'),(12,'Bunyi beep pendek beberapa kali'),(13,'Saat di jalankan program berat sering ngehang'),(14,'Saat dinyalakan tidak ada tampil di layar monitor'),(15,'Gambar yang di tampilkan pecah-pecah'),(16,'Tiba-tiba harddisk tidak terbaca'),(17,'Harus di tekan tombol berulang kali baru bisa nyala'),(18,'Saat boot screen PC/Laptop restart sendiri'),(19,'Operating system not found'),(20,'Saat copy/cut file yang ukurannya besar tiba-tiba berhenti'),(21,'Saat install OS windows tidak bisa di partisi'),(22,'Saat install tidak bisa format partisi'),(23,'Tidak bisa di install OS windows'),(24,'Windows jalannya lemot'),(25,'Drive tidak terbaca di windows'),(26,'Burning file hasil nya tidak bisa di jalankan'),(27,'Untuk baca kaset CD/DVD lemot'),(28,'Cover DVD-ROM macet tidak mau keluar');
/*!40000 ALTER TABLE `damage_indication` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `repair`
--

DROP TABLE IF EXISTS `repair`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `repair` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `device_type` varchar(255) NOT NULL,
  `damage_indication` varchar(255) NOT NULL,
  `note_from_user` varchar(255) DEFAULT NULL,
  `cost_total` int DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  `create_at` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `repair`
--

LOCK TABLES `repair` WRITE;
/*!40000 ALTER TABLE `repair` DISABLE KEYS */;
INSERT INTO `repair` VALUES (4,4,'Laptop','Sering not responding/ hang. Sering mati tiba-tiba. Fan processor mati. ','mohon segera dikerjakan ',370000,'dibatalkan','2023-05-07 20:31:22'),(5,4,'Computer','Mati total. Fan processor mati. ','',350000,'diambil','2023-05-07 20:49:54'),(6,3,'Computer','Mati total. ','',0,'dalam antrian','2023-05-11 07:26:43'),(7,3,'Computer','Mati total. ','',0,'dalam antrian','2023-05-11 07:46:37');
/*!40000 ALTER TABLE `repair` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `repair_detail`
--

DROP TABLE IF EXISTS `repair_detail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `repair_detail` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `repair_id` int NOT NULL,
  `damage_problem` varchar(255) DEFAULT NULL,
  `damage_solution` varchar(255) DEFAULT NULL,
  `cost` int DEFAULT NULL,
  `confirmed` varchar(45) DEFAULT NULL,
  `create_at` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `repair_detail`
--

LOCK TABLES `repair_detail` WRITE;
/*!40000 ALTER TABLE `repair_detail` DISABLE KEYS */;
INSERT INTO `repair_detail` VALUES (1,5,'PSU mati','ganti PSU Simbadda 380w',250000,'true','2023-03-16 20:55:18'),(2,5,'OS terdapat masalah','Instal ulang OS',100000,'true','2023-03-16 20:57:04'),(3,4,'fan prosesor bermasalah','ganti fan prosesor',320000,'true','2023-03-16 21:32:59'),(4,4,'mainboard kotor','bersihkan',50000,'true','2023-04-04 07:56:17'),(5,7,'kobong','buang saja',0,'false','2023-05-25 07:44:46');
/*!40000 ALTER TABLE `repair_detail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `role`
--

DROP TABLE IF EXISTS `role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `role` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `role_name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `role`
--

LOCK TABLES `role` WRITE;
/*!40000 ALTER TABLE `role` DISABLE KEYS */;
INSERT INTO `role` VALUES (1,'admin'),(2,'technician'),(3,'boss'),(4,'customer');
/*!40000 ALTER TABLE `role` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `role_id` int NOT NULL,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `address` varchar(255) DEFAULT NULL,
  `phone` varchar(255) DEFAULT NULL,
  `otp` varchar(45) DEFAULT NULL,
  `email_verified_at` datetime DEFAULT NULL,
  `create_at` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,1,'Admin','admin@email.com','123','sby','085xxxxxxxxx','xxxxxx','2021-01-13 06:35:27','2021-01-13 06:35:27'),(2,2,'Technician','tech@email.com','123','',NULL,NULL,'2021-01-13 06:35:27','2021-01-13 06:35:27'),(3,3,'Boss','boss@email.com','123',NULL,NULL,NULL,'2021-01-13 06:35:27','2021-01-13 06:35:27'),(4,4,'Muhammad Abdullah','ma22052000@gmail.com','123','Jl. Irawati II No. 2 Surabaya','08563357829','288599','2023-03-16 20:26:16','2023-05-16 20:25:50');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-26  5:46:17
