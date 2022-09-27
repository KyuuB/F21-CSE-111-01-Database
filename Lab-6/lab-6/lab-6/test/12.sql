SELECT n_name
FROM (SELECT n_name, MIN(minSpend)
    FROM (SELECT n_name, SUM(o_totalprice) AS minSpend
        FROM nation, customer, orders
        WHERE n_nationkey = c_nationkey
        AND o_custkey = c_custkey
        GROUP BY n_name))