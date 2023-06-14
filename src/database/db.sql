CREATE DATABASE db_OpenCvRoboXYZDell DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci;

CREATE TABLE IF NOT EXISTS `parametersAdjustFilterImg`(
    id          INT NOT NULL AUTO_INCREMENT,
    name        CHAR(50), 
    parameter01 INT,
    parameter02 INT,
    parameter03 INT,
    parameter04 INT,
    parameter05 INT,
    parameter06 INT,
    parameter07 INT,
    parameter08 INT,
    parameter09 INT,
    parameter10 INT,
    parameter11 INT,
    parameter12 INT,
    parameter13 INT,
    parameter14 INT,
    parameter15 INT,
    parameter16 INT,
    parameter17 INT,
    parameter18 INT,
    parameter19 INT,
    parameter20 INT,
    PRIMARY KEY(id)
);

CREATE TABLE IF NOT EXISTS `parameterstest`(
    id          INT(4) UNSIGNED ZEROFILL NOT NULL AUTO_INCREMENT,
    name        CHAR(50), 
    parameter01 INT,
    parameter02 INT,
    PRIMARY KEY(id)
);

