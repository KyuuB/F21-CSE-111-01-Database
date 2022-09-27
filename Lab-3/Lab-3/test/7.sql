SELECT strftime("%Y-%m", l_receiptdate) as 'year-month', count(l_receiptdate)
FROM lineitem
INNER JOIN orders ON orders.o_orderkey = lineitem.l_orderkey
INNER JOIN customer ON customer.c_custkey = orders.o_custkey
WHERE l_receiptdate BETWEEN '1993-01-01' AND '1993-12-31'
AND customer.c_name = 'Customer#000000010'
GROUP BY strftime("%Y-%m", l_receiptdate);