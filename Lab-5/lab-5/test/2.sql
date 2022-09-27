SELECT r_name, COUNT(s_name)
FROM (SELECT r_name AS s_region, AVG(s_acctbal) AS reg_acctbal
    FROM supplier, nation, region
    WHERE s_nationkey = n_nationkey
    AND n_regionkey = r_regionkey
    GROUP BY r_regionkey), region, nation, supplier
WHERE r_name = s_region
    AND s_nationkey = n_nationkey
    AND n_regionkey = r_regionkey
    AND s_acctbal < reg_acctbal
    GROUP BY r_regionkey;