SELECT cust_nation, ct_customer, ct_supplier
FROM (SELECT COUNT(c_name) AS ct_customer, n_name AS cust_nation, r_name
    FROM customer, nation, region
    WHERE c_nationkey = n_nationkey
    AND n_regionkey = r_regionkey
    AND r_name = 'AFRICA'
    GROUP BY n_name), --Count the number of customers from Africa and set AS ct_customer
        (SELECT COUNT(s_name) AS ct_supplier, n_name AS sup_nation, r_name
        FROM supplier, nation, region
        WHERE s_nationkey = n_nationkey
        AND n_regionkey = r_regionkey
        AND r_name = 'AFRICA'
        GROUP BY n_name) --Count the number of suppliers from Africa and set AS ct_supplier
WHERE cust_nation = sup_nation --Link the selections from their respective nations
GROUP BY cust_nation;