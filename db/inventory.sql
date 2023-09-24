BEGIN TRANSACTION;

CREATE TABLE Inventory (
    part_number VARCHAR(50) PRIMARY KEY,
    color VARCHAR(50),
    amount INTEGER,
    box VARCHAR(10)
);

COMMIT;
