SELECT SUBSTR(o_orderdate, 1, 4) AS Year, COUNT(o_orderpriority) AS OrderStatus_Medium
FROM orders
INNER JOIN lineitem ON lineitem.l_orderkey = orders.o_orderkey
INNER JOIN supplier ON supplier.s_suppkey = lineitem.l_suppkey
INNER JOIN nation ON nation.n_nationkey = supplier.s_nationkey
WHERE nation.n_name = 'CANADA'
AND o_orderpriority = '3-MEDIUM'
GROUP BY SUBSTR(o_orderdate, 1, 4);