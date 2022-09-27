--customers order with one order supplied exlusively by America
SELECT COUNT(DISTINCT c_name) 
FROM orders, customer 
WHERE o_custkey = c_custkey --Get all customers
AND o_orderkey NOT IN (SELECT DISTINCT( o_orderkey ) AS distinctSupplier
    --Negate all the suppliers
    FROM supplier, nation, lineitem, orders, region
    WHERE s_nationkey = n_nationkey
    AND n_regionkey = r_regionkey
    --Negate again meaning get only supplier exlusive to AMERICA
    AND r_name NOT IN ('AMERICA')
    AND o_orderkey = l_orderkey
    AND s_suppkey = l_suppkey)

