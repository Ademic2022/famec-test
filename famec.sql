-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: famec_db
-- ------------------------------------------------------
-- Server version	8.0.34

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `families`
--

DROP TABLE IF EXISTS `families`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `families` (
  `name` varchar(128) NOT NULL,
  `owner_id` varchar(60) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `id` varchar(60) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `owner_id` (`owner_id`),
  CONSTRAINT `families_ibfk_1` FOREIGN KEY (`owner_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `families`
--

LOCK TABLES `families` WRITE;
/*!40000 ALTER TABLE `families` DISABLE KEYS */;
INSERT INTO `families` VALUES ('fatimah','a57294fd-cd64-4a06-9a01-842a1a539f0e','4b256934-0c9e-4676-9a3f-4eb822b445cd','2023-09-06 16:05:44','2023-09-06 16:05:44');
/*!40000 ALTER TABLE `families` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `notifications`
--

DROP TABLE IF EXISTS `notifications`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `notifications` (
  `sender_id` varchar(60) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `recipient_id` varchar(60) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `content` varchar(255) NOT NULL,
  `is_read` tinyint(1) DEFAULT NULL,
  `family_id` varchar(60) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `id` varchar(60) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `sender_id` (`sender_id`),
  KEY `recipient_id` (`recipient_id`),
  KEY `family_id` (`family_id`),
  CONSTRAINT `notifications_ibfk_1` FOREIGN KEY (`sender_id`) REFERENCES `users` (`id`),
  CONSTRAINT `notifications_ibfk_2` FOREIGN KEY (`recipient_id`) REFERENCES `users` (`id`),
  CONSTRAINT `notifications_ibfk_3` FOREIGN KEY (`family_id`) REFERENCES `families` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `notifications`
--

LOCK TABLES `notifications` WRITE;
/*!40000 ALTER TABLE `notifications` DISABLE KEYS */;
INSERT INTO `notifications` VALUES ('a57294fd-cd64-4a06-9a01-842a1a539f0e','9912a299-220b-4bae-8d8a-02dc2d966189','A new task \'Bedroom Arrangment\' has been created in your family.',0,'4b256934-0c9e-4676-9a3f-4eb822b445cd','065dfada-11e9-4a11-8dbf-dae0cdbb1f96','2023-09-06 18:42:45','2023-09-06 18:42:45'),('a57294fd-cd64-4a06-9a01-842a1a539f0e','43823a9e-fe3a-4e09-9e74-6809293515a7','A new task \'Bedroom Arrangment\' has been created in your family.',0,'4b256934-0c9e-4676-9a3f-4eb822b445cd','19581be7-321e-4f4d-bbb1-b6cd68a1bf19','2023-09-06 18:42:45','2023-09-06 18:42:45'),('43823a9e-fe3a-4e09-9e74-6809293515a7','a57294fd-cd64-4a06-9a01-842a1a539f0e','A new task \'Bedroom  spaces\' has been created in your family.',0,'4b256934-0c9e-4676-9a3f-4eb822b445cd','2bfa16e4-34b9-4b48-847f-c207f016ceef','2023-09-06 20:36:36','2023-09-06 20:36:36'),('43823a9e-fe3a-4e09-9e74-6809293515a7','9912a299-220b-4bae-8d8a-02dc2d966189','A new task \'Bedroom  spaces\' has been created in your family.',0,'4b256934-0c9e-4676-9a3f-4eb822b445cd','7bc04d61-3c77-46cc-862e-2b8e831d4a4b','2023-09-06 20:36:36','2023-09-06 20:36:36');
/*!40000 ALTER TABLE `notifications` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tasks`
--

DROP TABLE IF EXISTS `tasks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tasks` (
  `title` varchar(255) NOT NULL,
  `description` varchar(1000) DEFAULT NULL,
  `due_date` varchar(50) DEFAULT NULL,
  `priority` int DEFAULT NULL,
  `status` int DEFAULT NULL,
  `user_id` varchar(60) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `family_id` varchar(60) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `id` varchar(60) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `user_id` (`user_id`),
  KEY `family_id` (`family_id`),
  CONSTRAINT `tasks_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`),
  CONSTRAINT `tasks_ibfk_2` FOREIGN KEY (`family_id`) REFERENCES `families` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tasks`
--

LOCK TABLES `tasks` WRITE;
/*!40000 ALTER TABLE `tasks` DISABLE KEYS */;
INSERT INTO `tasks` VALUES ('Bedroom Arrangment','cleanings','2023-09-28',1,0,'a57294fd-cd64-4a06-9a01-842a1a539f0e','4b256934-0c9e-4676-9a3f-4eb822b445cd','10b44c8e-f7ec-482c-8abb-a9dfddb4f2c8','2023-09-06 18:42:45','2023-09-06 18:42:45'),('Bedroom  spaces','describe task','2023-09-12',1,0,'43823a9e-fe3a-4e09-9e74-6809293515a7','4b256934-0c9e-4676-9a3f-4eb822b445cd','79adcf76-9236-4252-9488-d6fd5d487a94','2023-09-06 20:36:34','2023-09-06 20:36:34');
/*!40000 ALTER TABLE `tasks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `firstname` varchar(128) NOT NULL,
  `lastname` varchar(128) NOT NULL,
  `email` varchar(128) NOT NULL,
  `password` varchar(128) NOT NULL,
  `username` varchar(128) NOT NULL,
  `address` varchar(255) NOT NULL,
  `country` varchar(30) NOT NULL,
  `state` varchar(30) NOT NULL,
  `zipcode` int NOT NULL,
  `birthday` varchar(10) DEFAULT NULL,
  `family_id` varchar(60) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `id` varchar(60) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `family_id` (`family_id`),
  CONSTRAINT `users_ibfk_1` FOREIGN KEY (`family_id`) REFERENCES `families` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('ademic','Michael','mike@gmail.com','25d55ad283aa400af464c76d713c07ad','ademic','something','Nigeria','Oyo State',45234,'2/12','4b256934-0c9e-4676-9a3f-4eb822b445cd','43823a9e-fe3a-4e09-9e74-6809293515a7','2023-09-06 16:33:57','2023-09-06 16:33:57'),('Adeeyo','Michael','miked@gmail.com','25d55ad283aa400af464c76d713c07ad','iammelody','something','Nigeria','Oyo State',45234,'2/12','4b256934-0c9e-4676-9a3f-4eb822b445cd','9912a299-220b-4bae-8d8a-02dc2d966189','2023-09-06 18:29:00','2023-09-06 18:29:00'),('Fatimah','Hassan','fatimahhassan@gmail.com','25d55ad283aa400af464c76d713c07ad','kennyfatimah','something','Nigeria','Oyo State',45234,'3/14','4b256934-0c9e-4676-9a3f-4eb822b445cd','a57294fd-cd64-4a06-9a01-842a1a539f0e','2023-09-06 16:05:43','2023-09-06 16:05:43');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-09-07  1:26:12
