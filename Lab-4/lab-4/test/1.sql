SELECT customer.c_name, SUM(o_totalprice)
FROM orders
INNER JOIN customer ON customer.c_custkey = orders.o_custkey
INNER JOIN nation ON nation.n_nationkey = customer.c_nationkey
WHERE o_orderdate BETWEEN '1995-01-01' AND '1995-12-31'
AND nation.n_name = 'FRANCE'
GROUP BY customer.c_name;