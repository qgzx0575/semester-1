PRAGMA foreign_keys = ON;

/*
CREATE TABLE Branch (
    branch_id INTEGER PRIMARY KEY,
    street TEXT NOT NULL,
    city TEXT NOT NULL,
    postcode TEXT NOT NULL
);

CREATE TABLE Staff (
    staff_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    role TEXT,
    branch_id INTEGER,
    FOREIGN KEY (branch_id) REFERENCES Branch(branch_id)
);
*/

-- SELECT * FROM Staff;

-- INSERT INTO Branch (branch_id, street, city, postcode) VALUES (1, 'Shaw Line', 'Leeds', 'LS6 5UL');

-- INSERT INTO Staff (staff_id, name, role, branch_id) VALUES (101, 'Tom', NULL, NULL);

-- UPDATE Staff SET role='Manager' WHERE staff_id=101;
-- UPDATE Staff SET branch_id=1 WHERE staff_id=101;

-- INSERT INTO Branch (branch_id, street, city, postcode) VALUES (2, 'Thaw Line', 'Deeds', 'LS2 9JT');

-- INSERT INTO Staff (staff_id, name, role, branch_id) VALUES (102, 'Jerry', 'Cashier', 1);

-- INSERT INTO Staff (staff_id, name, role, branch_id) VALUES (103, 'Spike', 'Manager', 2);

-- INSERT INTO Staff (staff_id, name, role, branch_id) VALUES (104, 'Evil Tom', 'Cashier', 2);

-- INSERT INTO Branch (branch_id, street, city, postcode) VALUES (2, 'Daw Line', 'Reeds', 'LS2 8NG'); -- This will fail because branch_id 2 already exists

-- INSERT INTO Branch (branch_id, street, city, postcode) VALUES (3, 'Daw Line', NULL, 'LS2 8NG'); -- This will fail because city is NULL

-- SELECT * FROM Staff WHERE role='Manager';
-- SELECT * FROM Staff WHERE branch_id=1;