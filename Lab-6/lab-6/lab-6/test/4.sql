SELECT COUNT(*)
FROM (SELECT COUNT(p_partkey)
    FROM part, partsupp, nation, supplier
    WHERE s_suppkey = ps_suppkey 
    AND ps_partkey = p_partkey
    AND s_nationkey = n_nationkey
    AND n_name = 'UNITED STATES'
    GROUP BY s_name
    HAVING COUNT(p_partkey) > 40)