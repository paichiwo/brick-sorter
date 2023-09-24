BEGIN TRANSACTION;

CREATE TABLE Inventory (
    part_number VARCHAR(50) PRIMARY KEY,
    parent_id VARCHAR(50),
    color VARCHAR(50),
    amount INTEGER,
    box VARCHAR(10)
);

COMMIT;

