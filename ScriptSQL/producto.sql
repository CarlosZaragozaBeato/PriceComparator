/*
 Navicat Premium Data Transfer

 Source Server         : Prueba
 Source Server Type    : MySQL
 Source Server Version : 80032 (8.0.32)
 Source Host           : localhost:3306
 Source Schema         : comparador_precios

 Target Server Type    : MySQL
 Target Server Version : 80032 (8.0.32)
 File Encoding         : 65001

 Date: 11/03/2023 18:02:45
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for producto
-- ----------------------------
DROP TABLE IF EXISTS `producto`;
CREATE TABLE `producto`  (
  `ID_PRODUCTO` int NOT NULL AUTO_INCREMENT,
  `NOMBRE` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `PRECIO` float NULL DEFAULT NULL,
  `ULTIMA_ACTUALIZACION` timestamp NOT NULL,
  `ID_SUPERMERCADO` int NULL DEFAULT NULL,
  PRIMARY KEY (`ID_PRODUCTO`) USING BTREE,
  UNIQUE INDEX `ID_PRODUCTO`(`ID_PRODUCTO` ASC) USING BTREE,
  INDEX `ID_SUPERMERCADO`(`ID_SUPERMERCADO` ASC) USING BTREE,
  CONSTRAINT `producto_ibfk_1` FOREIGN KEY (`ID_SUPERMERCADO`) REFERENCES `supermercado` (`ID_SUPERMERCADO`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 153 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
