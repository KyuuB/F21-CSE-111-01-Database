--commit < receipt, 
SELECT o_orderpriority, COUNT(p_name)
FROM part, lineitem, orders
WHERE o_orderkey = l_orderkey
AND p_partkey = l_partkey 
AND o_orderdate LIKE '1997-%'
AND l_receiptdate > l_commitdate
GROUP BY o_orderpriority;