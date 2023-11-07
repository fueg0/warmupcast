from flask import Flask, render_template, redirect, url_for, request
from db import *

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/default")
def default():
    return render_template("layout.html")


@app.route("/variable")
def var():
    user = "Geeksforgeeks"
    return render_template("variable_example.html", name=user)


@app.route("/if")
def ifelse():
    user = "Practice GeeksforGeeks"
    return render_template("if_example.html", name=user)


@app.route("/for")
def for_loop():
    list_of_courses = ['Java', 'Python', 'C++', 'MATLAB']
    return render_template("for_example.html", courses=list_of_courses)


@app.route("/choice/<pick>")
def choice(pick):
    if pick == 'variable':
        return redirect(url_for('var'))
    if pick == 'if':
        return redirect(url_for('ifelse'))
    if pick == 'for':
        return redirect(url_for('for_loop'))


@app.route("/racks")
def racks():
    practice_racks = ["Tall Rack", "Zarchdan Rack", "Forklift Rack", "Mini Rack"]
    return render_template("rack_page_landing.html", racks=practice_racks)


@app.route("/clear_table")
def clear_rack():
    # refresh page to empty variables
    # refresh names if table already empty (double refresh)
    # render selected_rack_page
    pass


@app.route("/display_example")
def display_example():
    return render_template("display_example.html")


@app.route("/save_table/<num>", methods=['POST'])
def set_rack(num):
    app_connection = get_db_conn('rack_info.db')
    app_cursor = app_connection.cursor()
    app_cursor.execute(f"SELECT * FROM lifters WHERE rack_id={num}")
    rack_info = app_cursor.fetchall()

    for lifter in rack_info:
        update = False
        lifter_name = lifter[0]
        new_warmups = lifter[2]
        new_unit = lifter[3]

        if request.form[f"warmup_{lifter_name}"] != lifter[2]:
            update = True
            new_warmups = sql_str(request.form[f"warmup_{lifter_name}"])

        if request.form[f"unit_{lifter_name}"] != lifter[3]:
            update = True
            new_unit = request.form[f"unit_{lifter_name}"]

        if update:
            lifter_name = sql_str(lifter_name)
            app_cursor.execute(f"UPDATE lifters SET units={new_unit} WHERE name={lifter_name}")
            app_connection.commit()
            app_cursor.execute(
                f"UPDATE lifters SET warmups={new_warmups} WHERE name={lifter_name}")
            app_connection.commit()

        app_connection.commit()

    for item in request.form:
        print(item)

    app_cursor.execute(f"SELECT * FROM lifters WHERE rack_id={num}")
    rack_info = app_cursor.fetchall()
    app_connection.close()

    # call updateDisplay
    # updateDisplay checks DB, re-renders,

    return render_template(f"racks/{num}.html", num=rack_num, info=rack_info)
    # set table to data variable
    # send data to organize_inputs (main.py)
    # set variables for table
    # set variables for display
    pass


@app.route("/racks/<rack_num>")
def rack_num(rack_num):
    app_connection = get_db_conn('rack_info.db')
    app_cursor = app_connection.cursor()
    app_cursor.execute(f"SELECT * FROM lifters WHERE rack_id={rack_num}")
    rack_info = app_cursor.fetchall()
    app_connection.close()
    print(rack_info)

    for lifter in rack_info:
        print(lifter[0])

    return render_template(f"racks/{rack_num}.html", num=rack_num, info=rack_info)


if __name__ == "__main__":
    app.run(debug=False)
