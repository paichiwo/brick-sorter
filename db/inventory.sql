BEGIN TRANSACTION;

CREATE TABLE Inventory (
    part_number VARCHAR(50) PRIMARY KEY,
    part_name VARCHAR(150),
    color VARCHAR(50),
    amount INTEGER,
    box VARCHAR(10)
);

COMMIT;
