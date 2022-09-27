SELECT c_name, COUNT(orders.o_orderkey)
FROM customer
INNER JOIN orders ON orders.o_custkey = customer.c_custkey
INNER JOIN nation ON nation.n_nationkey = customer.c_nationkey
WHERE nation.n_name = 'GERMANY'
AND orders.o_orderdate BETWEEN '1993-01-01' AND '1993-12-31'
GROUP BY c_name;