CREATE DATABASE kompyuterlar;

USE kompyuterlar;

CREATE TABLE komp (brand TEXT,model TEXT,cpu TEXT,frequency FLOAT,ram TINYINT,os TEXT,price INT);

INSERT INTO komp VALUES
    ('Apple', 'MacBook Pro', 'Intel Core i7', 2.5, 16, 'macOS', 2500),
    ('Apple', 'MacBook Air', 'M1', 3.2, 8, 'macOS', 1300),
    ('ASUS', 'ZenBook', 'Intel Core i7', 2.8, 16, 'Windows 10', 1500),
    ('ASUS', 'VivoBook', 'Intel Core i5', 2.4, 8, 'Windows 10', 1000),
    ('HP', 'Pavilion 15', 'AMD Ryzen 5', 3.0, 8, 'Windows 11', 900),
    ('HP', 'ENVY x360', 'AMD Ryzen 7', 3.1, 16, 'Windows 11', 1800),
    ('Dell', 'XPS 13', 'Intel Core i7', 3.9, 16, 'Windows 10', 2400),
    ('Dell', 'Inspiron 15', 'Intel Core i5', 2.6, 8, 'Windows 10', 1100),
    ('Lenovo', 'ThinkPad X1', 'Intel Core i7', 3.1, 16, 'Windows 10', 2200),
    ('Lenovo', 'IdeaPad 3', 'Intel Core i3', 1.8, 4, 'Windows 10', 500),
    ('Acer', 'Aspire 5', 'AMD Ryzen 3', 2.1, 8, 'Windows 11', 700),
    ('Acer', 'Swift 3', 'Intel Core i5', 3.0, 8, 'Windows 11', 950),
    ('MSI', 'GF63', 'Intel Core i5', 2.4, 8, 'Windows 10', 1200),
    ('MSI', 'Stealth 15', 'Intel Core i7', 3.5, 16, 'Windows 10', 2000),
    ('Apple', 'MacBook Pro 13', 'M2', 3.5, 16, 'macOS', 2800),
    ('ASUS', 'ROG Strix', 'AMD Ryzen 9', 3.9, 16, 'Windows 11', 2700),
    ('HP', 'Spectre x360', 'Intel Core i7', 3.0, 16, 'Windows 11', 2600),
    ('Dell', 'G5 15', 'Intel Core i5', 2.5, 8, 'Windows 10', 1400),
    ('Lenovo', 'Legion 5', 'AMD Ryzen 7', 3.6, 16, 'Windows 11', 1900),
    ('Acer', 'Nitro 5', 'AMD Ryzen 5', 3.4, 8, 'Windows 10', 1700);


SELECT * FROM komp ORDER BY price DESC LIMIT 1;

SELECT * FROM komp ORDER BY price LIMIT 1;

SELECT frequency FROM komp WHERE price BETWEEN 400 AND 1000 AND cpu LIKE '%Intel%';

SELECT COUNT(*) FROM komp WHERE brand ='Apple';

SELECT * FROM komp WHERE os LIKE '%Windows%' AND brand ='ASUS' AND ram <>8 ORDER BY price ASC;
