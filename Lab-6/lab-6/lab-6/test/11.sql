SELECT n_name
FROM customer, nation
WHERE n_nationkey = c_nationkey
GROUP BY n_name
HAVING COUNT(*) = (SELECT MIN(numCustomers)
    FROM (SELECT COUNT(c_custkey) AS numCustomers
        FROM nation, customer
        WHERE n_nationkey = c_nationkey
        GROUP BY n_name))
