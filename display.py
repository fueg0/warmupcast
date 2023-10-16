import sqlite3
import db
import Lifter


def get_db(index="*"):
    app_connection = db.get_db_conn('rack_info.db')
    app_cursor = app_connection.cursor()

    app_cursor.execute(f"SELECT * FROM lifters WHERE rack_id={index}")
    rack_info = app_cursor.fetchall()

    data = []
    for lifter in rack_info:
        lifter_info = {"name": lifter[0],
                       "warmups": lifter[2],
                       "unit": lifter[3]
                       }

        lifter_info["warmups"] = db.parse_numbers(lifter_info["warmups"])
        data.append(lifter_info)

    warmups = Lifter.organize_input(data)


