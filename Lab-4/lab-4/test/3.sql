SELECT nation.n_name, COUNT(o_orderkey)
FROM orders
INNER JOIN customer ON customer.c_custkey = orders.o_custkey
INNER JOIN nation ON nation.n_nationkey = customer.c_nationkey
INNER JOIN region ON region.r_regionkey = nation.n_regionkey
GROUP BY n_nationkey
HAVING region.r_name = 'AMERICA';
