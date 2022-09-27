SELECT COUNT(DISTINCT s_suppkey)
FROM supplier, partsupp, part
WHERE s_suppkey = ps_suppkey
AND ps_partkey = p_partkey
AND p_type LIKE '%POLISHED%'
AND p_size IN (3, 23, 36, 49);