-- =========================================================
--        SBI HYDERABAD BANK MANAGEMENT SYSTEM
-- =========================================================

-- =========================================================
-- CREATE DATABASE
-- =========================================================

CREATE DATABASE sbi_hyderabad_bank;

-- =========================================================
-- CONNECT DATABASE
-- =========================================================

--\c sbi_hyderabad_bank;

-- =========================================================
-- DROP OLD TABLES
-- =========================================================

DROP TABLE IF EXISTS transaction_details CASCADE;
DROP TABLE IF EXISTS loan CASCADE;
DROP TABLE IF EXISTS bank_account CASCADE;
DROP TABLE IF EXISTS customer CASCADE;
DROP TABLE IF EXISTS employees CASCADE;
DROP TABLE IF EXISTS branch CASCADE;
DROP TABLE IF EXISTS bank CASCADE;

-- =========================================================
-- CREATE BANK TABLE
-- =========================================================

CREATE TABLE bank (
    bank_id SERIAL PRIMARY KEY,
    bank_name VARCHAR(100) NOT NULL,
    bank_address TEXT NOT NULL
);

-- =========================================================
-- CREATE BRANCH TABLE
-- =========================================================

CREATE TABLE branch (
    branch_id SERIAL PRIMARY KEY,
    branch_name VARCHAR(100) NOT NULL,
    address TEXT NOT NULL,
    ifsc_code VARCHAR(20) UNIQUE NOT NULL,
    bank_id INT NOT NULL,

    CONSTRAINT fk_bank
    FOREIGN KEY(bank_id)
    REFERENCES bank(bank_id)
    ON DELETE CASCADE
);

-- =========================================================
-- CREATE EMPLOYEES TABLE
-- =========================================================

CREATE TABLE employees (
    employee_id SERIAL PRIMARY KEY,
    employee_name VARCHAR(100) NOT NULL,
    employee_gender VARCHAR(10),
    employee_mobile VARCHAR(15) UNIQUE,
    employee_age INT,
    employee_address TEXT,
    branch_id INT NOT NULL,

    CONSTRAINT fk_employee_branch
    FOREIGN KEY(branch_id)
    REFERENCES branch(branch_id)
    ON DELETE CASCADE
);

-- =========================================================
-- CREATE CUSTOMER TABLE
-- =========================================================

CREATE TABLE customer (
    customer_id SERIAL PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    customer_gender VARCHAR(10),
    customer_mobile VARCHAR(15) UNIQUE,
    customer_age INT,
    customer_address TEXT,
    branch_id INT NOT NULL,

    CONSTRAINT fk_customer_branch
    FOREIGN KEY(branch_id)
    REFERENCES branch(branch_id)
    ON DELETE CASCADE
);

-- =========================================================
-- CREATE BANK ACCOUNT TABLE
-- =========================================================

CREATE TABLE bank_account (
    account_id SERIAL PRIMARY KEY,
    account_no BIGINT UNIQUE NOT NULL,
    account_type VARCHAR(50) NOT NULL,
    balance DECIMAL(12,2) DEFAULT 0,
    customer_id INT NOT NULL,

    CONSTRAINT fk_account_customer
    FOREIGN KEY(customer_id)
    REFERENCES customer(customer_id)
    ON DELETE CASCADE
);

-- =========================================================
-- CREATE LOAN TABLE
-- =========================================================

CREATE TABLE loan (
    loan_id SERIAL PRIMARY KEY,
    loan_type VARCHAR(50) NOT NULL,
    amount DECIMAL(12,2) NOT NULL,
    loan_status VARCHAR(50),
    customer_id INT NOT NULL,

    CONSTRAINT fk_loan_customer
    FOREIGN KEY(customer_id)
    REFERENCES customer(customer_id)
    ON DELETE CASCADE
);

-- =========================================================
-- CREATE TRANSACTION TABLE
-- =========================================================

CREATE TABLE transaction_details (
    transaction_id SERIAL PRIMARY KEY,
    amount DECIMAL(12,2) NOT NULL,
    transaction_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    account_no BIGINT NOT NULL,

    CONSTRAINT fk_transaction_account
    FOREIGN KEY(account_no)
    REFERENCES bank_account(account_no)
    ON DELETE CASCADE
);

-- =========================================================
-- INSERT SBI BANK DATA
-- =========================================================

INSERT INTO bank(bank_name, bank_address)
VALUES
('SBI', 'Hyderabad');

-- =========================================================
-- INSERT 3 BRANCHES
-- =========================================================

INSERT INTO branch(branch_name, address, ifsc_code, bank_id)
VALUES
('Ameerpet Branch', 'Hyderabad', 'SBIHYD0001', 1),
('Madhapur Branch', 'Hyderabad', 'SBIHYD0002', 1),
('Kukatpally Branch', 'Hyderabad', 'SBIHYD0003', 1);

-- =========================================================
-- INSERT 30 EMPLOYEES
-- =========================================================

INSERT INTO employees
(employee_name, employee_gender,
employee_mobile, employee_age,
employee_address, branch_id)
VALUES

('Ravi', 'Male', '9000000001', 28, 'Hyderabad', 1),
('Suresh', 'Male', '9000000002', 30, 'Hyderabad', 1),
('Priya', 'Female', '9000000003', 25, 'Hyderabad', 1),
('Kiran', 'Male', '9000000004', 27, 'Hyderabad', 1),
('Anitha', 'Female', '9000000005', 29, 'Hyderabad', 1),

