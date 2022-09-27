SELECT nation.n_name, MAX(s_acctbal)
FROM supplier
INNER JOIN nation ON nation.n_nationkey = supplier.s_nationkey
GROUP BY nation.n_name
HAVING s_acctbal > 9000;