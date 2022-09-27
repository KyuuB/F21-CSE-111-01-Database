--create separate nation and regions for supplier and customer, order by year 1, 4, 
--
SELECT sr.r_name, cr.r_name, SUBSTR(l_shipdate, 1, 4), SUM(l_extendedprice * (1 - l_discount))
FROM region sr, region cr, nation sn, nation cn, lineitem, orders, customer, supplier
WHERE s_suppkey = l_suppkey
AND o_custkey = c_custkey
AND l_orderkey = o_orderkey
AND cn.n_nationkey = c_nationkey
AND cn.n_regionkey = cr.r_regionkey
AND sn.n_nationkey = s_nationkey
AND sn.n_regionkey = sr.r_regionkey
AND l_shipdate BETWEEN '1996-01-01' AND '1997-12-31'
GROUP BY sr.r_name, cr.r_name, SUBSTR(l_shipdate, 1, 4)
ORDER BY sr.r_name, cr.r_name, SUBSTR(l_shipdate, 1, 4);
