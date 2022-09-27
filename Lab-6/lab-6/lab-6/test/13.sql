SELECT n_name
FROM (SELECT n_name, MAX(totalSold)
    FROM( SELECT n_name, SUM(l_extendedprice) AS totalSold
        FROM nation, lineitem, supplier
        WHERE n_nationkey = s_nationkey
        AND l_suppkey = s_suppkey
        AND l_shipdate LIKE '1994-%'
        GROUP BY n_name))
