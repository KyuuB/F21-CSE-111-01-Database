--p_retailprice < 1000, shipped LIKE 1997,
SELECT SUM(DISTINCT ps_supplycost)
FROM partsupp, part, lineitem
WHERE ps_partkey = p_partkey
AND ps_suppkey = l_suppkey
AND l_partkey = p_partkey
AND p_retailprice < 1000
AND l_shipdate LIKE '1997-%'
AND l_suppkey NOT IN(SELECT DISTINCT l_suppkey
    FROM partsupp, lineitem, part
    WHERE l_suppkey = ps_suppkey
    AND ps_partkey = p_partkey
    AND l_partkey = p_partkey
    AND l_extendedprice < 2000
    AND l_shipdate LIKE '1996-%');

