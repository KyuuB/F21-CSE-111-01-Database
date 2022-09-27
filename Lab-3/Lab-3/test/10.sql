SELECT SUM(o_totalprice)
FROM orders
INNER JOIN region ON region.r_regionkey = nation.n_regionkey
INNER JOIN nation ON nation.n_nationkey = customer.c_nationkey
INNER JOIN customer ON customer.c_custkey = orders.o_custkey
WHERE o_orderdate BETWEEN '1996-01-01' AND '1996-12-31'
AND region.r_name = 'AMERICA';