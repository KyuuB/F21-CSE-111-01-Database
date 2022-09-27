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


def T1(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("T1")

    with open("output/1.out", "w") as file:
        header = "{:>10}\n".format("orders")
        file.write(header)

    try:
        sql = """SELECT COUNT(DISTINCT l_orderkey)
                    FROM supplier, lineitem, part, partsupp
                    WHERE l_suppkey = s_suppkey
                    AND l_partkey = p_partkey
                    AND p_partkey = ps_partkey
                    AND ps_suppkey = s_suppkey
                    AND ps_suppkey = s_suppkey;"""
        cur = _conn.cursor()
        cur.execute(sql)
        result = cur.fetchall()
        for row in result:
            with open("output/1.out", "a") as file:
                results = "{:>9}\n" .format(row[0])
                file.write(results)

    except Error as e:
        _conn.rollback()
        print(e)
    

    print("++++++++++++++++++++++++++++++++++")


def T2(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("T2")

    with open("output/2.out", "w") as file:
        header = "{:<40} {:>10}\n".format("nation", "orders")
        file.write(header)

    try:
        sql = """SELECT n_name, COUNT(DISTINCT o_orderkey)
                FROM orders, nation, supplier, lineitem, 
                    part, partsupp
                WHERE o_orderkey = l_orderkey
                AND l_partkey = p_partkey
                AND l_suppkey = s_suppkey
                AND s_suppkey = ps_suppkey
                AND ps_partkey = p_partkey
                AND s_nationkey = n_nationkey
                GROUP BY s_nationkey
                HAVING COUNT(p_partkey) > 1;"""
        cur = _conn.cursor()
        cur.execute(sql)
        result = cur.fetchall()
        for row in result:
            with open("output/2.out", "a") as file:
                results = "{:<40} {:>10}\n".format(row[0], row[1])
                file.write(results)

    except Error as e:
        _conn.rollback()
        print(e)


    print("++++++++++++++++++++++++++++++++++")


def T3(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("T3")

    with open("input/3.in", "r") as file:
        k = int(file.readline().strip())
    with open("output/3.out", "w") as file:
        header = "{:<40} {:>10}\n".format("nation", "orders")
        file.write(header)

    try:
        
        cur = _conn.cursor()
        cur.execute("""SELECT n_name, COUNT(DISTINCT o_orderkey)
                FROM orders, nation, supplier, lineitem, 
                    part, partsupp
                WHERE o_orderkey = l_orderkey
                AND l_partkey = p_partkey
                AND l_suppkey = s_suppkey
                AND s_suppkey = ps_suppkey
                AND ps_partkey = p_partkey
                AND s_nationkey = n_nationkey
                GROUP BY s_nationkey
                HAVING COUNT(p_partkey) > ?""", (k,))
        result = cur.fetchall()
        for row in result:
            with open("output/3.out", "a") as file:
                results = "{:<40} {:>10}\n".format(row[0], row[1])
                file.write(results)

    except Error as e:
        _conn.rollback()
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def T4(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("T4")

    with open("output/4.out", "w") as file:
        header = "{:<40} {:<40} {:>10}\n".format("supReg", "custReg", "items")
        file.write(header)
    try:
        
        cur = _conn.cursor()
        cur.execute("""CREATE VIEW IF NOT EXISTS RegionItems AS
                        SELECT  s.r_name AS supReg, c.r_name AS custReg, COUNT(DISTINCT s_suppkey) AS itemNo
                        FROM supplier, customer, lineitem, region s, nation s, region c, nation c, orders
                        WHERE s.n_regionkey = s.r_regionkey
                        AND c.n_regionkey = s.r_regionkey
                        AND s.n_nationkey = supplier.s_nationkey
                        AND c.n_nationkey = customer.c_nationkey
                        AND l_suppkey = s_suppkey
                        AND o_custkey = customer.c_custkey
                        AND l_orderkey = o_orderkey
                        GROUP BY supReg, custReg;""")
        cur.execute("SELECT * FROM RegionItems;")
        result = cur.fetchall()
        for row in result:
            with open("output/4.out", "a") as file:
                results = "{:<40} {:<40} {:>10}\n".format(row[0], row[1], row[2])
                file.write(results)

    except Error as e:
        _conn.rollback()
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def T5(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("T5")

    with open("input/5.in", "r") as file:
        nation = file.readline().strip()

    with open("output/5.out", "w") as file:
        header = "{:<40} {:<40} {:>10}\n".format("supReg", "custReg", "items")
        file.write(header)

    try:
        
        cur = _conn.cursor()
        cur1 = _conn.cursor()
        cur.execute("""DELETE FROM lineitem
                        WHERE EXISTS (SELECT l_orderkey FROM supplier, nation, lineitem
                                    WHERE s_nationkey = n_nationkey
                                    AND l_suppkey = s_suppkey
                                    AND n_name = ?)""", (nation,))
        cur1.execute("""SELECT * FROM RegionItems;""")
        result = cur1.fetchall()
        for row in result:
            with open("output/5.out", "a") as file:
                results = "{:<40} {:<40} {:>10}\n".format(row[0], row[1], row[2])
                file.write(results)

    except Error as e:
        _conn.rollback()
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def T6(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("T6")

    with open("input/6.in", "r") as file:
        oldNation = file.readline().strip()
        newNation = file.readline().strip()

    with open("output/6.out", "w") as file:
        header = "{:<40} {:<40} {:>10}\n".format("supReg", "custReg", "items")
        file.write(header)

    
    cur1 = _conn.cursor()
        
    cur1.execute("""SELECT * FROM RegionItems;""")
    result = cur1.fetchall()
    for row in result:
        with open("output/6.out", "a") as file:
            results = "{:<40} {:<40} {:>10}\n".format(row[0], row[1], row[2])
            file.write(results)
    print("++++++++++++++++++++++++++++++++++")


def main():
    database = r"tpch.sqlite"

    # create a database connection
    conn = openConnection(database)
    with conn:
        T1(conn)
        T2(conn)
        T3(conn)
        T4(conn)
        T5(conn)
        T6(conn)

    closeConnection(conn, database)


if __name__ == '__main__':
    main()
