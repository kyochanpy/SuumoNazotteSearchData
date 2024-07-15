SET NAMES 'utf8mb4';

DROP DATABASE IF EXISTS test_map_ui;
CREATE DATABASE test_map_ui;
USE test_map_ui;

CREATE TABLE master (
    id INT AUTO_INCREMENT PRIMARY KEY,
    type VARCHAR(255) NOT NULL,
    name VARCHAR(255) NOT NULL,
    address VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    location GEOMETRY NOT NULL
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
