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
-- Table `BiblioLexicusDB`.`Ouvrages`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `BiblioLexicusDB`.`Ouvrages` (
  `ID_Ouvrages` VARCHAR(16) NOT NULL,
  `Nom_Ouvrage` VARCHAR(50) NOT NULL,
  `Nom_Auteur` VARCHAR(250) NOT NULL,
  `Annee_Publication` DATE NOT NULL,
  `Maison_Edition` VARCHAR(45) NOT NULL,
  `ID_Bibliotheque` VARCHAR(2) NOT NULL,
  `Pages_ou_Duree` INT UNSIGNED NULL,
  `Resume` NVARCHAR(2000) NOT NULL,
  `Genre` VARCHAR(2) NOT NULL,
  `Langue` VARCHAR(18) NOT NULL,
  `Disponibilite` BIT NOT NULL,
  `Numero_Copie` INT NOT NULL,
  `Type_Ouvrage` VARCHAR(2) NOT NULL,
  PRIMARY KEY (`ID_Ouvrages`),
  UNIQUE INDEX `idOuvrages_UNIQUE` (`ID_Ouvrages` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `BiblioLexicusDB`.`Donnees_Bibiliotheque`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `BiblioLexicusDB`.`Donnees_Bibiliotheque` (
  `ID_Ouvrages` VARCHAR(2) NOT NULL,
  `ID_Utilistateurs` VARCHAR(16) NOT NULL,
  `Heure_Ouverture` VARCHAR(11) NOT NULL,
  `CodePostale` VARCHAR(6) NOT NULL,
  `Site_Internet_Bibliotheque` VARCHAR(45) NOT NULL,
  `Numero_Telephone` VARCHAR(14) NOT NULL,
  PRIMARY KEY (`ID_Ouvrages`),
  UNIQUE INDEX `ID_Bibiliotheque_UNIQUE` (`ID_Ouvrages` ASC) VISIBLE,
  UNIQUE INDEX `ID_Users_UNIQUE` (`ID_Utilistateurs` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `BiblioLexicusDB`.`Donnees_Bibiliotheque_has_Ouvrages`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `BiblioLexicusDB`.`Donnees_Bibiliotheque_has_Ouvrages` (
  `Donnees_Bibiliotheque_ID_Ouvrages` VARCHAR(2) NOT NULL,
  `Ouvrages_ID_Ouvrages` VARCHAR(16) NOT NULL,
  PRIMARY KEY (`Donnees_Bibiliotheque_ID_Ouvrages`, `Ouvrages_ID_Ouvrages`),
  INDEX `fk_Donnees_Bibiliotheque_has_Ouvrages_Ouvrages1_idx` (`Ouvrages_ID_Ouvrages` ASC) VISIBLE,
  INDEX `fk_Donnees_Bibiliotheque_has_Ouvrages_Donnees_Bibiliotheque_idx` (`Donnees_Bibiliotheque_ID_Ouvrages` ASC) VISIBLE,
  CONSTRAINT `fk_Donnees_Bibiliotheque_has_Ouvrages_Donnees_Bibiliotheque`
    FOREIGN KEY (`Donnees_Bibiliotheque_ID_Ouvrages`)
    REFERENCES `BiblioLexicusDB`.`Donnees_Bibiliotheque` (`ID_Ouvrages`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Donnees_Bibiliotheque_has_Ouvrages_Ouvrages1`
    FOREIGN KEY (`Ouvrages_ID_Ouvrages`)
    REFERENCES `BiblioLexicusDB`.`Ouvrages` (`ID_Ouvrages`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `BiblioLexicusDB`.`Liste_Utilisateurs`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `BiblioLexicusDB`.`Liste_Utilisateurs` (
  `ID_Utilisateurs` VARCHAR(16) NOT NULL,
  `Nom` VARCHAR(50) NOT NULL,
  `Prenom` VARCHAR(100) NOT NULL,
  `Date_Naissance` DATE NOT NULL,
  `Frais_Dossier` DECIMAL UNSIGNED NOT NULL DEFAULT 0,
  `Courriel` VARCHAR(320) NOT NULL,
  `Addresse_Postale` VARCHAR(6) NOT NULL,
  `Expiration_Abonnement` DATE NOT NULL,
  `Permissions` VARCHAR(2) NOT NULL DEFAULT '00',
  PRIMARY KEY (`ID_Utilisateurs`),
  UNIQUE INDEX `Courriel_UNIQUE` (`Courriel` ASC) VISIBLE,
  UNIQUE INDEX `ID_Utilisateur_UNIQUE` (`ID_Utilisateurs` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `BiblioLexicusDB`.`Ouvrages_Emprunte`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `BiblioLexicusDB`.`Ouvrages_Emprunte` (
  `ID_Ouvrages` VARCHAR(16) NOT NULL,
  `Date_Retour` DATE NOT NULL,
  `ID_Utilisateurs` VARCHAR(16) NOT NULL,
  PRIMARY KEY (`ID_Ouvrages`),
  UNIQUE INDEX `ID_Ouvrage_UNIQUE` (`ID_Ouvrages` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `BiblioLexicusDB`.`Commentaires`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `BiblioLexicusDB`.`Commentaires` (
  `ID_Commentaire` INT NOT NULL,
  `ID_Ouvrages` VARCHAR(16) NOT NULL,
  `ID_Utilisateurs` VARCHAR(16) NOT NULL,
  `Date_Publication` DATETIME NOT NULL,
  `Texte_Commentaire` TINYTEXT NOT NULL,
  PRIMARY KEY (`ID_Commentaire`),
  UNIQUE INDEX `ID_Commentaire_UNIQUE` (`ID_Commentaire` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `BiblioLexicusDB`.`Liste_Utilisateurs_has_Donnees_Bibiliotheque`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `BiblioLexicusDB`.`Liste_Utilisateurs_has_Donnees_Bibiliotheque` (
  `Liste_Utilisateurs_ID_Utilisateurs` VARCHAR(16) NOT NULL,
  `Donnees_Bibiliotheque_ID_Ouvrages` VARCHAR(2) NOT NULL,
  PRIMARY KEY (`Liste_Utilisateurs_ID_Utilisateurs`, `Donnees_Bibiliotheque_ID_Ouvrages`),
  INDEX `fk_Liste_Utilisateurs_has_Donnees_Bibiliotheque_Donnees_Bib_idx` (`Donnees_Bibiliotheque_ID_Ouvrages` ASC) VISIBLE,
  INDEX `fk_Liste_Utilisateurs_has_Donnees_Bibiliotheque_Liste_Utili_idx` (`Liste_Utilisateurs_ID_Utilisateurs` ASC) VISIBLE,
  CONSTRAINT `fk_Liste_Utilisateurs_has_Donnees_Bibiliotheque_Liste_Utilisa1`
    FOREIGN KEY (`Liste_Utilisateurs_ID_Utilisateurs`)
    REFERENCES `BiblioLexicusDB`.`Liste_Utilisateurs` (`ID_Utilisateurs`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Liste_Utilisateurs_has_Donnees_Bibiliotheque_Donnees_Bibil1`
    FOREIGN KEY (`Donnees_Bibiliotheque_ID_Ouvrages`)
    REFERENCES `BiblioLexicusDB`.`Donnees_Bibiliotheque` (`ID_Ouvrages`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `BiblioLexicusDB`.`Commentaires_has_Liste_Utilisateurs`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `BiblioLexicusDB`.`Commentaires_has_Liste_Utilisateurs` (
  `Commentaires_ID_Commentaire` INT NOT NULL,
  `Liste_Utilisateurs_ID_Utilisateurs` VARCHAR(16) NOT NULL,
  PRIMARY KEY (`Commentaires_ID_Commentaire`, `Liste_Utilisateurs_ID_Utilisateurs`),
  INDEX `fk_Commentaires_has_Liste_Utilisateurs_Liste_Utilisateurs1_idx` (`Liste_Utilisateurs_ID_Utilisateurs` ASC) VISIBLE,
  INDEX `fk_Commentaires_has_Liste_Utilisateurs_Commentaires1_idx` (`Commentaires_ID_Commentaire` ASC) VISIBLE,
  CONSTRAINT `fk_Commentaires_has_Liste_Utilisateurs_Commentaires1`
    FOREIGN KEY (`Commentaires_ID_Commentaire`)
    REFERENCES `BiblioLexicusDB`.`Commentaires` (`ID_Commentaire`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Commentaires_has_Liste_Utilisateurs_Liste_Utilisateurs1`
    FOREIGN KEY (`Liste_Utilisateurs_ID_Utilisateurs`)
    REFERENCES `BiblioLexicusDB`.`Liste_Utilisateurs` (`ID_Utilisateurs`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `BiblioLexicusDB`.`Commentaires_has_Ouvrages`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `BiblioLexicusDB`.`Commentaires_has_Ouvrages` (
  `Commentaires_ID_Commentaire` INT NOT NULL,
  `Ouvrages_ID_Ouvrages` VARCHAR(16) NOT NULL,
  PRIMARY KEY (`Commentaires_ID_Commentaire`, `Ouvrages_ID_Ouvrages`),
  INDEX `fk_Commentaires_has_Ouvrages_Ouvrages1_idx` (`Ouvrages_ID_Ouvrages` ASC) VISIBLE,
  INDEX `fk_Commentaires_has_Ouvrages_Commentaires1_idx` (`Commentaires_ID_Commentaire` ASC) VISIBLE,
  CONSTRAINT `fk_Commentaires_has_Ouvrages_Commentaires1`
    FOREIGN KEY (`Commentaires_ID_Commentaire`)
    REFERENCES `BiblioLexicusDB`.`Commentaires` (`ID_Commentaire`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Commentaires_has_Ouvrages_Ouvrages1`
    FOREIGN KEY (`Ouvrages_ID_Ouvrages`)
    REFERENCES `BiblioLexicusDB`.`Ouvrages` (`ID_Ouvrages`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `BiblioLexicusDB`.`Liste_Utilisateurs_has_Ouvrages_Emprunte`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `BiblioLexicusDB`.`Liste_Utilisateurs_has_Ouvrages_Emprunte` (
  `Liste_Utilisateurs_ID_Utilisateurs` VARCHAR(16) NOT NULL,
  `Ouvrages_Emprunte_ID_Ouvrages` VARCHAR(16) NOT NULL,
  PRIMARY KEY (`Liste_Utilisateurs_ID_Utilisateurs`, `Ouvrages_Emprunte_ID_Ouvrages`),
  INDEX `fk_Liste_Utilisateurs_has_Ouvrages_Emprunte_Ouvrages_Emprun_idx` (`Ouvrages_Emprunte_ID_Ouvrages` ASC) VISIBLE,
  INDEX `fk_Liste_Utilisateurs_has_Ouvrages_Emprunte_Liste_Utilisate_idx` (`Liste_Utilisateurs_ID_Utilisateurs` ASC) VISIBLE,
  CONSTRAINT `fk_Liste_Utilisateurs_has_Ouvrages_Emprunte_Liste_Utilisateurs1`
    FOREIGN KEY (`Liste_Utilisateurs_ID_Utilisateurs`)
    REFERENCES `BiblioLexicusDB`.`Liste_Utilisateurs` (`ID_Utilisateurs`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Liste_Utilisateurs_has_Ouvrages_Emprunte_Ouvrages_Emprunte1`
    FOREIGN KEY (`Ouvrages_Emprunte_ID_Ouvrages`)
    REFERENCES `BiblioLexicusDB`.`Ouvrages_Emprunte` (`ID_Ouvrages`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `BiblioLexicusDB`.`Ouvrages_has_Ouvrages_Emprunte`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `BiblioLexicusDB`.`Ouvrages_has_Ouvrages_Emprunte` (
  `Ouvrages_ID_Ouvrages` VARCHAR(16) NOT NULL,
  `Ouvrages_Emprunte_ID_Ouvrages` VARCHAR(16) NOT NULL,
  PRIMARY KEY (`Ouvrages_ID_Ouvrages`, `Ouvrages_Emprunte_ID_Ouvrages`),
  INDEX `fk_Ouvrages_has_Ouvrages_Emprunte_Ouvrages_Emprunte1_idx` (`Ouvrages_Emprunte_ID_Ouvrages` ASC) VISIBLE,
  INDEX `fk_Ouvrages_has_Ouvrages_Emprunte_Ouvrages1_idx` (`Ouvrages_ID_Ouvrages` ASC) VISIBLE,
  CONSTRAINT `fk_Ouvrages_has_Ouvrages_Emprunte_Ouvrages1`
    FOREIGN KEY (`Ouvrages_ID_Ouvrages`)
    REFERENCES `BiblioLexicusDB`.`Ouvrages` (`ID_Ouvrages`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Ouvrages_has_Ouvrages_Emprunte_Ouvrages_Emprunte1`
    FOREIGN KEY (`Ouvrages_Emprunte_ID_Ouvrages`)
    REFERENCES `BiblioLexicusDB`.`Ouvrages_Emprunte` (`ID_Ouvrages`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
