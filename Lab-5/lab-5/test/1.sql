SELECT COUNT(c_name)
FROM customer
INNER JOIN nation ON nation.n_nationkey = customer.c_nationkey
INNER JOIN region ON region.r_regionkey = nation.n_regionkey
WHERE region.r_name NOT IN ('AFRICA', 'EUROPE','ASIA');

