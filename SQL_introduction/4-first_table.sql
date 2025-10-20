-- Create a table in the current database in my SQL server
CREATE TABLE first_table (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) NOY NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMPS,
    PROMARY KEY (id)
)