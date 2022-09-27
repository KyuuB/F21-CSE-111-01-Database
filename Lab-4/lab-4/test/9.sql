SELECT COUNT(DISTINCT orders.o_clerk)
FROM lineitem
INNER JOIN orders ON orders.o_orderkey = lineitem.l_orderkey
INNER JOIN supplier ON supplier.s_suppkey = lineitem.l_suppkey
INNER JOIN nation ON nation.n_nationkey = supplier.s_nationkey
WHERE nation.n_name = 'UNITED STATES';