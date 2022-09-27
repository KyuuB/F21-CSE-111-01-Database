--Cust key in order doesn't exist in order,
-- and cust acctbal is less than avg acctbal
SELECT r_name, COUNT(DISTINCT c_name)
FROM region, nation, customer, orders
WHERE c_nationkey = n_nationkey
AND n_regionkey = r_regionkey
AND c_acctbal < (SELECT AVG(c_acctbal)
    FROM customer)
AND NOT c_custkey IN (SELECT o_custkey
    FROM orders)
GROUP BY r_name;