SELECT nation.n_name, COUNT(DISTINCT o_orderkey)
FROM orders
INNER JOIN lineitem ON lineitem.l_orderkey = orders.o_orderkey
INNER JOIN supplier ON supplier.s_suppkey = lineitem.l_suppkey
INNER JOIN nation ON nation.n_nationkey = supplier.s_nationkey
WHERE o_orderstatus = 'F'
AND o_orderdate BETWEEN '1995-01-01' AND '1995-12-31'
GROUP BY n_name
HAVING COUNT(DISTINCT o_orderkey) > 50