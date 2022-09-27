SELECT s_name, s_acctbal
FROM supplier
INNER JOIN region ON region.r_regionkey = nation.n_regionkey
INNER JOIN nation ON nation.n_nationkey = supplier.s_nationkey
WHERE s_acctbal > 5000
AND region.r_name = 'AMERICA';