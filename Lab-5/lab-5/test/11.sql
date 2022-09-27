SELECT p_name
FROM (SELECT MIN(l_extendedprice * (1 - l_discount)) AS lowV_part
    FROM lineitem, part
    WHERE p_partkey = l_partkey
    AND l_shipdate > '1996-10-2'), part