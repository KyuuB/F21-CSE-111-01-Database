--supplier customer pair where o_totalprice is minimum.
-- o_orderstatus = F
SELECT s_name, c_name, MIN(o_totalprice)
FROM supplier, customer, orders, lineitem
WHERE s_suppkey = l_suppkey
AND c_custkey = o_custkey
AND l_orderkey = o_orderkey
AND o_orderstatus = 'F'
