-- 13-change_class.sql, Lindsey Thomas C19
-- Script that removes all records with a score <= 5 in the table second_table of the database hbtn_0c_0 in your MySQL server
DELETE FROM second_table
WHERE score <= 5;
