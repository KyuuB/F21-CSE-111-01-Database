SELECT part.p_type, MIN(l_discount), MAX(l_discount)
FROM lineitem
INNER JOIN part ON part.p_partkey = lineitem.l_partkey
GROUP BY p_type
HAVING SUBSTR(p_type, 1, 7) = 'ECONOMY'
AND SUBSTR(p_type, LENGTH(p_type) - 5, LENGTH(p_type)) = 'COPPER';