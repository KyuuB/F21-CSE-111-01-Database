SELECT nation.n_name, o_orderstatus, COUNT(o_orderkey)
FROM orders
INNER JOIN customer ON customer.c_custkey = orders.o_custkey
INNER JOIN nation ON nation.n_nationkey = customer.c_nationkey
INNER JOIN region ON region.r_regionkey = nation.n_regionkey
WHERE region.r_name = 'AMERICA'
GROUP BY nation.n_name, o_orderstatus;