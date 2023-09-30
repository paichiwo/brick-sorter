BEGIN TRANSACTION;

CREATE TABLE Inventory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    part_number VARCHAR(50),
    part_name VARCHAR(150),
    color VARCHAR(50),
    amount INTEGER,
    box VARCHAR(10)
);

COMMIT;
