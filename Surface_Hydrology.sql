-- --------------------------------------------------------
-- 主機:                           35.187.158.20
-- 伺服器版本:                        5.7.14-google-log - (Google)
-- 伺服器操作系統:                      Linux
-- HeidiSQL 版本:                  9.5.0.5196
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- 傾印 LHC_tem 的資料庫結構
CREATE DATABASE IF NOT EXISTS `LHC_tem` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `LHC_tem`;

-- 傾印  表格 LHC_tem.django_migrations 結構
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 取消選取資料匯出。
-- 傾印  表格 LHC_tem.members 結構
CREATE TABLE IF NOT EXISTS `members` (
  `pid` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(10) NOT NULL COMMENT '名字',
  `type` varchar(10) NOT NULL COMMENT '成員屬性',
  `master_graduation_year` int(11) DEFAULT NULL COMMENT '碩士畢業年份',
  `master_disseration_title` varchar(100) DEFAULT NULL COMMENT '碩士論文題目',
  `master_disseration_url` varchar(150) DEFAULT NULL COMMENT '碩士論文連結',
  `doctor_graduation_year` int(11) DEFAULT NULL COMMENT '博士畢業年份',
  `doctor_disseration_title` varchar(150) DEFAULT NULL COMMENT '博士論文題目',
  `doctor_disseration_url` varchar(150) DEFAULT NULL COMMENT '博士論文連結',
  PRIMARY KEY (`pid`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8;

-- 取消選取資料匯出。
-- 傾印  表格 LHC_tem.papers 結構
CREATE TABLE IF NOT EXISTS `papers` (
  `pid` int(11) NOT NULL AUTO_INCREMENT,
  `author` varchar(200) NOT NULL COMMENT '作者',
  `date` varchar(7) NOT NULL DEFAULT 'yyyy/mm' COMMENT '發表年月',
  `title` varchar(500) NOT NULL COMMENT '題目與期刊',
  PRIMARY KEY (`pid`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;

-- 取消選取資料匯出。
-- 傾印  表格 LHC_tem.RAWDATA_Capa2 結構
CREATE TABLE IF NOT EXISTS `RAWDATA_Capa2` (
  `TIMESTAMP` datetime NOT NULL,
  `T0` decimal(5,2) DEFAULT NULL COMMENT '(0cm)溫度(Deg C)',
  `T10` decimal(5,2) DEFAULT NULL COMMENT '(-10cm)溫度(Deg C)',
  `T30` decimal(5,2) DEFAULT NULL COMMENT '(-30cm)溫度(Deg C)',
  `T50` decimal(5,2) DEFAULT NULL COMMENT '(-50cm)溫度(Deg C)',
  `T150` decimal(5,2) DEFAULT NULL COMMENT '(-150cm)溫度(Deg C)',
  `SF10` decimal(3,3) DEFAULT NULL COMMENT '(-10cm)土壤含水量',
  `SF30` decimal(3,3) DEFAULT NULL COMMENT '(-30cm)土壤含水量',
  `SF50` decimal(3,3) DEFAULT NULL COMMENT '(-50cm)土壤含水量',
  `SF70` decimal(3,3) DEFAULT NULL COMMENT '(-70cm)土壤含水量',
  `SF90` decimal(3,3) DEFAULT NULL COMMENT '(-90cm)土壤含水量',
  `ReceiveDate` date NOT NULL COMMENT '收數據日期',
  PRIMARY KEY (`TIMESTAMP`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 取消選取資料匯出。
-- 傾印  表格 LHC_tem.RAWDATA_Capa3 結構
CREATE TABLE IF NOT EXISTS `RAWDATA_Capa3` (
  `TIMESTAMP` datetime NOT NULL,
  `T0` decimal(5,2) DEFAULT NULL COMMENT '(0cm)溫度(Deg C)',
  `T10` decimal(5,2) DEFAULT NULL COMMENT '(-10cm)溫度(Deg C)',
  `T30` decimal(5,2) DEFAULT NULL COMMENT '(-30cm)溫度(Deg C)',
  `T50` decimal(5,2) DEFAULT NULL COMMENT '(-50cm)溫度(Deg C)',
  `SF10` decimal(3,3) DEFAULT NULL COMMENT '(-10cm)土壤含水量',
  `SF30` decimal(3,3) DEFAULT NULL COMMENT '(-30cm)土壤含水量',
  `SF50` decimal(3,3) DEFAULT NULL COMMENT '(-50cm)土壤含水量',
  `SF70` decimal(3,3) DEFAULT NULL COMMENT '(-70cm)土壤含水量',
  `SF90` decimal(3,3) DEFAULT NULL COMMENT '(-90cm)土壤含水量',
  `ReceiveDate` date NOT NULL COMMENT '收數據日期',
  PRIMARY KEY (`TIMESTAMP`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 取消選取資料匯出。
-- 傾印  表格 LHC_tem.RAWDATA_Capa4 結構
CREATE TABLE IF NOT EXISTS `RAWDATA_Capa4` (
  `TIMESTAMP` datetime NOT NULL,
  `WS_ms_Avg` decimal(6,3) DEFAULT NULL COMMENT '水平風速(meters/second)',
  `WindDir` decimal(6,3) DEFAULT NULL COMMENT '風向(Degrees)',
  `AirTC_20_Avg` decimal(5,3) DEFAULT NULL COMMENT '20m溫度(Deg C)',
  `RH_20` decimal(6,3) DEFAULT NULL COMMENT '20m濕度(%)',
  `AirTC_15_Avg` decimal(5,3) DEFAULT NULL COMMENT '15m溫度(Deg C)',
  `RH_15` decimal(6,3) DEFAULT NULL COMMENT '15m濕度(%)',
  `AirTC_10_Avg` decimal(5,3) DEFAULT NULL COMMENT '10m溫度(Deg C)',
  `RH_10` decimal(6,3) DEFAULT NULL COMMENT '10m濕度(%)',
  `AirTC_5_Avg` decimal(5,3) DEFAULT NULL COMMENT '5m溫度(Deg C)',
  `RH_5` decimal(6,3) DEFAULT NULL COMMENT '5m濕度(%)',
  `NR_Wm2_Avg` decimal(9,3) DEFAULT NULL COMMENT '淨輻射(Watts/meter)',
  `SEVolt_Avg` decimal(7,4) DEFAULT NULL COMMENT '地熱通量(mV)',
  `Temp_C_Avg_1` decimal(5,3) DEFAULT NULL COMMENT '(0cm)溫度(Deg C)',
  `Temp_C_Avg_2` decimal(5,3) DEFAULT NULL COMMENT '(-10cm)溫度(Deg C)',
  `Temp_C_Avg_3` decimal(5,3) DEFAULT NULL COMMENT '(-30cm)溫度(Deg C)',
  `Temp_C_Avg_4` decimal(5,3) DEFAULT NULL COMMENT '(-50cm)溫度(Deg C)',
  `Temp_C_Avg_5` decimal(5,3) DEFAULT NULL COMMENT '(-70cm)溫度(Deg C)',
  `Temp_C_Avg_6` decimal(5,3) DEFAULT NULL COMMENT '(-90cm)溫度(Deg C)',
  `Result1_Avg` decimal(4,4) DEFAULT NULL COMMENT '(-10cm)土壤含水量',
  `Result2_Avg` decimal(4,4) DEFAULT NULL COMMENT '(-30cm)土壤含水量',
  `Result3_Avg` decimal(4,4) DEFAULT NULL COMMENT '(-50cm)土壤含水量',
  `Result4_Avg` decimal(4,4) DEFAULT NULL COMMENT '(-70cm)土壤含水量',
  `Result5_Avg` decimal(4,4) DEFAULT NULL COMMENT '(-90cm)土壤含水量',
  `Inf_data` decimal(6,2) DEFAULT NULL COMMENT '入滲(mV)',
  `Temp_C_Avg_7` decimal(5,3) DEFAULT NULL COMMENT '(-150cm)溫度(Deg C)',
  `Rain_mm_Tot` decimal(6,2) DEFAULT NULL COMMENT '雨量(mm)',
  `Pressure_Avg` decimal(8,4) DEFAULT NULL COMMENT '氣壓(hPa)',
  `ReceiveDate` date NOT NULL COMMENT '收數據日期',
  PRIMARY KEY (`TIMESTAMP`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 取消選取資料匯出。
-- 傾印  表格 LHC_tem.work_experience 結構
CREATE TABLE IF NOT EXISTS `work_experience` (
  `pid` int(11) NOT NULL AUTO_INCREMENT,
  `unit` varchar(50) NOT NULL COMMENT '單位',
  `department` varchar(50) DEFAULT NULL COMMENT '部門',
  `title` varchar(50) NOT NULL COMMENT '職稱',
  `start_Year` int(10) unsigned NOT NULL COMMENT '起始年分',
  `end_Year` int(10) unsigned DEFAULT NULL COMMENT '結束年分',
  PRIMARY KEY (`pid`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;

-- 取消選取資料匯出。
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
