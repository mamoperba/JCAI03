-- MySQL dump 10.13  Distrib 8.0.45, for Win64 (x86_64)
--
-- Host: localhost    Database: db_gudang
-- ------------------------------------------------------
-- Server version	8.0.45

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
-- Table structure for table `sparepart`
--

DROP TABLE IF EXISTS `sparepart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sparepart` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nama_part` varchar(100) DEFAULT NULL,
  `kategori` varchar(50) DEFAULT NULL,
  `merk` varchar(50) DEFAULT NULL,
  `harga` int DEFAULT NULL,
  `stok` int DEFAULT NULL,
  `tanggal_masuk` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sparepart`
--

LOCK TABLES `sparepart` WRITE;
/*!40000 ALTER TABLE `sparepart` DISABLE KEYS */;
INSERT INTO `sparepart` VALUES (2,'Kampas Rem Depan','Kaki-kaki','Brembo',350000,30,'2026-01-12'),(3,'Filter Udara','Mesin','Toyota',80000,40,'2026-01-15'),(4,'Aki Mobil 12V','Kelistrikan','GS Astra',950000,20,'2026-01-18'),(5,'Busi Iridium','Mesin','NGK',45000,100,'2026-01-20'),(6,'Radiator Coolant','Pendingin','Prestone',70000,60,'2026-01-22'),(7,'Lampu LED Headlamp','Kelistrikan','Philips',250000,25,'2026-01-25'),(8,'Shockbreaker Belakang','Kaki-kaki','KYB',600000,15,'2026-01-28'),(9,'Filter Oli','Mesin','Bosch',60000,70,'2026-02-01'),(10,'Kopling Set','Transmisi','Exedy',1200000,10,'2026-02-05'),(11,'Oli Mesin 6W-20','Mesin','Castrol',15000,20,'2026-03-18'),(12,'lampu depan','Kelistrikan','Philips',20000,10,'2026-03-13');
/*!40000 ALTER TABLE `sparepart` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-03-18 11:28:05
