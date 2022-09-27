SELECT COUNT(DISTINCT o_custkey)
FROM orders
INNER JOIN customer ON customer.c_custkey = orders.o_custkey
INNER JOIN lineitem ON lineitem.l_orderkey = orders.o_orderkey
WHERE l_discount >= 0.1;