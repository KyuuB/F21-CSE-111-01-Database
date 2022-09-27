--less than 50 distinct (o_orderkey)
--FROM germany and france 
SELECT COUNT(DISTINCT l_suppkey)
FROM (SELECT l_suppkey, COUNT( DISTINCT o_orderkey) AS numOrders
    FROM supplier, customer, orders, lineitem, nation
    WHERE (n_name = 'GERMANY' 
    OR n_name = 'FRANCE')
    AND o_custkey = c_custkey
    AND l_suppkey = s_suppkey
    AND l_orderkey = o_orderkey
    AND n_nationkey = c_nationkey
    GROUP BY l_suppkey) AS GermFranCustomers
    WHERE GermFranCustomers.numOrders < 50

