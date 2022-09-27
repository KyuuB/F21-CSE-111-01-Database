--Distinct parts by customers in America That are supplier by exactly 3 suppliers from ASIA

SELECT DISTINCT(p_name)
FROM customer, orders, lineitem, part, nation, region
WHERE c_nationkey = n_nationkey
AND n_regionkey = r_regionkey
AND c_custkey = o_custkey
AND p_partkey = l_partkey
AND o_orderkey = l_orderkey
AND r_name = 'AMERICA'
AND p_partkey IN (SELECT p_partkey
    FROM supplier, region, nation, part, partsupp
    WHERE s_nationkey = n_nationkey
    AND n_regionkey = r_regionkey
    AND s_suppkey = ps_suppkey
    AND ps_partkey = p_partkey  
    AND r_name = 'ASIA'
    GROUP BY r_name
    HAVING COUNT( s_suppkey) = 3)