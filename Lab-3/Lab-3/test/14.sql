SELECT COUNT(o_orderpriority)
FROM orders
INNER JOIN customer ON customer.c_custkey = orders.o_custkey
INNER JOIN nation ON nation.n_nationkey = customer.c_nationkey
WHERE nation.n_name = 'BRAZIL'
AND o_orderpriority = '1-URGENT'
AND o_orderdate BETWEEN '1994-01-01' AND '1997-12-31';