('Rahul', 'Male', '9000000006', 31, 'Hyderabad', 2),
('Sneha', 'Female', '9000000007', 24, 'Hyderabad', 2),
('Arjun', 'Male', '9000000008', 26, 'Hyderabad', 2),
('Divya', 'Female', '9000000009', 28, 'Hyderabad', 2),
('Vijay', 'Male', '9000000010', 32, 'Hyderabad', 2),

('Teja', 'Male', '9000000011', 27, 'Hyderabad', 3),
('Lavanya', 'Female', '9000000012', 26, 'Hyderabad', 3),
('Mahesh', 'Male', '9000000013', 29, 'Hyderabad', 3),
('Pooja', 'Female', '9000000014', 25, 'Hyderabad', 3),
('Ramesh', 'Male', '9000000015', 30, 'Hyderabad', 3),

('Ajay', 'Male', '9000000016', 28, 'Hyderabad', 1),
('Niharika', 'Female', '9000000017', 23, 'Hyderabad', 1),
('Karthik', 'Male', '9000000018', 26, 'Hyderabad', 1),
('Swathi', 'Female', '9000000019', 27, 'Hyderabad', 1),
('Varun', 'Male', '9000000020', 29, 'Hyderabad', 1),

('Sanjay', 'Male', '9000000021', 31, 'Hyderabad', 2),
('Meghana', 'Female', '9000000022', 24, 'Hyderabad', 2),
('Harsha', 'Male', '9000000023', 28, 'Hyderabad', 2),
('Keerthi', 'Female', '9000000024', 25, 'Hyderabad', 2),
('Naresh', 'Male', '9000000025', 30, 'Hyderabad', 2),

('Bhanu', 'Male', '9000000026', 27, 'Hyderabad', 3),
('Sirisha', 'Female', '9000000027', 26, 'Hyderabad', 3),
('Lokesh', 'Male', '9000000028', 29, 'Hyderabad', 3),
('Deepika', 'Female', '9000000029', 24, 'Hyderabad', 3),
('Tarun', 'Male', '9000000030', 32, 'Hyderabad', 3);

-- =========================================================
-- INSERT 10 CUSTOMERS
-- =========================================================

INSERT INTO customer
(customer_name, customer_gender,
customer_mobile, customer_age,
customer_address, branch_id)
VALUES

('Venky', 'Male', '9100000001', 22, 'Hyderabad', 1),
('Anil', 'Male', '9100000002', 25, 'Hyderabad', 1),
('Sneha', 'Female', '9100000003', 24, 'Hyderabad', 1),
('Rohit', 'Male', '9100000004', 26, 'Hyderabad', 2),
('Kavya', 'Female', '9100000005', 23, 'Hyderabad', 2),

('Vamsi', 'Male', '9100000006', 27, 'Hyderabad', 2),
('Neha', 'Female', '9100000007', 22, 'Hyderabad', 3),
('Sai', 'Male', '9100000008', 28, 'Hyderabad', 3),
('Akhil', 'Male', '9100000009', 24, 'Hyderabad', 3),
('Reshma', 'Female', '9100000010', 25, 'Hyderabad', 3);

-- =========================================================
-- INSERT BANK ACCOUNTS
-- =========================================================

INSERT INTO bank_account
(account_no, account_type,
balance, customer_id)
VALUES

(100001, 'Savings', 5000, 1),
(100002, 'Current', 12000, 2),
(100003, 'Savings', 8000, 3),
(100004, 'Savings', 15000, 4),
(100005, 'Current', 20000, 5),

(100006, 'Savings', 7000, 6),
(100007, 'Current', 11000, 7),
(100008, 'Savings', 9000, 8),
(100009, 'Savings', 6000, 9),
(100010, 'Current', 17000, 10);

-- =========================================================
-- INSERT 5 LOANS
-- =========================================================

INSERT INTO loan
(loan_type, amount,
loan_status, customer_id)
VALUES

('Home Loan', 500000, 'Approved', 1),
('Car Loan', 300000, 'Pending', 2),
('Education Loan', 200000, 'Approved', 3),
('Personal Loan', 100000, 'Approved', 4),
('Business Loan', 700000, 'Pending', 5);

-- =========================================================
-- INSERT 10 TRANSACTIONS
-- =========================================================

INSERT INTO transaction_details
(amount, account_no)
VALUES

(1000, 100001),
(2000, 100002),
(1500, 100003),
(2500, 100004),
(3000, 100005),
(1200, 100006),
(1800, 100007),
(2200, 100008),
(2700, 100009),
(3500, 100010);

-- =========================================================
-- DISPLAY TABLE DATA
-- =========================================================

SELECT * FROM bank;
SELECT * FROM branch;
SELECT * FROM employees;
SELECT * FROM customer;
SELECT * FROM bank_account;
SELECT * FROM loan;
SELECT * FROM transaction_details;

-- =========================================================
-- SHOW ALL TABLES
-- =========================================================

\dt

-- =========================================================
-- DESCRIBE TABLES
-- =========================================================

\d bank
\d branch
\d employees
\d customer
\d bank_account
\d loan
\d transaction_details