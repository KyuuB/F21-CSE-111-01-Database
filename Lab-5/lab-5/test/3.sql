SELECT MIN(l_discount) AS min_discount
FROM (SELECT AVG(l_discount) AS avg_discount
FROM lineitem, orders
WHERE l_orderkey = o_orderkey), lineitem, orders
WHERE l_orderkey = o_orderkey
    AND o_orderdate LIKE '1995-10-%'
    AND avg_discount < l_discount;
