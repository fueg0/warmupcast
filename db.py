import sqlite3
import csv
import re

# define connection and cursor
connection = sqlite3.connect('rack_info.db')
cursor = connection.cursor()
# RACK_NAMES = ["Short", "Zarch", "Tall", "Tall 2", "Wasteland"]


def parse_numbers(input_str):
    # Use regular expression to find all integers or decimals in the string
    numbers = re.findall(r"\b\d+(\.\d+)?\b", input_str)

    # Convert the extracted strings to integers or floats
    parsed_numbers = []
    for num in numbers:
        if '.' in num:
            parsed_numbers.append(float(num))
        else:
            parsed_numbers.append(int(num))

    return parsed_numbers


def sql_str(str_to_format):
    return "\"" + str_to_format + "\""


def get_db_conn(db):
    conn = sqlite3.connect(db)
    return conn


def setup_from_csv(racks, lifters):
    with open(racks, 'r') as csvfile:
        reader = csv.DictReader(csvfile)

        for rack in reader:
            rack_num = rack["num"]
            rack_name = sql_str(rack["name"])
            try:
                cursor.execute(f"INSERT INTO racks VALUES ({rack_num}, {rack_name})")
            except sqlite3.IntegrityError:
                print(f"{rack_name} Rack already registered in WarmupCast")

    with open(lifters, 'r') as csvfile:
        reader = csv.DictReader(csvfile)

        for lifter in reader:
            lifter_name = sql_str(lifter["name"])
            rack_num = int(lifter["rack_num"])
            warmups = sql_str(lifter["warmups"])
            units = "TRUE" if lifter["units"] else "FALSE"

            try:
                cursor.execute(f"INSERT INTO lifters VALUES ({lifter_name}, {rack_num}, {warmups}, {units})")
            except sqlite3.IntegrityError:
                print(f"{lifter_name}\n Lifter already registered in WarmupCast")

    connection.commit()


def setup_from_db():
    pass


def test():
    # insert rack and lifter

    cursor.execute("INSERT INTO racks VALUES (0, \"Tall\")")
    cursor.execute("INSERT INTO racks VALUES (2, \"Forklift\")")
    cursor.execute("INSERT INTO racks VALUES (3, \"Wasteland\")")
    cursor.execute("INSERT INTO lifters VALUES ( \"Duncan Michaud\", 0, \"\", FALSE)")

    # get rack and lifter
    cursor.execute("SELECT * FROM racks")
    results = cursor.fetchall()
    print(results)

    cursor.execute("SELECT * FROM lifters")
    results = cursor.fetchall()
    print(results)

    # update
    cursor.execute("UPDATE racks SET rack_id = 1 WHERE rack_id = 2")

    cursor.execute("SELECT rack_id FROM racks")
    results = cursor.fetchall()
    print(results)

    # delete
    cursor.execute("DELETE FROM racks WHERE rack_id=3")

    cursor.execute("SELECT rack_id FROM racks")
    results = cursor.fetchall()
    print(results)

    connection.commit()


if __name__ == '__main__':
    # create racks table
    command_create = """CREATE TABLE IF NOT EXISTS
    racks(rack_id INTEGER UNIQUE PRIMARY KEY, name TEXT)"""
    cursor.execute(command_create)

    # create individual lifters table
    command_create_lifter = """CREATE TABLE IF NOT EXISTS
    lifters(name TEXT UNIQUE PRIMARY KEY, rack_id INTEGER, warmups TEXT, units BOOLEAN)"""
    cursor.execute(command_create_lifter)

    setup_from_csv("racks_data.csv", "lifters_data.csv")

    cursor.execute("SELECT * FROM racks")
    results = cursor.fetchall()
    print(results)
    cursor.execute("SELECT * FROM lifters")
    results = cursor.fetchall()
    print(results)
