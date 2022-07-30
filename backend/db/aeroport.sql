-- MySQL dump 10.19  Distrib 10.3.34-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: aeroport
-- ------------------------------------------------------
-- Server version	10.3.34-MariaDB-0ubuntu0.20.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `alembic_version`
--

DROP TABLE IF EXISTS `alembic_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
INSERT INTO `alembic_version` VALUES ('474f5767b64b');
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `client`
--

DROP TABLE IF EXISTS `client`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `client` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nom` varchar(50) DEFAULT NULL,
  `prenom` varchar(50) DEFAULT NULL,
  `mail` varchar(50) DEFAULT NULL,
  `telephone` varchar(15) DEFAULT NULL,
  `cin` varchar(15) DEFAULT NULL,
  `nbr_passage` int(11) DEFAULT NULL,
  `categorie` enum('vol','reservation') DEFAULT NULL,
  `voyage` enum('national','International') DEFAULT NULL,
  `date_voyage` date DEFAULT NULL,
  `heurre_voyage` time DEFAULT NULL,
  `payement` enum('mvola','carte_bank') DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_client_id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `client`
--

LOCK TABLES `client` WRITE;
/*!40000 ALTER TABLE `client` DISABLE KEYS */;
/*!40000 ALTER TABLE `client` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reservation_international`
--

DROP TABLE IF EXISTS `reservation_international`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `reservation_international` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nom` varchar(50) DEFAULT NULL,
  `prenom` varchar(50) DEFAULT NULL,
  `mail` varchar(50) DEFAULT NULL,
  `telephone` varchar(15) DEFAULT NULL,
  `cin` varchar(15) DEFAULT NULL,
  `nbr_passage` int(11) DEFAULT NULL,
  `destination` enum('paris','bordeau') DEFAULT NULL,
  `date_voyage` date DEFAULT NULL,
  `heurre_voyage` time DEFAULT NULL,
  `payement` enum('mvola','carte_bank') DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_reservation_international_id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reservation_international`
--

LOCK TABLES `reservation_international` WRITE;
/*!40000 ALTER TABLE `reservation_international` DISABLE KEYS */;
/*!40000 ALTER TABLE `reservation_international` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reservation_national`
--

DROP TABLE IF EXISTS `reservation_national`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `reservation_national` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nom` varchar(50) DEFAULT NULL,
  `prenom` varchar(50) DEFAULT NULL,
  `mail` varchar(50) DEFAULT NULL,
  `telephone` varchar(15) DEFAULT NULL,
  `cin` varchar(15) DEFAULT NULL,
  `nbr_passage` int(11) DEFAULT NULL,
  `destination` enum('mahajanga','tamatave','diego') DEFAULT NULL,
  `date_voyage` date DEFAULT NULL,
  `heurre_voyage` time DEFAULT NULL,
  `payement` enum('mvola','carte_bank') DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_reservation_national_id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reservation_national`
--

LOCK TABLES `reservation_national` WRITE;
/*!40000 ALTER TABLE `reservation_national` DISABLE KEYS */;
/*!40000 ALTER TABLE `reservation_national` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vol_international`
--

DROP TABLE IF EXISTS `vol_international`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vol_international` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nom` varchar(50) DEFAULT NULL,
  `prenom` varchar(50) DEFAULT NULL,
  `mail` varchar(50) DEFAULT NULL,
  `telephone` varchar(15) DEFAULT NULL,
  `cin` varchar(15) DEFAULT NULL,
  `nbr_passage` int(11) DEFAULT NULL,
  `destination` enum('paris','bordeau') DEFAULT NULL,
  `date_voyage` date DEFAULT NULL,
  `heurre_voyage` time DEFAULT NULL,
  `payement` enum('mvola','carte_bank') DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_vol_international_id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vol_international`
--

LOCK TABLES `vol_international` WRITE;
/*!40000 ALTER TABLE `vol_international` DISABLE KEYS */;
/*!40000 ALTER TABLE `vol_international` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vol_national`
--

DROP TABLE IF EXISTS `vol_national`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vol_national` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nom` varchar(50) DEFAULT NULL,
  `prenom` varchar(50) DEFAULT NULL,
  `mail` varchar(50) DEFAULT NULL,
  `telephone` varchar(15) DEFAULT NULL,
  `cin` varchar(15) DEFAULT NULL,
  `nbr_passage` int(11) DEFAULT NULL,
  `destination` enum('mahajanga','tamatave','diego') DEFAULT NULL,
  `date_voyage` date DEFAULT NULL,
  `heurre_voyage` time DEFAULT NULL,
  `payement` enum('mvola','carte_bank') DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_vol_national_id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vol_national`
--

LOCK TABLES `vol_national` WRITE;
/*!40000 ALTER TABLE `vol_national` DISABLE KEYS */;
/*!40000 ALTER TABLE `vol_national` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-07-30 15:26:46
