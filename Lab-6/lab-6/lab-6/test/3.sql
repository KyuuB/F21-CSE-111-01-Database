SELECT COUNT(*)
FROM (SELECT COUNT(p_partkey) 
    FROM nation, part, partsupp, supplier
    WHERE s_suppkey = ps_suppkey
    AND ps_partkey = p_partkey
    AND s_nationkey = n_nationkey
    AND n_name = 'UNITED STATES'
    GROUP BY p_partkey
    HAVING COUNT(s_name) = 2)