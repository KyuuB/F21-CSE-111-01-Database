import sqlite3
from sqlite3 import Error


def openConnection(_dbFile):
    print("++++++++++++++++++++++++++++++++++")
    print("Open database: ", _dbFile)

    conn = None
    try:
        conn = sqlite3.connect(_dbFile)
        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

    return conn

def closeConnection(_conn, _dbFile):
    print("++++++++++++++++++++++++++++++++++")
    print("Close database: ", _dbFile)

    try:
        _conn.close()
        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def create_View1(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Create V1")
    try:
        cursor = _conn.cursor()
        cursor.execute("DROP view IF EXISTS V1;")
        v1 = """
                create view V1 AS
                SELECT c_custkey, c_name, c_address, c_phone,
                    c_acctbal, c_mktsegment, c_comment, 
                    nation.n_name AS c_nation, region.r_name AS c_region
                FROM customer, region, nation
                WHERE customer.c_nationkey = nation.n_nationkey
                AND nation.n_regionkey = region.r_regionkey;"""
        cursor.execute(v1)
    except Error as e:
        print(e)
    print("++++++++++++++++++++++++++++++++++")


def create_View2(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Create V2")
    try:
        cursor = _conn.cursor()
        cursor.execute("DROP view IF EXISTS V2;")
        v2 = """create view V2 AS
                SELECT s_suppkey, s_name, s_address, s_phone, 
                s_acctbal, s_comment, n_name AS s_nation, r_name AS s_region
                FROM supplier, region, nation
                WHERE s_nationkey = n_nationkey
                AND n_regionkey = r_regionkey;"""
        cursor.execute(v2)
    except Error as e:
        print(e)
    print("++++++++++++++++++++++++++++++++++")


def create_View5(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Create V5")
    try:
        cursor = _conn.cursor()
        cursor.execute("DROP view IF EXISTS V5;")
        v5 = """create view V5 AS
                select o_orderkey, o_custkey, o_orderstatus, o_totalprice, 
                strftime('%Y', o_orderdate) AS o_orderyear, o_orderpriority, o_clerk,
                o_shippriority, o_comment
                FROM orders;"""
        cursor.execute(v5)
    except Error as e:
        print(e)
    print("++++++++++++++++++++++++++++++++++")


def create_View10(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Create V10")
    try:
        cursor = _conn.cursor()
        cursor.execute("DROP view IF EXISTS V10;")
        v10 = """create view V10 AS
                select p_type, MIN(l_discount) AS min_discount, 
                    MAX(l_discount) AS max_discount
                FROM part, lineitem
                WHERE l_partkey = p_partkey
                GROUP BY p_type;
                """
        cursor.execute(v10)
    except Error as e:
        print(e)
    print("++++++++++++++++++++++++++++++++++")


def create_View151(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Create V151")
    try:
        cursor = _conn.cursor()
        cursor.execute("DROP view IF EXISTS V151;")
        v151 = """create view V151 AS
                select c_custkey, c_name, c_nationkey, c_acctbal
                FROM customer
                WHERE c_acctbal > 0;"""
        cursor.execute(v151)
    except Error as e:
        print(e)
    print("++++++++++++++++++++++++++++++++++")


def create_View152(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Create V152")
    try:
        cursor = _conn.cursor()
        cursor.execute("DROP view IF EXISTS V152;")
        v152 = """create view V152 AS
                select s_suppkey, s_name, s_nationkey, s_acctbal
                FROM supplier
                WHERE s_acctbal < 0;"""
        cursor.execute(v152)
    except Error as e:
        print(e)
    print("++++++++++++++++++++++++++++++++++")


def Q1(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q1")
    try:
        cursor = _conn.cursor()
        q1 = """
            select c_name, sum(o_totalprice)
            from orders, V1
            where o_custkey = c_custkey and
                c_nation = 'FRANCE'
                AND o_orderdate like '1995-__-__'
            group by c_name;
        """
        cursor.execute(q1)
        output = open('output/1.out', 'w')
        
        for row in cursor.fetchall():
            r = '{:<1}|{:<10}'.format(row[0],row[1])
            print(r, file = output)

    except Error as e:
        print(e)
    print("++++++++++++++++++++++++++++++++++")


def Q2(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q2")
    try:
        cursor = _conn.cursor()
        q2 = """
            select s_region, count(*)
            from V2
            group by s_region;
        """
        cursor.execute(q2)
        output = open('output/2.out', 'w')
        
        for row in cursor.fetchall():
            r = '{:<1}|{:<10}'.format(row[0],row[1])
            print(r, file = output)
    except Error as e:
        print(e)
    print("++++++++++++++++++++++++++++++++++")


def Q3(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q3")
    try:
        cursor = _conn.cursor()
        q3 = """
            select c_nation, count(*)
            from orders, V1
            where c_custkey = o_custkey
                and c_region='AMERICA'
            group by c_nation;
        """
        cursor.execute(q3)
        output = open('output/3.out', 'w')
        
        for row in cursor.fetchall():
            r = '{:<1}|{:<10}'.format(row[0],row[1])
            print(r, file = output)
    except Error as e:
        print(e)
    print("++++++++++++++++++++++++++++++++++")


def Q4(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q4")
    try:
        cursor = _conn.cursor()
        q4 = """
            select s_name, count(ps_partkey)
            from partsupp, V2, part
            where p_partkey = ps_partkey
                and ps_suppkey = s_suppkey
                and s_nation = 'CANADA'
                and p_size < 20
            group by s_name;
        """
        cursor.execute(q4)
        output = open('output/4.out', 'w')
        
        for row in cursor.fetchall():
            r = '{:<1}|{:<10}'.format(row[0],row[1])
            print(r, file = output)
    except Error as e:
        print(e)
    print("++++++++++++++++++++++++++++++++++")


def Q5(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q5")
    try:
        cursor = _conn.cursor()
        q5 = """
            select c_name, count(*)
            from V1, V5
            where o_custkey = c_custkey
                and c_nation = 'GERMANY'
                and o_orderyear like '1993'
            group by c_name;
        """
        cursor.execute(q5)
        output = open('output/5.out', 'w')
        
        for row in cursor.fetchall():
            r = '{:<1}|{:<10}'.format(row[0],row[1])
            print(r, file = output)
    except Error as e:
        print(e)
    print("++++++++++++++++++++++++++++++++++")


def Q6(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q6")
    try:
        cursor = _conn.cursor()
        q6 = """
            select s_name, o_orderpriority, count(distinct ps_partkey)
            from partsupp, lineitem, supplier, V5, nation
            where l_orderkey = o_orderkey
                and l_partkey = ps_partkey
                and l_suppkey = ps_suppkey
                and ps_suppkey = s_suppkey
                and s_nationkey = n_nationkey
                and n_name = 'CANADA'
            group by s_name, o_orderpriority;
        """
        cursor.execute(q6)
        output = open('output/6.out', 'w')
        
        for row in cursor.fetchall():
            r = '{:<1}|{:<10}|{:<20}'.format(row[0],row[1], row[2])
            print(r, file = output)
    except Error as e:
        print(e)
    print("++++++++++++++++++++++++++++++++++")


def Q7(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q7")
    try:
        cursor = _conn.cursor()
        q7 = """
            select c_nation, o_orderstatus, count(*)
            from V5, V1
            where o_custkey = c_custkey
                and c_region='AMERICA'
            group by c_nation, o_orderstatus;
        """
        cursor.execute(q7)
        output = open('output/7.out', 'w')
        
        for row in cursor.fetchall():
            r = '{:<1}|{:<10}|{:<20}'.format(row[0],row[1], row[2])
            print(r, file = output)
    except Error as e:
        print(e)
    print("++++++++++++++++++++++++++++++++++")


def Q8(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q8")
    try:
        cursor = _conn.cursor()
        q8 = """
            select s_nation, count(distinct l_orderkey) as co
            from V5, V2, lineitem
            where o_orderkey = l_orderkey
                and l_suppkey = s_suppkey
                and o_orderstatus = 'F'
                and o_orderyear like '1995'
            group by s_nation
            having co > 50;
        """
        cursor.execute(q8)
        output = open('output/8.out', 'w')
        
        for row in cursor.fetchall():
            r = '{:<1}|{:<10}'.format(row[0],row[1])
            print(r, file = output)
    except Error as e:
        print(e)
    print("++++++++++++++++++++++++++++++++++")


def Q9(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q9")
    try:
        cursor = _conn.cursor()
        q9 = """
            select count(distinct o_clerk)
            from V2, V5, lineitem
            where o_orderkey = l_orderkey
                and l_suppkey = s_suppkey
                and s_nation = 'UNITED STATES';
        """
        cursor.execute(q9)
        output = open('output/9.out', 'w')
        
        for row in cursor.fetchall():
            r = '{:<1}'.format(row[0])
            print(r, file = output)
    except Error as e:
        print(e)
    print("++++++++++++++++++++++++++++++++++")


def Q10(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q10")
    try:
        cursor = _conn.cursor()
        q10 = """
            select p_type, min_discount, max_discount
            from V10
                WHERE p_type like '%ECONOMY%'
                and p_type like '%COPPER%'
            group by p_type;
        """
        cursor.execute(q10)
        output = open('output/10.out', 'w')
        
        for row in cursor.fetchall():
            r = '{:<1}|{:<10}|{:<20}'.format(row[0],row[1], row[2])
            print(r, file = output)
    except Error as e:
        print(e)
    print("++++++++++++++++++++++++++++++++++")


def Q11(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q11")
    try:
        cursor = _conn.cursor()
        q11 = """
            select s.s_region, s.s_name, s.s_acctbal
            from V2 s
            WHERE s.s_acctbal = (select max(s1.s_acctbal)
                                    from V2 s1
                                    WHERE s.s_region = s1.s_region
                                );

        """
        cursor.execute(q11)
        output = open('output/11.out', 'w')
        
        for row in cursor.fetchall():
            r = '{:<1}|{:<10}|{:<20}'.format(row[0],row[1], row[2])
            print(r, file = output)
    except Error as e:
        print(e)
    print("++++++++++++++++++++++++++++++++++")


def Q12(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q12")
    try:
        cursor = _conn.cursor()
        q12 = """
            select s_nation, max(s_acctbal) as mb
            from V2
            group by s_nation
            having mb > 9000;
        """
        cursor.execute(q12)
        output = open('output/12.out', 'w')
        
        for row in cursor.fetchall():
            r = '{:<1}|{:<10}'.format(row[0],row[1])
            print(r, file = output)
    except Error as e:
        print(e)
    print("++++++++++++++++++++++++++++++++++")


def Q13(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q13")
    try:
        cursor = _conn.cursor()
        q13 = """
            select count(*)
            from orders, lineitem, V1, V2
            where o_orderkey = l_orderkey
                and o_custkey = c_custkey
                and l_suppkey = s_suppkey
                and s_region = 'AFRICA'
                and c_nation = 'UNITED STATES';

        """
        cursor.execute(q13)
        output = open('output/13.out', 'w')
        
        for row in cursor.fetchall():
            r = '{:<1}'.format(row[0])
            print(r, file = output)
    except Error as e:
        print(e)
    print("++++++++++++++++++++++++++++++++++")

    
def Q14(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q14")
    try:
        cursor = _conn.cursor()
        q14 = """
            select s_region as suppRegion, c_region as custRegion, max(o_totalprice)
            from lineitem, orders, V1, V2
            where l_suppkey = s_suppkey   --r1 supp region --r2 customer region
                and l_orderkey = o_orderkey             
                and o_custkey = c_custkey
            group by s_region, c_region;
        """
        cursor.execute(q14)
        output = open('output/14.out', 'w')
        
        for row in cursor.fetchall():
            r = '{:<1}|{:<10}|{:<20}'.format(row[0],row[1], row[2])
            print(r, file = output)
    except Error as e:
        print(e)
    print("++++++++++++++++++++++++++++++++++")


def Q15(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q15")
    try:
        cursor = _conn.cursor()
        q15 = """
            select count(distinct l_orderkey)
            from lineitem, V152, orders, V151
            where l_suppkey = s_suppkey
                and l_orderkey = o_orderkey
                and o_custkey = c_custkey;
        """
        cursor.execute(q15)
        output = open('output/15.out', 'w')
        
        for row in cursor.fetchall():
            r = '{:<1}'.format(row[0])
            print(r, file = output)
    except Error as e:
        print(e)
    print("++++++++++++++++++++++++++++++++++")


def main():
    database = r"tpch.sqlite"

    # create a database connection
    conn = openConnection(database)
    with conn:
        create_View1(conn)
        Q1(conn)

        create_View2(conn)
        Q2(conn)

        Q3(conn)
        Q4(conn)

        create_View5(conn)
        Q5(conn)

        Q6(conn)
        Q7(conn)
        Q8(conn)
        Q9(conn)

        create_View10(conn)
        Q10(conn)

        Q11(conn)
        Q12(conn)
        Q13(conn)
        Q14(conn)

        create_View151(conn)
        create_View152(conn)
        Q15(conn)

    closeConnection(conn, database)


if __name__ == '__main__':
    main()
