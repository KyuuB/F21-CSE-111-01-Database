SELECT r_name
FROM (SELECT r_name, MIN(amountSpent)
    FROM (SELECT r_name, SUM(l_extendedprice) AS amountSpent
        FROM nation, customer, region, supplier, lineitem
        WHERE n_nationkey = c_nationkey
        AND r_regionkey = n_regionkey
        AND l_suppkey = s_suppkey
        AND s_nationkey = n_nationkey
        GROUP BY r_name))

