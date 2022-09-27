SELECT COUNT(l_orderkey)
FROM (SELECT *
    FROM customer, orders, nation
    WHERE n_name = 'UNITED STATES'
    AND c_custkey = o_custkey
    AND c_nationkey = n_nationkey),
    (SELECT *
    FROM lineitem, supplier, nation, region
    WHERE r_name = 'AFRICA'
    AND l_suppkey = s_suppkey
    AND s_nationkey = n_nationkey
    AND r_regionkey = n_regionkey)
WHERE o_orderkey = l_orderkey;
    
