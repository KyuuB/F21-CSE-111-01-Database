--COUNT o_orderkey, between 1997 october to december, recieved < commit. Group by priority
SELECT o_orderpriority, COUNT(DISTINCT o_orderkey)
FROM orders, customer, lineitem
WHERE o_custkey = c_custkey
AND l_orderkey = o_orderkey
AND o_orderdate BETWEEN '1997-10-01' AND '1997-12-31'
AND l_commitdate > l_receiptdate
GROUP BY o_orderpriority;