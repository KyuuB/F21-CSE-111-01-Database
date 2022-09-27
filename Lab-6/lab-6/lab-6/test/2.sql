SELECT COUNT(*) as 'Number of Customers'
FROM (SELECT COUNT(c_name)
    FROM orders, customer 
    WHERE c_custkey = o_custkey
    AND o_orderdate LIKE '1995-11-%'
    GROUP BY c_name
    HAVING count(o_orderkey) >= 3)
