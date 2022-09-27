SELECT p_name, ps_supplycost * ps_availqty AS totValue
FROM part, supplier, partsupp, nation
WHERE s_suppkey = ps_suppkey
AND ps_partkey = p_partkey
AND s_nationkey = n_nationkey
AND n_name = 'UNITED STATES'
AND ps_supplycost * ps_availqty IN (SELECT ps_supplycost * ps_availqty AS tot_value
    FROM partsupp
    ORDER BY (tot_value) DESC
    LIMIT (SELECT COUNT(ps_partkey) * 0.01 
        FROM partsupp
        ORDER BY (ps_supplycost * ps_availqty) ASC));

--Same thing as Query 5, where I got the answer but couldn't 
--group them up to match the output. 
-- Is there a solution to how should group/order them for 
-- future reference?

