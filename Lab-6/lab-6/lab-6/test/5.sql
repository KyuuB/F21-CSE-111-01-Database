
SELECT COUNT( s_suppkey )
FROM supplier, part, partsupp
WHERE s_suppkey = ps_suppkey 
AND ps_partkey = p_partkey
AND p_retailprice = (SELECT MAX(p_retailprice)
    FROM part) 

