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


def createPriceRange(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Create PriceRange")
    # Create table called PriceRange, that contains maker, type, minPrice, maxPrice
    # Compute max and min for each type and maker 
    try:
        cursor = _conn.cursor()
        drop = """
            DROP VIEW IF EXISTS [PriceRange]"""
        cursor.execute(drop)

        create = """
            CREATE VIEW IF NOT EXISTS [PriceRange] AS 
            SELECT maker, Product.type, MIN(PC.price), MAX(PC.price), 
            MIN(Laptop.price), MAX(Laptop.price), MIN(Printer.price), 
            MAX(Printer.price) FROM Product
            LEFT JOIN PC ON Product.model = PC.model
            LEFT JOIN Laptop ON Product.model = Laptop.model
            LEFT JOIN Printer ON Product.model = Printer.model
            GROUP BY Product.type, maker
            ORDER BY Product.type
            """
        cursor.execute(create)

        _conn.commit()
        print("success")
    except Error as e:
        print(e)
    print("++++++++++++++++++++++++++++++++++")


def printPriceRange(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Print PriceRange")
    
    l = '{:<10} {:<20} {:>20} {:>20}'.format("maker", "product", "minPrice", "maxPrice")
    print(l)
    cursor = _conn.cursor()
    cursor.execute("SELECT * FROM PriceRange ORDER BY maker, type")
    rows = cursor.fetchall()
    
    try:
        i = 0
        for row in rows:
            i += 1
            if row[1] == 'pc':
                list = '{:<10} {:<20} {:>20} {:>20}'.format(row[0], row[1], row[2], row[3])
                print(list)
            elif row[1] == 'laptop':
                list = '{:<10} {:<20} {:>20} {:>20}'.format(row[0], row[1], row[4], row[5])
                print(list)
            elif row[1] == 'printer':
                list = '{:<10} {:<20} {:>20} {:>20}'.format(row[0], row[1], row[6], row[7])
                print(list)
        _conn.commit()
        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def insertPC(_conn, _maker, _model, _speed, _ram, _hd, _price):
    print("++++++++++++++++++++++++++++++++++")
    l = 'Insert PC ({}, {}, {}, {}, {}, {})'.format(_maker, _model, _speed, _ram, _hd, _price)
    print(l)
    try:
        cursor = _conn.cursor()

        # DELETE conflicting PC models, and conflicting model, types, and maker for Products
        cursor.execute("DELETE FROM PC WHERE model = ?", (_model,))
        cursor.execute("DELETE FROM Product WHERE model = ? AND type = ? AND maker = ?", (_model, 'pc', _maker))

        # Now we insert PC and Product.
        cursor.execute("INSERT into PC (model, speed, ram, hd, price) values (?, ?, ?, ?, ?)",
            (_model, _speed, _ram, _hd, _price))
        cursor.execute("INSERT into Product (maker, model, type) values (?, ?, ?)",
            (_maker, _model, 'pc'))
        _conn.commit()
        print("success")
    except Error as e:
        print(e)
    
    print("++++++++++++++++++++++++++++++++++")


def updatePrinter(_conn, _model, _price):
    print("++++++++++++++++++++++++++++++++++")
    l = 'Update Printer ({}, {})'.format(_model, _price)
    print(l)
    try:
        cursor = _conn.cursor()
        cursor.execute("UPDATE Printer SET price = ? WHERE model = ?" , (_price, _model))
        _conn.commit()
        print("success")
    except Error as e:
        print(e)
    print("++++++++++++++++++++++++++++++++++")


def deleteLaptop(_conn, _model):
    print("++++++++++++++++++++++++++++++++++")
    l = 'Delete Laptop ({})'.format(_model)
    print(l)
    try:
        cursor = _conn.cursor()
        cursor.execute("DELETE FROM Laptop WHERE model = ?", (_model,)) #Need to add a comma at the end
        # because parameter needs to be a tuple.
        cursor.execute("DELETE FROM Product WHERE model = ?", (_model,))
        _conn.commit()
        print("success")
    except Error as e:
        print(e)
    print("++++++++++++++++++++++++++++++++++")


def main():
    database = r"data.sqlite"

    # create a database connection
    conn = openConnection(database)
    with conn:
        createPriceRange(conn)
        printPriceRange(conn)

        file = open('input.in', 'r')
        lines = file.readlines()
        for line in lines:
            print(line.strip())

            tok = line.strip().split(' ')
            if tok[0] == 'I':
                insertPC(conn, tok[2], tok[3], tok[4], tok[5], tok[6], tok[7])
            elif tok[0] == 'U':
                updatePrinter(conn, tok[2], tok[3])
            elif tok[0] == 'D':
                deleteLaptop(conn, tok[2])

            printPriceRange(conn)

        file.close()

    closeConnection(conn, database)


if __name__ == '__main__':
    main()
