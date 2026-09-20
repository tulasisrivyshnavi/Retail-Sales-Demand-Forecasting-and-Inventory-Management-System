-- ============================================================
-- create_database.sql
-- Run this ONCE in MySQL Workbench or CLI to create the DB.
-- ============================================================

CREATE DATABASE IF NOT EXISTS retail_forecast_db
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

-- Create an application user (safer than using root)
-- Change 'app_password' to something strong.
CREATE USER IF NOT EXISTS 'retail_app'@'localhost'
    IDENTIFIED BY 'app_password';

GRANT ALL PRIVILEGES ON retail_forecast_db.*
    TO 'retail_app'@'localhost';

FLUSH PRIVILEGES;

SELECT 'Database retail_forecast_db created successfully.' AS message;
