-- Need nation key
-- Dates between
-- alphabetical order
--c_custkey, c_nationkey
--o_custkey, o_orderdate
--n_nationkey, n_name

SELECT n_name
FROM nation
INNER JOIN customer ON customer.c_nationkey = nation.n_nationkey
INNER JOIN orders ON orders.o_custkey = customer.c_custkey
WHERE o_orderdate BETWEEN '1996-09-10'AND '1996-09-12'
GROUP BY n_name
ORDER BY n_name ASC;
