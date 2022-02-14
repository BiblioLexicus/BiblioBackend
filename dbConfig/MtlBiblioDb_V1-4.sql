-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema BiblioLexicusDB
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema BiblioLexicusDB
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `BiblioLexicusDB` DEFAULT CHARACTER SET utf8 ;
USE `BiblioLexicusDB` ;

-- -----------------------------------------------------
-- Table `BiblioLexicusDB`.`Work_List`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `BiblioLexicusDB`.`Work_List` (
  `ID_Works` VARCHAR(16) NOT NULL,
  `Name_Works` VARCHAR(50) NOT NULL,
  `Author_Name` VARCHAR(250) NOT NULL,
  `Publication_Date` DATE NOT NULL,
  `Edition_House` VARCHAR(45) NOT NULL,
  `ID_Library` VARCHAR(2) NOT NULL,
  `Length` INT UNSIGNED NOT NULL,
  `Resume` NVARCHAR(2000) NOT NULL,
  `Genre` VARCHAR(2) NOT NULL,
  `Language` VARCHAR(18) NOT NULL,
  `State` BIT NOT NULL,
  `Copy_Number` INT UNSIGNED NOT NULL,
  `Type_Work` VARCHAR(2) NOT NULL,
  `Price` DECIMAL(10,4) UNSIGNED NOT NULL,
  PRIMARY KEY (`ID_Works`, `ID_Library`),
  UNIQUE INDEX `idWorks_UNIQUE` (`ID_Works` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `BiblioLexicusDB`.`Libraries_Data`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `BiblioLexicusDB`.`Libraries_Data` (
  `ID_Users` VARCHAR(16) NOT NULL,
  `Schedule` VARCHAR(11) NOT NULL,
  `Postal_Code` VARCHAR(6) NOT NULL,
  `Library_Website` VARCHAR(45) NOT NULL,
  `Phone_Address` VARCHAR(14) NOT NULL,
  `Library_Name` VARCHAR(45) NULL,
  `ID_Library` VARCHAR(2) NOT NULL,
  PRIMARY KEY (`ID_Library`),
  CONSTRAINT `fk_Donnees_Bibiliotheque_Work_List1`
    FOREIGN KEY (`ID_Library`)
    REFERENCES `BiblioLexicusDB`.`Work_List` (`ID_Library`)
    --avant, ici c'était on delete delete...  mais on verra si cest mieux presentement
    ON DELETE CASCADE
    ON UPDATE CASCADE,
CONSTRAINT `fk_Donnees_Bibiliotheque_User_List1`
    FOREIGN KEY (`ID_Users`)
    REFERENCES `BiblioLexicusDB`.`User_List` (`ID_Users`)      
    --avant, ici c'était on delete delete...  mais on verra si cest mieux presentement... même commentaire que plus haut

    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `BiblioLexicusDB`.`User_List`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `BiblioLexicusDB`.`User_List` (
  `ID_Users` VARCHAR(16) NOT NULL,
  `Name` VARCHAR(50) NOT NULL,
  `First_Name` VARCHAR(100) NOT NULL,
  `Date_Birth` DATE NOT NULL,
  `Fees` DECIMAL UNSIGNED NOT NULL DEFAULT 0,
  `Email` VARCHAR(320) NOT NULL,
  `Addresse_Postale` VARCHAR(6) NOT NULL,
  `Expiration_Subscription` DATE NOT NULL,
  `Permissions` VARCHAR(2) NOT NULL DEFAULT '00',
  `Related_Library_ID` VARCHAR(2),
  PRIMARY KEY (`ID_Users`),
  UNIQUE INDEX `Email_UNIQUE` (`Email` ASC) VISIBLE,
  UNIQUE INDEX `ID_Users_UNIQUE` (`ID_Users` ASC) VISIBLE)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `BiblioLexicusDB`.`Loaned_Works`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `BiblioLexicusDB`.`Loaned_Works` (
  `ID_Works` VARCHAR(16) NOT NULL,
  `End_Loan_Date` DATE NOT NULL,
  `ID_Users` VARCHAR(16) NOT NULL,
  `Work_Lost` BIT NOT NULL,
  PRIMARY KEY (`ID_Works`, `ID_Users`),
  UNIQUE INDEX `ID_Works_UNIQUE` (`ID_Works` ASC) VISIBLE,
  INDEX `fk_Ouvrages_Emprunte_User_List1_idx` (`ID_Users` ASC) VISIBLE,
  CONSTRAINT `fk_Ouvrages_Emprunte_Work_List`
    FOREIGN KEY (`ID_Works`)
    REFERENCES `BiblioLexicusDB`.`Work_List` (`ID_Works`)
    ON DELETE NO ACTION
    ON UPDATE CASCADE,
  CONSTRAINT `fk_Ouvrages_Emprunte_User_List1`
    FOREIGN KEY (`ID_Users`)
    REFERENCES `BiblioLexicusDB`.`User_List` (`ID_Users`)
    ON DELETE NO ACTION
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `BiblioLexicusDB`.`Comments`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `BiblioLexicusDB`.`Comments` (
  `ID_Comments` INT NOT NULL,
  `ID_Works` VARCHAR(16) NOT NULL,
  `ID_Users` VARCHAR(16) NOT NULL,
  `Release_Date` DATETIME NOT NULL,
  `Comment_Text` TINYTEXT NOT NULL,
  PRIMARY KEY (`ID_Comments`, `ID_Works`, `ID_Users`),
  UNIQUE INDEX `ID_Commentaire_UNIQUE` (`ID_Comments` ASC) VISIBLE,
  INDEX `fk_Commentaires_Work_List1_idx` (`ID_Works` ASC) VISIBLE,
  INDEX `fk_Commentaires_User_List1_idx` (`ID_Users` ASC) VISIBLE,
  CONSTRAINT `fk_Commentaires_Work_List1`
    FOREIGN KEY (`ID_Works`)
    REFERENCES `BiblioLexicusDB`.`Work_List` (`ID_Works`)
    ON DELETE NO ACTION
    ON UPDATE CASCADE,
  CONSTRAINT `fk_Commentaires_User_List1`
    FOREIGN KEY (`ID_Users`)
    REFERENCES `BiblioLexicusDB`.`User_List` (`ID_Users`)
    ON DELETE NO ACTION
    ON UPDATE CASCADE)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;



INSERT INTO `BiblioLexicusDB`.`Works` 
VALUES (OO12121234567801,randomTitle,randomName,2001-01-01,randomEditionHouse,1L,256,bla bla bla uiyguyftr6r,FA,Fr,0,1,Mo,0.15,2)
