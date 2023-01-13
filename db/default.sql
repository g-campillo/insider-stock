CREATE DATABASE IF NOT EXISTS app;

USE app;

DROP TABLE IF EXISTS `trades`;

CREATE TABLE `trades` (
  `id` int NOT NULL AUTO_INCREMENT,
  `filingDate` datetime DEFAULT NULL,
  `tradeDate` date DEFAULT NULL,
  `ticker` varchar(8) DEFAULT NULL,
  `companyName` varchar(256) DEFAULT NULL,
  `insiderName` varchar(128) DEFAULT NULL,
  `insiderTitle` varchar(64) DEFAULT NULL,
  `tradeType` varchar(64) DEFAULT NULL,
  `price` decimal(13,2) DEFAULT NULL,
  `qty` int DEFAULT NULL,
  `owned` int DEFAULT NULL,
  `deltaOwned` int DEFAULT NULL,
  `value` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `filingDate` (`filingDate`,`tradeDate`,`ticker`,`companyName`,`insiderName`,`insiderTitle`,`tradeType`,`price`,`qty`,`owned`,`deltaOwned`,`value`)
);