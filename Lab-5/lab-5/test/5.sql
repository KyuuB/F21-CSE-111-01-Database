--Group by part size, minimum(ps_supplycost), Contain STEEL in name, from region ASIA
SELECT s_name, p_size, MIN(ps_supplycost)
FROM supplier, part, partsupp, nation, region
WHERE s_suppkey = ps_suppkey
AND ps_partkey = p_partkey
AND s_nationkey = n_nationkey
AND n_regionkey = r_regionkey
AND r_name = 'ASIA'
AND SUBSTR(p_type, LENGTH(p_type) - 4, LENGTH(p_type)) = 'STEEL'
AND p_type LIKE '%STEEL%'
GROUP BY p_size 
ORDER BY s_name;
-- I got all the suppliers and the suppliers
-- names in order, but I couldn't group them 
-- up in a way that would match the results.
-- How would I group them up, for future labs?