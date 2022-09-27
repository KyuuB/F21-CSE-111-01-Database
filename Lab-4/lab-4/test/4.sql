SELECT s_name, count(part.p_size)
FROM supplier
INNER JOIN partsupp ON partsupp.ps_suppkey = supplier.s_suppkey
INNER JOIN part ON part.p_partkey = partsupp.ps_partkey
INNER JOIN nation ON nation.n_nationkey = supplier.s_nationkey
WHERE nation.n_name = 'CANADA'
AND part.p_size < 20
GROUP BY s_name;