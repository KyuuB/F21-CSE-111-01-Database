SELECT p_mfgr
FROM (SELECT p_mfgr, MIN(ps_availqty) FROM supplier, partsupp, part
WHERE s_suppkey = ps_suppkey
AND ps_partkey = p_partkey
AND s_name = 'Supplier#000000010');