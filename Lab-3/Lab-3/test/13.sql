SELECT SUM(c_acctbal)
FROM customer
INNER JOIN nation ON nation.n_nationkey = customer.c_nationkey
INNER JOIN region ON region.r_regionkey = nation.n_regionkey
WHERE c_mktsegment = 'MACHINERY'
AND region.r_name = 'EUROPE';