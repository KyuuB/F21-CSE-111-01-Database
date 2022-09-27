SELECT region.r_name, s_name, MAX(s_acctbal)
FROM supplier
INNER JOIN region ON region.r_regionkey = nation.n_regionkey
INNER JOIN nation ON nation.n_nationkey = supplier.s_nationkey
GROUP BY r_name;