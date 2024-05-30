# HeidiSQL Dump 
#
# --------------------------------------------------------
# Host:                         127.0.0.1
# Database:                     todolist
# Server version:               5.5.8-log
# Server OS:                    Win32
# Target compatibility:         ANSI SQL
# HeidiSQL version:             4.0
# Date/time:                    2024-03-06 00:37:18
# --------------------------------------------------------

/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ANSI,NO_BACKSLASH_ESCAPES';*/
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;*/


#
# Database structure for database 'todolist'
#

CREATE DATABASE /*!32312 IF NOT EXISTS*/ "todolist" /*!40100 DEFAULT CHARACTER SET latin1 */;

USE "todolist";


#
# Table structure for table 'admin'
#

CREATE TABLE /*!32312 IF NOT EXISTS*/ "admin" (
  "Userid" varchar(100) NOT NULL,
  "Pwd" varchar(100) NOT NULL
);



#
# Dumping data for table 'admin'
#

LOCK TABLES "admin" WRITE;
/*!40000 ALTER TABLE "admin" DISABLE KEYS;*/
REPLACE INTO "admin" ("Userid", "Pwd") VALUES
	('admin','admin');
/*!40000 ALTER TABLE "admin" ENABLE KEYS;*/
UNLOCK TABLES;


#
# Table structure for table 'dailylist'
#

CREATE TABLE /*!32312 IF NOT EXISTS*/ "dailylist" (
  "id" int(4) NOT NULL AUTO_INCREMENT,
  "Uid" varchar(100) NOT NULL,
  "Task" varchar(100) NOT NULL,
  "Tdate" varchar(100) NOT NULL,
  "Description" varchar(100) NOT NULL,
  PRIMARY KEY ("id")
) AUTO_INCREMENT=5;



#
# Dumping data for table 'dailylist'
#

LOCK TABLES "dailylist" WRITE;
/*!40000 ALTER TABLE "dailylist" DISABLE KEYS;*/
REPLACE INTO "dailylist" ("id", "Uid", "Task", "Tdate", "Description") VALUES
	(3,'nanda','Complete Task 2','6/3/2024','Complete Task 2 description');
REPLACE INTO "dailylist" ("id", "Uid", "Task", "Tdate", "Description") VALUES
	(4,'nanda','Complete Task 1','6/3/2024','Complete Task 1 description');
/*!40000 ALTER TABLE "dailylist" ENABLE KEYS;*/
UNLOCK TABLES;


#
# Table structure for table 'pills'
#

CREATE TABLE /*!32312 IF NOT EXISTS*/ "pills" (
  "id" int(4) NOT NULL AUTO_INCREMENT,
  "Uid" varchar(100) NOT NULL,
  "Pills" varchar(100) NOT NULL,
  "Status" varchar(100) NOT NULL,
  "Description" varchar(100) NOT NULL,
  PRIMARY KEY ("id")
) AUTO_INCREMENT=4;



#
# Dumping data for table 'pills'
#

LOCK TABLES "pills" WRITE;
/*!40000 ALTER TABLE "pills" DISABLE KEYS;*/
REPLACE INTO "pills" ("id", "Uid", "Pills", "Status", "Description") VALUES
	(1,'nanda','Take Paracetamol 500 mcg','Not Taken','Take Paracetamol 500 mcg');
REPLACE INTO "pills" ("id", "Uid", "Pills", "Status", "Description") VALUES
	(3,'nanda','Take Paracetamol 100 mcg','Not Taken','Take Paracetamol 100 mcg');
/*!40000 ALTER TABLE "pills" ENABLE KEYS;*/
UNLOCK TABLES;


#
# Table structure for table 'usertbl'
#

CREATE TABLE /*!32312 IF NOT EXISTS*/ "usertbl" (
  "id" int(10) unsigned NOT NULL AUTO_INCREMENT,
  "fname" varchar(100) NOT NULL,
  "Uid" varchar(100) NOT NULL,
  "Pwd" varchar(100) NOT NULL,
  "email_id" varchar(100) NOT NULL,
  "address" varchar(1000) NOT NULL,
  "mobile" varchar(100) NOT NULL,
  PRIMARY KEY ("id")
) AUTO_INCREMENT=5;



#
# Dumping data for table 'usertbl'
#

LOCK TABLES "usertbl" WRITE;
/*!40000 ALTER TABLE "usertbl" DISABLE KEYS;*/
REPLACE INTO "usertbl" ("id", "fname", "Uid", "Pwd", "email_id", "address", "mobile") VALUES
	('1','a','a','a','a@gmail.com','cbe','9003502338');
REPLACE INTO "usertbl" ("id", "fname", "Uid", "Pwd", "email_id", "address", "mobile") VALUES
	('2','Nanda kumar S','nanda','nanda','nandapoy@gmail.com','cbe','09629595205');
REPLACE INTO "usertbl" ("id", "fname", "Uid", "Pwd", "email_id", "address", "mobile") VALUES
	('3','raja','raja','raja','raja1@gmail.com','cbe','09629595205');
/*!40000 ALTER TABLE "usertbl" ENABLE KEYS;*/
UNLOCK TABLES;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE;*/
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;*/
