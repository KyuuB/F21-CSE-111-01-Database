SELECT supplier.s_name, o_orderpriority, COUNT(DISTINCT lineitem.l_partkey)
FROM orders
INNER JOIN lineitem ON lineitem.l_orderkey = orders.o_orderkey
INNER JOIN supplier ON supplier.s_suppkey = lineitem.l_suppkey
INNER JOIN nation ON nation.n_nationkey = supplier.s_nationkey
INNER JOIN partsupp ON partsupp.ps_suppkey = lineitem.l_suppkey
INNER JOIN part ON part.p_partkey = partsupp.ps_partkey
WHERE nation.n_name = 'CANADA'
GROUP BY s_name, o_orderpriority;

