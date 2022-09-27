PRAGMA foreign_keys = on;

SELECT "1----------";
.headers on
--put your code here
    DROP TABLE IF EXISTS Classes;
    DROP TABLE IF EXISTS Ships;
    DROP TABLE IF EXISTS Battles;
    DROP TABLE IF EXISTS Outcomes;
    
    CREATE TABLE IF NOT EXISTS Classes (
        class           varchar(20)     PRIMARY KEY,
        type            varchar(3)
        CHECK (type IN ('bb','bc')),      
        country         varchar(15)     NOT NULL,
        numGuns         INTEGER,
        bore            INTEGER,
        displacement    INTEGER
    );
    CREATE TABLE IF NOT EXISTS Ships(
        name        varchar(20)         PRIMARY KEY,
        class       varchar(20)         REFERENCES Classes(class)
        ON UPDATE SET NULL,
        launched    DATE
    );
    CREATE TABLE IF NOT EXISTS Battles(
        name    varchar(20)             PRIMARY KEY,
        data    DATE 
    );
    CREATE TABLE IF NOT EXISTS Outcomes(
        ship        varchar(20)         REFERENCES Ships(name) 
        ON DELETE CASCADE ON UPDATE CASCADE,
        battle      varchar(20)         REFERENCES Battles(name) 
        ON DELETE CASCADE ON UPDATE CASCADE,
        result      varchar(15) CHECK (result IN ('ok', 'sunk', 'damaged'))
    );
;
.headers off

SELECT "2----------";
.headers on
--put your code here
INSERT INTO Classes (class, type, country, numGuns, bore, displacement)
VALUES 
    ('Bismarck', 'bb', 'Germany', 8, 15, 42000),
    ('Iowa', 'bb', 'USA', 9, 16, 46000),
    ('Kongo', 'bc', 'Japan', 8, 14, 32000),
    ('North Carolina', 'bb', 'USA', 9, 16, 37000),
    ('Renown', 'bc', 'Britain', 6, 15, 32000),
    ('Revenge', 'bb', 'Britain', 8, 15, 29000),
    ('Tennessee', 'bb', 'USA', 12, 14, 32000),
    ('Yamato', 'bb', 'Japan', 9, 18, 65000)
;
INSERT INTO Ships 
VALUES 
    ('California', 'Tennessee', 1915),
    ('Haruna', 'Kongo', 1915),
    ('Hiei', 'Kongo', 1915),
    ('Iowa', 'Iowa', 1933),
    ('Kirishima', 'Kongo', 1915),
    ('Kongo', 'Kongo', 1913),
    ('Missouri', 'Iowa', 1935),
    ('Musashi', 'Yamato', 1942),
    ('New Jersey', 'Iowa', 1936),
    ('North Carolina', 'North Carolina', 1941),
    ('Ramillies', 'Revenge', 1917),
    ('Renown', 'Renown', 1916),
    ('Repulse', 'Renown', 1916),
    ('Resolution', 'Revenge', 1916),
    ('Revenge', 'Revenge', 1916),
    ('Royal Oak', 'Revenge', 1916),
    ('Royal Sovereign', 'Revenge', 1916),
    ('Tennessee', 'Tennessee', 1915),
    ('Washington', 'North Carolina', 1941),
    ('Wisconsin', 'Iowa', 1940),
    ('Yamato', 'Yamato', 1941);

INSERT INTO Battles
VALUES 
    ('Denmark Strait', 1941-05-24),
    ('Guadalcanal', 1942-11-15),
    ('North Cape', 1943-12-26),
    ('Surigao Strait', 1944-10-25);

INSERT INTO Outcomes 
VALUES 
    ('California', 'Surigao Strait', 'ok'),
    ('Kirishima', 'Guadalcanal', 'sunk'),
    ('Resolution', 'Denmark Strait', 'ok'),
    ('Wisconsin', 'Guadalcanal', 'damaged'),
    ('Tennessee', 'Surigao Strait', 'ok'),
    ('Washington', 'Guadalcanal', 'ok'),
    ('New Jersey', 'Surigao Strait', 'ok'),
    ('Yamato', 'Surigao Strait', 'sunk'),
    ('Wisconsin', 'Surigao Strait', 'damaged');
;



select * from Classes;
select * from Ships;
select * from Battles;
select * from Outcomes;
.headers off

SELECT "3----------";
.headers on
--put your code here
DELETE FROM Classes
WHERE displacement < 30000
AND numGuns < 8;
;

select * from Classes;
select * from Ships;
.headers off

SELECT "4----------";
.headers on
--put your code here
DELETE FROM Battles
WHERE name = 'Guadalcanal';
;

select * from Battles;
select * from Outcomes;
.headers off

SELECT "5----------";
.headers on
--put your code here
UPDATE Battles
SET name = 'Strait of Surigao'
WHERE name = 'Surigao Strait';
;

select * from Battles;
select * from Outcomes;
.headers off

SELECT "6----------";
.headers on
--put your code here
DELETE FROM Ships
WHERE class IS NULL OR trim(class) = '';
;

select * from Ships;
select * from Outcomes;
.headers off
